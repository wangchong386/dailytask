# 向新集群中添加数据节点（Cloudera Manager）
## 操作步骤：
一、修改 hostname
1.修改新节点的 /etc/sysconfig/network 配置文件，按照集群节点命名规范更新HOSTNAME：

系统默认的：（将localhost按照需要的命名规则进行修改）

```

NETWORKING=yes

HOSTNAME=localhost.localdomain

```
2. 重启节点使HOSTNAME生效

```
[root@localhost ~]# reboot
Broadcast message from root@localhost.localdomain
        (/dev/pts/0) at 11:53 ...
The system is going down for reboot NOW!

```
3.更新/etc/hosts 文件
增加新节点的ip和hostname映射，并用namenode的hosts文件覆盖新节点和已有节点，保持整个集群hosts文件同步
（__目前该操作暂时手工完成__）
```
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
```
