## AWK
To become an expert AWK programmer,you need to know its internals.AWK follows a simple workflow
* Read

* Execute

* Repeat

```
awk '{pattern + action}' {filenames}
```

语法总是这样，其中 pattern 表示 AWK 在数据中查找的内容，而 action 是在找到匹配内容时所执行的一系列命令。

(1) awk+action的示例，每行都会执行action{print $1}.  -F指定域分隔符
* 如果只是显示/etc/passwd的账户
```
#cat /etc/passwd |awk  -F ':'  '{print $1}'  
root
daemon
bin
sys
```

-- 按照-F指定域分隔符为':'进行分割
* 只是显示/etc/passwd的账户和账户对应的shell,而账户与shell之间以逗号分割,而且在所有行添加列名name,shell,在最后一行添加"blue,/bin/nosh"

-- 这个是很使用，相当于给文件没一列进行起别名
```
cat /etc/passwd |awk  -F ':'  'BEGIN {print "name,shell"}  {print $1","$7} END {print "blue,/bin/nosh"}'
name,shell
root,/bin/bash
daemon,/bin/sh
bin,/bin/sh
sys,/bin/sh
....
blue,/bin/nosh
```
