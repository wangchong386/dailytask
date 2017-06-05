## Using Kafka with Flume
> In CDH 5.2 and higher, Flume contains a Kafka source and sink. Use these to stream data from Kafka to Hadoop or from any Flume source to Kafka.
In CDH 5.7 and higher, the Flume connector to Kafka only works with Kafka 2.0 and higher.

### Kafka Source
> 使用kafka source 将kafka topic中的数据传输到hadoop中。kafka可以与任何flume sink结合使用，可以方便的将kafka中的数据写入到hdfs，hbase和solr

__示例__

```
tier1.sources  = source1
 tier1.channels = channel1
 tier1.sinks = sink1
 
 tier1.sources.source1.type = org.apache.flume.source.kafka.KafkaSource
 tier1.sources.source1.zookeeperConnect = zk01.example.com:2181
 tier1.sources.source1.topic = weblogs
 tier1.sources.source1.groupId = flume
 tier1.sources.source1.channels = channel1
 tier1.sources.source1.interceptors = i1
 tier1.sources.source1.interceptors.i1.type = timestamp
 tier1.sources.source1.kafka.consumer.timeout.ms = 100
 
 tier1.channels.channel1.type = memory
 tier1.channels.channel1.capacity = 10000
 tier1.channels.channel1.transactionCapacity = 1000
 
 tier1.sinks.sink1.type = hdfs
 tier1.sinks.sink1.hdfs.path = /tmp/kafka/%{topic}/%y-%m-%d
 tier1.sinks.sink1.hdfs.rollInterval = 5
 tier1.sinks.sink1.hdfs.rollSize = 0
 tier1.sinks.sink1.hdfs.rollCount = 0
 tier1.sinks.sink1.hdfs.fileType = DataStream
 tier1.sinks.sink1.channel = channel1
```
* 为了更高的吞吐量，配置多kafka sources从相同的topic读取，如果你配置所有的source使用相同的groupId,topic包含多分区。每个源从不同的分区集读取数据，从而提高摄取速度。
* 下表介绍了Kafka source支持的参数。 必需的属性以粗体显示。
![](images/kafka11.png)