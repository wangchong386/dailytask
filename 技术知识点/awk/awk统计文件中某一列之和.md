### 使用awk统计文本文件中一列之和

* Unix / Linux 系统中，多用纯文本文件表示一些带格式的内容，比如就像数据库里面的一个 table 那样的格式。
* 这个时候，默认一行（以"\n"结束的一个字符串）为一条记录（一个 record ）， 一行中用特定的分隔符（默认是 "\t" ）分割的值为一个域（ field ）。
* awk 命令就是专门用来处理这样的文件的，它把文件中的每一个 record 作为一个独立的处理单元。
* 也就是说，你写 awk 脚本的时候，直接想象它处理的对象是一个 record 就对了。
* 并且，在 awk 里面，用$n （n=1,2,...,NF）表示该 record 中第 n 个 field 的值，其中NF是 record 中 field 的个数。

可以使用命令：
```
awk -F'\t' -v sum=0 '{sum += $1} END{print sum}' file_name
```
