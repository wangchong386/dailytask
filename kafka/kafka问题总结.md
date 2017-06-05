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