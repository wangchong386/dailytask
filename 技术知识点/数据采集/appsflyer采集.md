## appsflyer？
> AppsFlyer成立于2011年，是全球领先的移动APP广告效果监测分析平台，提供APP应用的广告跟踪、评估等技术服务。AppsFlyer总部位于以色列，在全球各地包括美国旧金山、纽约和泰国、中国、韩国、日本、印度等亚太地区均设有办事处。AppsFlyer是Facebook和Twitter官方认证的移动评估合作伙伴，在中国的客户包括智明星通、IGG、百度、中国手游、携程、乐逗游戏、昆仑乐享和奇虎等

## appsflyer生产环境使用
### 
* 解析路径
/usr/local/project/appsflyer_receiver_v0/appsflyer_receiver_run.sh

```
#!/bin/sh

if [ $(whoami) != 'hdfs' ]; then
    echo "Please run this script as hdfs"
    exit 1
fi


basedir=appsflyer_receiver
projectdir="/usr/local/project/$basedir"
classpath="$projectdir/lib/*"
echo $projectdir
cd $projectdir


echo "start appsflyer_receiver"
nohup /usr/local/jdk1.7.0_55/bin/java -cp "lib/*" com.dhgate.appsflyerlog.HttpServer \
        > /dev/null 2>&1 &
echo "run in the background"

```
### 使用pig脚本将其转化到hdfs中
```
#!/bin/sh

#=============================================================================
# 获取当前时间的上一个小时，如果当前是00点则取前一天的23点数据
# appsflyerlog.2015-11-26_06.log
#=============================================================================
if  [ ! -n "$1" ] ;then
    etl_date=$(date '+%Y-%m-%d')
    hour=$(date -d "1 hour ago" '+%H')
    if [ "$hour" = "23" ]; then
        etl_date=$(date -d "-1 day $etl_date" '+%Y-%m-%d')
    fi
    echo $etl_date $hour
else
    etl_date=$1
    hour=$2
fi

dt=$(date -d "$etl_date" "+%Y-%m-%d")

# 日志路径
readonly log_file_path='/data/track/appsflyerlog'
# HDFS路径
readonly hdfs_table_path='/dw/ods/ods_log_appsflyer'
# log日志集中存放
readonly log_file_local='/data/appsflyerlog'

# 日志文件名称
# 例如 appsflyerlog.2015-11-26_06.log
log_file_name="appsflyerlog.${etl_date}_${hour}.log"

# Load前清理HDFS历史数据
target_hdfs_path="$hdfs_table_path/dt=$dt/hour=$hour"
hadoop fs -rm -r    $target_hdfs_path
hadoop fs -mkdir -p $target_hdfs_path

#=============================================================================
# 将log文件集中到一台server后转存到hive表分区
#=============================================================================
cat <<EOF | xargs -I {} scp {}:"$log_file_path/$log_file_name" "$log_file_local/{}_$log_file_name"
appsflyer1
EOF

hive -hiveconf dt="$dt" \
     -hiveconf hour="$hour" \
     -hiveconf log_file_local="$log_file_local" \
     -hiveconf log_file_name="$log_file_name" \
     -f /dw/ods/log/hsql/ods_log_appsflyer.sql

```
### ETL清洗转换并生成报表提供给业务人员
* /dw/ods/log/hsql/ods_log_appsflyer.sql

```
set hive.exec.compress.output=true;
set mapred.output.compress=true;
set mapred.output.compression.codec=org.apache.hadoop.io.compress.GzipCodec;
LOAD DATA local INPATH
    '${hiveconf:log_file_local}/*${hiveconf:log_file_name}'
    OVERWRITE INTO TABLE ods_log_appsflyer
    PARTITION (dt='${hiveconf:dt}',hour='${hiveconf:hour}');

```