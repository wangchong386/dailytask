## Spark基础知识解答
### 一. Spark基础知识
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
