## spark-submit出错

## 现象1：build Artifacts时报错Java.lang.outofmemoryerror

* 报错信息：
```
17/06/23 16:49:11 INFO Client:
         client token: N/A
         diagnostics: Application application_1496750989788_98736 failed 3 times due to AM Container for appattempt_1496750989788_98736_000003 exited with  exitCode: 15
For more detailed output, check application tracking page:http://d1-datanode34:8088/proxy/application_1496750989788_98736/Then, click on links to logs of each attempt.
Diagnostics: Exception from container-launch.
Container id: container_e04_1496750989788_98736_03_000001
Exit code: 15
Stack trace: ExitCodeException exitCode=15:
        at org.apache.hadoop.util.Shell.runCommand(Shell.java:543)
        at org.apache.hadoop.util.Shell.run(Shell.java:460)
        at org.apache.hadoop.util.Shell$ShellCommandExecutor.execute(Shell.java:720)
        at org.apache.hadoop.yarn.server.nodemanager.DefaultContainerExecutor.launchContainer(DefaultContainerExecutor.java:210)
        at org.apache.hadoop.yarn.server.nodemanager.containermanager.launcher.ContainerLaunch.call(ContainerLaunch.java:302)
        at org.apache.hadoop.yarn.server.nodemanager.containermanager.launcher.ContainerLaunch.call(ContainerLaunch.java:82)
        at java.util.concurrent.FutureTask.run(FutureTask.java:262)
        at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1145)
        at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:615)
        at java.lang.Thread.run(Thread.java:745)


Container exited with a non-zero exit code 15
Failing this attempt. Failing the application.
         ApplicationMaster host: N/A
         ApplicationMaster RPC port: -1
         queue: root.hdfs
         start time: 1498207562288
         final status: FAILED
         tracking URL: http://d1-datanode34:8088/cluster/app/application_1496750989788_98736
         user: hdfs
Exception in thread "main" org.apache.spark.SparkException: Application application_1496750989788_98736 finished with failed status
        at org.apache.spark.deploy.yarn.Client.run(Client.scala:927)
        at org.apache.spark.deploy.yarn.Client$.main(Client.scala:973)
        at org.apache.spark.deploy.yarn.Client.main(Client.scala)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.lang.reflect.Method.invoke(Method.java:606)
        at org.apache.spark.deploy.SparkSubmit$.org$apache$spark$deploy$SparkSubmit$$runMain(SparkSubmit.scala:672)
        at org.apache.spark.deploy.SparkSubmit$.doRunMain$1(SparkSubmit.scala:180)
        at org.apache.spark.deploy.SparkSubmit$.submit(SparkSubmit.scala:205)
        at org.apache.spark.deploy.SparkSubmit$.main(SparkSubmit.scala:120)
        at org.apache.spark.deploy.SparkSubmit.main(SparkSubmit.scala)
17/06/23 16:49:12 INFO ShutdownHookManager: Shutdown hook called
17/06/23 16:49:12 INFO ShutdownHookManager: Deleting directory /tmp/spark-50f0dc10-789f-48a1-8126-415b8fe1401c

```
* 报错信息显示：
`Application application_1496750989788_98736 failed 3 times due to AM Container for appattempt_1496750989788_98736_000003`

-- 该`application_1496750989788_98736`失败了三次并退出
* 将日志打印出来进行查看：`yarn logs -applicationId application_1496750989788_98736`
```
org.apache.spark.SparkException: Only one SparkContext may be running in this JVM (see SPARK-2243). To ignore this error, set spark.driver.allowMultipleContexts = true. The curr
ently running SparkContext was created at:
org.apache.spark.SparkContext.<init>(SparkContext.scala:82)
org.apache.spark.streaming.StreamingContext$.createNewSparkContext(StreamingContext.scala:854)
org.apache.spark.streaming.StreamingContext.<init>(StreamingContext.scala:81)
org.apache.spark.streaming.api.java.JavaStreamingContext.<init>(JavaStreamingContext.scala:134)
dh.bigdata.etl.Main.main(Main.java:34)
sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
java.lang.reflect.Method.invoke(Method.java:606)
```