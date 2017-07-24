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
