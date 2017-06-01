## CDH安装过程中异常处理
### 1. 安装Cloudera Manager agent及相关组件过程中,安装cloudera-manager-agent失败
![](images/addhosterror1.png)
#### (1) __httpd版本不匹配__
![](images/addhosterror2.png)
从打印出的错误日志可以看出：

需要Available: httpd-2.2.15-39.el6.centos.x86_64 (base_source)版本，

但是系统安装的是：Installed: httpd-2.2.21-1.x86_64 (@extra_source) 

在机器该节点也可以看到：
···
[root@hostname ~]# yum list httpd
Loaded plugins: fastestmirror
Repository base_source is listed more than once in the configuration
Repository epel_server is listed more than once in the configuration
Repository updates_source is listed more than once in the configuration
Repository extra_source is listed more than once in the configuration
Loading mirror speeds from cached hostfile
Available Packages
httpd.x86_64                                                                        2.2.21-1                                                                         extra_source
···
