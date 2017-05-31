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