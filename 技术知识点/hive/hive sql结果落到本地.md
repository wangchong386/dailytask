## hive sql开发
### 1. 如何将hive sql执行结果落到本地目录，并进行压缩：
```
#!/bin/sh
##装载conf文件
. /dw/config/hive_config.conf

##表名##
stab=table_name

##获取ETL运行日期
if  [ ! -n "$1" ] ;then
run_date
else
run_date $1
fi

write_log "[INFO]" "$stab" "etl_start" "$etl_date" "etl数据加工开始"

data_dir="/var/lib/hadoop-hdfs/wangchong/data/$etl_date"
v_sql_1="


"

hive -e "$v_sql_1"
cd $data_dir
cat 000* > tmp
rm -rf 000*
cat tmp > 000000_0
gzip --best 000000_0
rm -rf tmp
touch "${data_dir}/status.ok"
rm "${data_dir}/".*.crc 2> /dev/null

write_log "[INFO]" "$stab" "etl_end" "$etl_date" "etl数据加工完成"

```


