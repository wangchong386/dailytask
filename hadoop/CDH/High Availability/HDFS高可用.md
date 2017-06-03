## HDFS High Availability
> 背景：在标准配置中，NameNode是HDFS集群中的单点故障（SPOF）。 每个集群都有一个NameNode，如果该主机或进程变得不可用，则整个集群将不可用，直到NameNode重新启动或在新的主机上运行。 Secondary NameNode不提供故障切换功能。

### 标准方式主要通过两种方式降低HDFS的总可用性：
* 在诸如主机崩溃的计划外事件的情况下，集群不可用，直到操作员重新启动NameNode。
* NameNode机器上的计划维护事件（如软件或硬件升级）导致群集停机时间。

所以HDFS HA可以通过在一个集群中配置两个namenode来解决上述问题。分为活跃的namenode和备用的namenode,在这块可能有人提到secondary namenode也有相同的功能，但是备用namenode与它不同的是，备用NameNode是热备份，允许在主机崩溃的情况下快速自动故障切换到新的NameNode，或者为了进行计划维护而允许管理员启动的优化转换。 
### 实现
> CDH5支持基于Quorum-based Storage的存储作为唯一的HA实现
```
重要提示：在Cloudera Manager 5中，当您尝试使用NFS挂载的共享编辑目录升级为HA配置的CDH 4群集时：
1. 如果在升级之前不禁用HA配置，您的HA配置将继续工作; 但是您会看到一个警告，建议您切换到基于Quorum的存储。
2. 如果在升级之前禁用了HA配置，则无法使用NFS挂载的共享目录重新启用HA。 而是必须将HA配置为使用基于Quorum的存储
```
__重要提示__:需要具体了解如何自动故障切换可以访问以下地址：`https://www.cloudera.com/documentation/enterprise/5-5-x/topics/cdh_hag_hdfs_ha_intro.html`

