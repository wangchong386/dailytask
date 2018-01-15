### 字符编码
背景：字符串和编码

* 因为计算机只能处理数字，如果要处理文本，就必须先把文本转换为数字才能处理。最早的计算机在设计时采用8个比特（bit）作为一个字节（byte），所以，一个字节能表示的最大的整数就是255（二进制11111111=十进制255），如果要表示更大的整数，就必须用更多的字节。比如两个字节可以表示的最大整数是65535，4个字节可以表示的最大整数是4294967295。

* 由于计算机是美国人发明的，因此，最早只有127个字符被编码到计算机里，也就是大小写英文字母、数字和一些符号，这个编码表被称为ASCII编码，比如大写字母A的编码是65，小写字母z的编码是122。

* 但是要处理中文显然一个字节是不够的，至少需要两个字节，而且还不能和ASCII编码冲突，所以，中国制定了GB2312编码，用来把中文编进去。

* 你可以想得到的是，全世界有上百种语言，日本把日文编到Shift_JIS里，韩国把韩文编到Euc-kr里，各国有各国的标准，就会不可避免地出现冲突，结果就是，在多语言混合的文本中，显示出来会有乱码。
* 所以Unicode应运而生。Unicode把所有语言都统一到一套编码里，这样就不会再有乱码问题了。

## 格式化
* 在Python中，采用的格式化方式和C语言是一致的，用__%__实现，举例如下：
```
>>> 'Hello, %s' % 'world'
'Hello, world'
>>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
'Hi, Michael, you have $1000000.'
```
* 常见的占位符有：

占位符|替换内容
---|---
%d|整数
%f|浮点数
%s|字符串
%x|十六进制整数

### list
Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
```
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print (classmates[1])
>>>['Michael', 'Bob', 'Tracy']
3
Bob
```
当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1。

如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
```
>>> classmates[-1]
'Tracy'
```
* list是一个可变的有序表，所以，可以往list中追加元素到末尾：
```
print(classmates.append('Adam'))
print(classmates)
>>>
['Michael', 'Bob', 'Tracy', 'Adam']
```
* 也可以把元素插入到指定的位置，比如索引号为__1__的位置：
```
>>> classmates.insert(1, 'Jack')
>>> classmates
['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
```
* 删除list末尾的元素
```
>>> classmates.pop()
'Adam'
>>> classmates
['Michael', 'Jack', 'Bob', 'Tracy']
```
* 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
```
>>> classmates.pop(2)
'Bob'
```
* 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：

```
>>> classmates[1] = 'Sarah'
>>> print(classmates)
['Michael', 'Sarah', 'Tracy']
```
* list元素也可以是另一个list，比如：
```
>>> s = ['python', 'java', ['asp', 'php'], 'scheme']
>>> len(s)
4
```

### tuple
* 另一种有序列表叫元组：tuple. tuple和list非常类似，但是tuple一旦初始化就不能修改
* 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来

