### 最终页模块逻辑
![](images/hivesql1.png)

#### 一、 一般曝光模块
路径：
（1）-（4）-（5）

* 语言&站点：
要求最终页的语言和站点与下单时的语言和站点一样

* 时间性：
  * 要求在最终页的当天完成下单；
  * 下单时间在最终页时间之后；
  * 订单在下单的当天或者第二天完成confirm；

* 其它通用限制条件：
vid不为空

* 关联条件：
vid 或者 buyerid    item_code


#### 二、特殊曝光模块说明（搜索+推荐）

* 搜索（click_position rlike '^s[0-9]+'）
* 路径：
（1）-（4）-（5）
搜索www需要有一个特殊处理，就是列表页加入购物车情况
（2）-（4）-（5）

* 语言&站点&时间性：
同上

* 其它通用限制条件：
同上+UUID不为空

* 关联条件：
同上+UUID

* 推荐
路径：
后端曝光-（1）-（4）-（5）
后端曝光见下面说明d)；历史推荐不能限制UUID和后端曝光，只能通过#tracking来限定（1）-（4）-（5）
其余限制同搜索


#### 三、一些表和数据说明
* a)最终页#tracking的第一段在click_position字段，具体参考下面的整理
![](images/hivesql2.png)
* b)下单时的vid选用ods_rfx_prod_ext.vid字段
   * 说明：线上付款成功页succ记录的订单vid与ods_rfx_prod_ext.vid的匹配度达到95%；所以放弃付款成功页这个限制条件（线下付款不会走这个页面，以及付款成功页经常也出现加载问题）
* c)放弃了上次讨论时的Checkout_U0001事件的限制
   * 说明：经过与搜索和推荐的同事讨论，业务认为一个模块的曝光，目的是有效曝光让用户当天完成购买，但很难让用户在这个模块完成加购物车的动作；不建议lastclick的归因方法，建议给购物车之前的每个路径都归因；
   * 数据：有27%的下单用户，会在购买这个产品之前按从2个及以上不同的位置查看最终页，这部分GMV会归因到多个位置
* d)推荐的后端事件表为ods_log_rec_s，这个表2016.4月才开始添加；所以推荐的历史数据没有UUID
* e)当天完成下单
      * www上，当天下单的订单中，有81%在当天有对应的最终页事件
      * wap上，当天下单的订单中，有91%在当天有对应的最终页事件
      * www对比wap值低的一部分原因是列表页直接加购物车
* f)当天或者第二天完成confirm
      * 订单在下单当天完成confim的占92%；
      * 当天或者第二天完成confirm的占96%

#### 四、sql举例
* www首页右侧you may like位置的GMV（推荐位）
* URL示例：
http://www.mmmm.com/product/2013-red-wedding-dresses-lace-tulle-applique/156892617.html?recinfo=22,101,1#hp1507_recm-1-5|null:101:1177089674
* 备注：这个#码是5.31号修改的，所以这样跑没有数据，sql仅是举例
非推荐的去掉rec表和uuid的限制

```

select t.dt, count(distinct t.rfx_no) orders, sum(t.prod_gmv) gmv
  from (select distinct item.vid,
                        item.item_code,
                        item.dt,
                        m.rfx_no,
                        m.started_date,
                        m.prod_gmv
          from (select distinct v.vid,
                                v.item_code,
                                v.dt,
                                from_unixtime(cast(vt / 1000 as bigint),
                                              'yyyy-MM-dd HH:mm:ss') vt,
                                v.user_id,
                                uuid
                  from ods_log_pageview v
                 where v.dt = '2016-05-18'
                   and dt <= '2016-05-24'
                   and v.track_id = 'Item_U0001'
                   and v.site = 'www'
                   and vid is not null
                   and vid <> ''
                   and uuid is not null
                   and uuid <> ''
                   and click_position = 'hp1507_recm') item
         inner join (select distinct s.uuid, s.vid, dt
                      from ods_log_rec_s s
                     where s.dt = '2016-05-18'
                       and dt <= '2016-05-24'
                       and uuid is not null
                       and vid is not null
                       and uuid <> ''
                       and vid <> ''
                       and site = 'www') rec
            on item.vid = rec.vid
           and item.uuid = rec.uuid
           and item.dt = rec.dt
         inner join (select a.rfx_no,
                           item_code,
                           prod_gmv,
                           c.vid,
                           a.buyer_id,
                           a.started_date
                      from (select rfx_no, started_date, buyer_id
                              from mds_rfx_info
                             where dt = '2016-05-25'
                               and to_date(started_date) = '2016-05-18'
                               and to_date(started_date) <= '2016-05-24'
                               and confirm_date is not null
                               and confirm_date <> ''
                               and datediff(to_date(confirm_date),
                                            to_date(started_date)) <= 1
                               and (visit_detail_info not like 'mobile_p%' or
                                   visit_detail_info is null)) a
                     inner join (select rfx_no,
                                       item_code,
                                       rfx_prod_id,
                                       prod_gmv
                                  from mds_rfx_prod
                                 where dt = '2016-05-25') b
                        on a.rfx_no = b.rfx_no
                     inner join (select rfx_prod_ext_id, vid, rfx_no
                                  from ods_rfx_prod_ext
                                 where dt = '2016-05-25') c
                        on b.rfx_prod_id = c.rfx_prod_ext_id
                       and b.rfx_no = c.rfx_no) m
            on item.item_code = m.item_code
         where (item.vid = m.vid or item.user_id = m.buyer_id)
           and m.started_date > item.vt
           and datediff(to_date(m.started_date), to_date(item.vt)) = 0) t
 group by t.dt
 order by dt;

```
