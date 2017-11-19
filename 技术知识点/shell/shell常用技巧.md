### for循环
*  for循环
```
 #!/bin/sh
 for etl_date in 2016-06-{01..30} \
                 2016-07-{01..02}
    do
    echo $etl_date
    done |
  xargs -P 12 -I {} bash -c 'echo sh  test.sh {}'
```
```
 #!/bin/sh
 for((i=1;i<34;i++))
 do
 etl_date=`date -d "$i day ago" +%Y-%m-%d` 
 sh sds_lp_visit_detail.sh $etl_date
 Done
 ```
 
 http://man.linuxde.net/
 *  批量挂载分区
 ```
 for d in 2016-06-{08..21}; 
 do echo $d; 
 done | xargs -I {} echo "alter table sds_rpt.rpt_bi_pvuv_channel add partition (dt ='{}')"
```
