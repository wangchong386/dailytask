## Spark基础知识解答
#### 1 . Spark是什么?
Spark基于mapreduce算法实现的分布式计算，拥有HadoopMapReduce所具有的优点;但不同于MapReduce的是Job中间输出和结果可以保存在内存中，从而不再需要读写HDFS，因此Spark能更好地适用于数据挖掘与机器学习等需要迭代的map reduce的算法
#### 2. Spark与Hadoop的对比(Spark的优势)
* Spark的中间数据放到内存中，对于迭代运算效率更高
* Spark比Hadoop更通用
* Spark提供了统一的编程接口
* 容错性– 在分布式数据集计算时通过checkpoint来实现容错
* 可用性– Spark通过提供丰富的Scala, Java，Python API及交互式Shell来提高可用性
#### 3. Spark有那些组件
* Spark Streaming：支持高吞吐量、支持容错的实时流数据处理
* Spark SQL， Data frames: 结构化数据查询
* MLLib：Spark 生态系统里用来解决大数据机器学习问题的模块
* GraphX是构建于Spark上的图计算模型
* SparkR是一个R语言包，它提供了轻量级的方式使得可以在R语言中使用 Spark
### 二. DataFrame相关知识点
#### 1. DataFrame是什么?
DataFrame是一种以RDD为基础的分布式数据集，类似于传统数据库中的二维表格。
#### 2. DataFrame与RDD的主要区别在于?
DataFrame带有schema元信息，即DataFrame所表示的二维表数据集的每一列都带有名称和类型。这使得SparkSQL得以洞察更多的结构信息，从而对藏于DataFrame背后的数据源以及作用于DataFrame之上的变换进行了针对性的优化，最终达到大幅提升运行时效率的目标。
反观RDD，由于无从得知所存数据元素的具体内部结构，Spark Core只能在stage层面进行简单、通用的流水线优化。
#### 3. DataFrame 特性
* 支持从KB到PB级的数据量
* 支持多种数据格式和多种存储系统
* 通过Catalyst优化器进行先进的优化生成代码
* 通过Spark无缝集成主流大数据工具与基础设施
* API支持Python、Java、Scala和R语言

### 三 . RDD相关知识点
#### 1. RDD，全称为?
Resilient Distributed Datasets，意为容错的、并行的数据结构，可以让用户显式地将数据存储到磁盘和内存中，并能控制数据的分区。同时，RDD还提供了一组丰富的操作来操作这些数据。
#### 2. RDD的特点?
* 它是在集群节点上的不可变的、已分区的集合对象。
* 通过并行转换的方式来创建如(map, filter, join, etc)。
* 失败自动重建。
* 可以控制存储级别(内存、磁盘等)来进行重用。
* 必须是可序列化的。
* 是静态类型的。
#### 3. RDD核心概念
* Client：客户端进程，负责提交作业到Master。
* Master：Standalone模式中主控节点，负责接收Client提交的作业，管理Worker，并命令Worker启动分配Driver的资源和启动Executor的资源。
* Worker：Standalone模式中slave节点上的守护进程，负责管理本节点的资源，定期向Master 汇报心跳，接收Master的命令，启动Driver和Executor。
* Driver： 一个Spark作业运行时包括一个Driver进程，也是作业的主进程，负责作业的解析、生成Stage并调度Task到Executor上。包括DAGScheduler，TaskScheduler。
* Executor：即真正执行作业的地方，一个集群一般包含多个Executor，每个Executor接收Driver的命令Launch Task，一个Executor可以执行一到多个Task。
#### 4. RDD常见术语
* DAGScheduler： 实现将Spark作业分解成一到多个Stage，每个Stage根据RDD的Partition个数决定Task的个数，然后生成相应的Task set放到TaskScheduler中。
* TaskScheduler：实现Task分配到Executor上执行。
* Task：运行在Executor上的工作单元。
* Job：SparkContext提交的具体Action操作，常和Action对应。
* Stage：每个Job会被拆分很多组任务(task)，每组任务被称为Stage，也称 TaskSet。
* RDD：Resilient Distributed Datasets的简称，弹性分布式数据集，是Spark最核心的模块和类。
* Transformation/Action：SparkAPI的两种类型;Transformation返回值还是一个RDD，Action返回值不少一个RDD，而是一个Scala的集合;所有的Transformation都是采用的懒策略，如果只是将Transformation提交是不会执行计算的，计算只有在Action被提交时才会被触发。
* DataFrame： 带有Schema信息的RDD，主要是对结构化数据的高度抽象。
* DataSet：结合了DataFrame和RDD两者的优势，既允许用户很方便的操作领域对象，又具有SQL执行引擎的高效表现。
#### 5. RDD提供了两种类型的操作：
transformation和action
* 1，transformation是得到一个新的RDD，方式很多，比如从数据源生成一个新的RDD，从RDD生成一个新的RDD
* 2，action是得到一个值，或者一个结果(直接将RDD cache到内存中)
* 3，所有的transformation都是采用的懒策略，就是如果只是将transformation提交是不会执行计算的，计算只有在action被提交的时候才被触发
#### 6. RDD中关于转换(transformation)与动作(action)的区别
transformation会生成新的RDD，而后者只是将RDD上某项操作的结果返回给程序，而不会生成新的RDD;无论执行了多少次transformation操作，RDD都不会真正执行运算(记录lineage)，只有当action操作被执行时，运算才会触发。
#### 7. RDD 与 DSM的最大不同是?
* DSM(distributed shared memory)
* RDD只能通过粗粒度转换来创建，而DSM则允许对每个内存位置上数据的读和写。在这种定义下，DSM不仅包括了传统的共享内存系统，也包括了像提供了共享 DHT(distributed hash table) 的 Piccolo 以及分布式数据库等。
#### 8. RDD的优势?
* 1、高效的容错机制
* 2、结点落后问题的缓和 (mitigate straggler)
* 3、批量操作
* 4、优雅降级 (degrade gracefully)
#### 9. 如何获取RDD?
* 1、从共享的文件系统获取，(如：HDFS)
* 2、通过已存在的RDD转换
* 3、将已存在scala集合(只要是Seq对象)并行化 ，通过调用SparkContext的parallelize方法实现
* 4、改变现有RDD的之久性;RDD是懒散，短暂的。
#### 10. RDD都需要包含以下四个部分
* a. 源数据分割后的数据块，源代码中的splits变量
* b. 关于“血统”的信息，源码中的dependencies变量
* c. 一个计算函数(该RDD如何通过父RDD计算得到)，源码中的iterator(split)和compute函数
* d. 一些关于如何分块和数据存放位置的元信息，如源码中的partitioner和preferredLocations0
#### 11. RDD中将依赖的两种类型
窄依赖(narrowdependencies)和宽依赖(widedependencies)。
* 窄依赖是指父RDD的每个分区都只被子RDD的一个分区所使用。相应的，那么宽依赖就是指父RDD的分区被多个子RDD的分区所依赖。例如，map就是一种窄依赖，而join则会导致宽依赖
依赖关系分类的特性：

* 第一，窄依赖可以在某个计算节点上直接通过计算父RDD的某块数据计算得到子RDD对应的某块数据;
* 第二，数据丢失时，对于窄依赖只需要重新计算丢失的那一块数据来恢复;
### Spark Streaming 相关知识点
#### 1. Spark Streaming的基本原理
Spark Streaming的基本原理是将输入数据流以时间片(秒级)为单位进行拆分，然后以类似批处理的方式处理每个时间片数据
#### RDD 基本操作
常见的聚合操作：

* count(*) 所有值不全为NULL时，加1操作
* count(1) 不管有没有值，只要有这条记录，值就加1
* count(col) col列里面的值为null，值不会加1，这个列里面的值不为NULL，才加1
* sum求和
* sum(可转成数字的值) 返回bigint
* avg求平均值
* avg(可转成数字的值)返回double
* distinct不同值个数
* count(distinct col)
#### 按照某些字段排序
* select col1,other... from table where conditio order by col1,col2 [asc|desc]
* Join表连接
* join等值连接(内连接)，只有某个值在m和n中同时存在时。
* left outer join 左外连接，左边表中的值无论是否在b中存在时，都输出;右边表中的值，只有在左边表中存在时才输出。
* right outer join 和 left outer join 相反。
Transformation具体内容
reduceByKey(func, [numTasks]) : 在一个(K，V)对的数据集上使用，返回一个(K，V)对的数据集，key相同的值，都被使用指定的reduce函数聚合到一起。和groupbykey类似，任务的个数是可以通过第二个可选参数来配置的。
join(otherDataset, [numTasks]) :在类型为(K,V)和(K,W)类型的数据集上调用，返回一个(K,(V,W))对，每个key中的所有元素都在一起的数据集
groupWith(otherDataset, [numTasks]) : 在类型为(K,V)和(K,W)类型的数据集上调用，返回一个数据集，组成元素为(K, Seq[V], Seq[W]) Tuples。这个操作在其它框架，称为CoGroup
cartesian(otherDataset) : 笛卡尔积。但在数据集T和U上调用时，返回一个(T，U)对的数据集，所有元素交互进行笛卡尔积。
flatMap(func) :类似于map，但是每一个输入元素，会被映射为0到多个输出元素(因此，func函数的返回值是一个Seq，而不是单一元素)
Case 1将一个list乘方后输出
val input = sc.parallelize(List(1,2,3,4))
val result = input.map(x => x*x)
println(result.collect().mkString(","))
Case 2 wordcount
val textFile = sc.textFile(args(1))
val result = textFile.flatMap(line => line.split("\\s+")).map(word => (word, 1)).reduceByKey(_ + _)
println(result.collect().mkString(","))
result.saveAsTextFile(args(2))
Case 3 打印rdd的元素
rdd.foreach(println) 或者 rdd.map(println).
rdd.collect().foreach(println)
rdd.take(100).foreach(println)
spark SQL
Spark Streaming优劣
优势：
1、统一的开发接口
2、吞吐和容错
3、多种开发范式混用，Streaming + SQL, Streaming +MLlib
4、利用Spark内存pipeline计算
劣势：
微批处理模式，准实时
