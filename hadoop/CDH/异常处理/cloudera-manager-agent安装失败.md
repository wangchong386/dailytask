## CDH安装过程中异常处理
### 1. 安装Cloudera Manager agent及相关组件过程中,安装cloudera-manager-agent失败
![](images/addhosterror1.png)
#### (1) __httpd版本不匹配__
![](images/addhosterror2.png)
从打印出的错误日志可以看出：

需要Available: httpd-2.2.15-39.el6.centos.x86_64 (base_source)版本，

但是系统安装的是：Installed: httpd-2.2.21-1.x86_64 (@extra_source) 

在机器该节点也可以看到：
```
[root@hostname ~]# yum list httpd
Loaded plugins: fastestmirror
Repository base_source is listed more than once in the configuration
Repository epel_server is listed more than once in the configuration
Repository updates_source is listed more than once in the configuration
Repository extra_source is listed more than once in the configuration
Loading mirror speeds from cached hostfile
Available Packages
httpd.x86_64                                                                        2.2.21-1                                                                         extra_source
```

* 解决措施：
```
[root@hostname ~]# yum install httpd-2.2.15-39.el6.centos.x86_64
Loaded plugins: fastestmirror
Setting up Install Process
Repository base_source is listed more than once in the configuration
Repository epel_server is listed more than once in the configuration
Repository updates_source is listed more than once in the configuration
Repository extra_source is listed more than once in the configuration
Loading mirror speeds from cached hostfile
Resolving Dependencies
--> Running transaction check
---> Package httpd.x86_64 0:2.2.15-39.el6.centos will be installed
--> Processing Dependency: httpd-tools = 2.2.15-39.el6.centos for package: httpd-2.2.15-39.el6.centos.x86_64
--> Processing Dependency: apr-util-ldap for package: httpd-2.2.15-39.el6.centos.x86_64
--> Processing Dependency: /etc/mime.types for package: httpd-2.2.15-39.el6.centos.x86_64
--> Running transaction check
---> Package apr-util-ldap.x86_64 0:1.3.9-3.el6_0.1 will be installed
--> Processing Dependency: apr-util = 1.3.9-3.el6_0.1 for package: apr-util-ldap-1.3.9-3.el6_0.1.x86_64
---> Package httpd-tools.x86_64 0:2.2.15-39.el6.centos will be installed
---> Package mailcap.noarch 0:2.1.31-2.el6 will be installed
--> Running transaction check
---> Package apr-util.x86_64 0:1.3.9-3.el6_0.1 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

=================================================================================================================================================================================
 Package                                    Arch                                Version                                           Repository                                Size
=================================================================================================================================================================================
Installing:
 httpd                                      x86_64                              2.2.15-39.el6.centos                              base_source                              825 k
Installing for dependencies:
 apr-util                                   x86_64                              1.3.9-3.el6_0.1                                   base_source                               87 k
 apr-util-ldap                              x86_64                              1.3.9-3.el6_0.1                                   base_source                               15 k
 httpd-tools                                x86_64                              2.2.15-39.el6.centos                              base_source                               75 k
 mailcap                                    noarch                              2.1.31-2.el6                                      base_source                               27 k

```