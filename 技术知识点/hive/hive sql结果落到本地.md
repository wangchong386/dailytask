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


### 2. hive sqlldr到oracle数据库

```
#!/bin/sh
##装载config文件
source /etc/profile
source ~/.bash_profile
whoami
echo $PATH
echo $CLASSPATH
. /dw/config/hive_config.conf
if  [ ! -n "$1" ] ;then
run_date
else
run_date $1
fi
hadoop fs -test -e /dw/table_name/dt=$etl_date
if [ $? -eq 0 ]; then
v_replace=`cat table_name.ctl|grep infile|awk -F "/" '{print $6}'`
echo $v_replace $etl_date
###echo "sed -i 's/$v_replace/$etl_date/g' table_name.ctl"
###sed -i -e 's/$v_replace/$etl_date/g' table_name.ctl
RS_EXEC=`sqlplus -S username/passwd@实例<<EOF
 set heading off
 set feedback off
 set pagesize 0
 set verify off
   begin
     delete from table_name where stat_Dt='$etl_date';
     commit;
   end;
  /
 exit
EOF`


echo "
load data
infile '/dw/DataFileShare/BI/table_name/$etl_date/000000_0.txt'
badfile '/dw/logs/$etl_date/table_name.bad'
discardfile 'table_name.discard'
append into table table_name
fields terminated by X\"07\" TRAILING NULLCOLS
(
cloumn1 ,
cloumn2
)">/dw/rpt/bi/sqlload/table_name.ctl
myPath=/dw/DataFileShare/BI/cloumn1/$etl_date
if [ ! -d "$myPath" ]; then
   mkdir -p  "$myPath"
else
rm  /dw/DataFileShare/BI/table_name/$etl_date/*
fi
###rm /dw/DataFileShare/BI/table_name/$etl_date/*
hadoop fs -get /dw/rpt/table_nam/dt=$etl_date/*  /dw/DataFileShare/BI/table_name/$etl_date/000000_0.txt
###cat table_nam.ctl
sqlldr username/passwd@实例  control=/dw/rpt/bi/sqlload/table_name.ctl log=/dw/rpt/bi/sqlload/table_name.log
exit 0
else
echo "源数据没有生成"
fi
exit 0

```

### 3. hive sqoop到关系型数据库
```
#!/bin/sh

##装载config文件
. /dw/config/hive_config.conf
##表名##
##获取ETL运行日期
if  [ ! -n "$1" ] ;then
    run_date
else
    run_date $1
fi
echo $etl_date


v_sql="
    set sql_safe_updates = 0;
    use reportdb;
    delete from table_name where report_date='$etl_date';
    commit;
    set sql_safe_updates = 1;
"
 echo $v_sql

# execute sql stat
mysql -ureport -h172.21.100.101 -P3316 -ppasswd<<!
$v_sql
!


sqoop export --connect jdbc:mysql://172.21.100.101:3316/reportdb \
--username username --password passwd --export-dir /dw/sds/table_name/dt=$etl_date/0* \
--table table_name --input-fields-terminated-by '\t' --input-null-string '\\N' \
--input-null-non-string '\\N' -m 1

```