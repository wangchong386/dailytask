## kafka安装
### kafka安装
* 这步很简单，先是在parcels下载本地源，然后下载，分发，安装并激活一系列手动页面操作。
![](images/kafka5.png)
* 然后添加服务
![](images/kafka6.png)
等等按顺序操作。即可安装成功：
![](images/kafka7.png)
CDH kafka安装很简单也很方便，所以就大概说下
### kafka需要注意：
* kafka broker的平稳关闭
如果kafka broker没有正常关闭，则后续的重启可能需要比预期更多的时间。当broker花费超过30秒钟的时间，在停止Kafka服务，停止Kafka broker角色或停止运行Kafka服务的集群时，可能会发生这种情况。 kafka broker也被关闭，作为升级的一部分。 您可以设置两个配置属性来控制Cloudera Manager是否等待broker平稳地关闭：
