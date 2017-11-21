### 匹配出student.txt文件中在score.txt文件对应的内容
* 在文件score.txt中存有如下数据：（姓名 分数）
```
lisi 88
bokeyuan 97
zhangsan 77
wangwu 89
hongliu 92
zhanghua 97
```
* 在文件student.txt中存有：
```
zhangsan
hongliu
```
#### 处理方法
* 第一种方法
```
awk  ' {if (ARGIND==1) grade[$1] = $0}  {if (ARGIND>1 && ($1 in grade)) print grade[$1]} ' score.txt student.txt
```
* 简化版：
`awk 'ARGIND==1 {grade[$1]=$0}  ARGIND>1 && ($1 in grade) {print grade[$1]}' score.txt student.txt`
* 分析：
    * ARGIND==1 处理第一个参数，即score.txt文件
    * {grade[$1]=$0} 以score.txt文件中的第一列为索引，将score.txt中的第一列内容存储在grade数据中
    * if (ARGIND>1 && ($1 in grade)) print grade[$1] 如果处理的是第二个及以后的文件，即student.txt.检查第一列(姓名)是否在grade数组中。如果在就打印以姓名为索引的grade的信息 
