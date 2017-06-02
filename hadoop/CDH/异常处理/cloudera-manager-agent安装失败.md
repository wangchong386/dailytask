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
> 1.安装httpd2.2.15版本
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
> 2.查看是否已经安装

```
[root@hostname ~]# yum list httpd
Loaded plugins: fastestmirror
Repository base_source is listed more than once in the configuration
Repository epel_server is listed more than once in the configuration
Repository updates_source is listed more than once in the configuration
Repository extra_source is listed more than once in the configuration
Loading mirror speeds from cached hostfile
Installed Packages
httpd.x86_64                                                                  2.2.15-39.el6.centos                                                                   @base_source
Available Packages
httpd.x86_64                                                                  2.2.21-1                                                                               extra_source
```
> 3.如果安装httpd的话，显示已经安装
```
[root@localhost ~]# yum install httpd-2.2.15-39.el6.centos
Loaded plugins: fastestmirror
Setting up Install Process
Repository base_source is listed more than once in the configuration
Repository epel_server is listed more than once in the configuration
Repository updates_source is listed more than once in the configuration
Repository extra_source is listed more than once in the configuration
Loading mirror speeds from cached hostfile
Package matching httpd-2.2.15-39.el6.centos.x86_64 already installed. Checking for update.
Nothing to do

``` 
 
可以通过命令将httpd程序删除之后，重新安装
`yum remove httpd-2.2.21-1.x86_64`
然后在进行安装就可以：
`yum install httpd-2.2.15-39.el6.centos.x86_64`

#### (2) __glibc-common版本不匹配__
##### 首先可以看下glibc是什么以及它的重要性：
> glibc是GNU发布的libc库，即c运行库。glibc是linux系统中最底层的api，几乎其它任何运行库都会依赖于glibc。glibc除了封装linux操作系统所提供的系统服务外，它本身也提供了许多其它一些必要功能服务的实现。由于 glibc 囊括了几乎所有的 UNIX 通行的标准，可以想见其内容包罗万象。而就像其他的 UNIX 系统一样，其内含的档案群分散于系统的树状目录结构中，像一个支架一般撑起整个操作系统。在 GNU/Linux 系统中，其C函式库发展史点出了GNU/Linux 演进的几个重要里程碑，用 glibc 作为系统的C函式库，是GNU/Linux演进的一个重要里程碑。
```
Error: Package: glibc-2.12-1.149.el6_6.7.i686 (updates_source)
           Requires: glibc-common = 2.12-1.149.el6_6.7
           Installed: glibc-common-2.12-1.192.el6.x86_64 (@anaconda-CentOS-201605220104.x86_64/6.8)
               glibc-common = 2.12-1.192.el6
           Available: glibc-common-2.12-1.149.el6.x86_64 (base_source)
               glibc-common = 2.12-1.149.el6
           Available: glibc-common-2.12-1.149.el6_6.4.x86_64 (updates_source)
               glibc-common = 2.12-1.149.el6_6.4
           Available: glibc-common-2.12-1.149.el6_6.5.x86_64 (updates_source)
               glibc-common = 2.12-1.149.el6_6.5
           Available: glibc-common-2.12-1.149.el6_6.7.x86_64 (updates_source)
               glibc-common = 2.12-1.149.el6_6.7
 You could try using --skip-broken to work around the problem
 You could try running: rpm -Va --nofiles --nodigest

```