## CDH kafka问题总结
### 1.org.apache.kafka.common.errors.TimeoutException
* 症状:
```
[2017-06-05 19:06:37,254] ERROR Error when sending message to topic kafkatest with key: null, value: 4 bytes with error: (org.apache.kafka.clients.producer.internals.ErrorLoggingCallback)
org.apache.kafka.common.errors.TimeoutException: Failed to update metadata after 60000 ms.
```
* 原因：
原因是kafka客户端连接到broker是成功的，但连接到集群后更新回来的集群meta信息是错误的即是会返回的是节点的hostname，解决办法就是手动配置`advertised.host.name`和`advertised.port`，2个参数都必须配置，重启问题解决：
```
advertised.host.name=10.0.0.100
advertised.port=9092
```
### 2. java.io.FileNotFoundException: /data00/kafka/data/.lock (Permission denied)
* 症状：
```
Fatal error during KafkaServerStartable startup. Prepare to shutdown
java.io.FileNotFoundException: /data00/kafka/data/.lock (Permission denied)
	at java.io.RandomAccessFile.open(Native Method)
	at java.io.RandomAccessFile.<init>(RandomAccessFile.java:241)
	at kafka.utils.FileLock.<init>(FileLock.scala:29)
	at kafka.log.LogManager$$anonfun$lockLogDirs$1.apply(LogManager.scala:98)
	at kafka.log.LogManager$$anonfun$lockLogDirs$1.apply(LogManager.scala:97)
	at scala.collection.TraversableLike$$anonfun$map$1.apply(TraversableLike.scala:234)
	at scala.collection.TraversableLike$$anonfun$map$1.apply(TraversableLike.scala:234)
	at scala.collection.IndexedSeqOptimized$class.foreach(IndexedSeqOptimized.scala:33)
	at scala.collection.mutable.WrappedArray.foreach(WrappedArray.scala:35)
	at scala.collection.TraversableLike$class.map(TraversableLike.scala:234)
	at scala.collection.AbstractTraversable.map(Traversable.scala:104)
	at kafka.log.LogManager.lockLogDirs(LogManager.scala:97)
	at kafka.log.LogManager.<init>(LogManager.scala:59)
	at kafka.server.KafkaServer.createLogManager(KafkaServer.scala:611)
	at kafka.server.KafkaServer.startup(KafkaServer.scala:183)
	at kafka.server.KafkaServerStartable.startup(KafkaServerStartable.scala:37)
	at kafka.Kafka$.main(Kafka.scala:67)
	at com.cloudera.kafka.wrap.Kafka$.main(Kafka.scala:76)
	at com.cloudera.kafka.wrap.Kafka.main(Kafka.scala)
```
* 原因：
在CDH添加了两台kafka机器，发现没有硬盘。运维后来将两台kafka机器磁盘已经加上，并做了raid。并已经在CDH上显示。但是数据目录没有检测到该磁盘路径。需要手动进行添加。最好是从原来的/var/local/kafka/data目录进行拷贝。但是拷贝之重新重启kafka broker.会报以上的错误，明显是权限的错误。
原来是以前/kafka/data/.lock文件是kafka用户和kafka用户组的，我是用root账号进行复制的，所以出错。