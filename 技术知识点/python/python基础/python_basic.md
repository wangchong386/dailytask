## python的编译过程
* 当用户键入代码交给Python处理的时候会先进行词法分析，例如用户键入关键字或者当输入关键字有误时，都会被词法分析所触发，不正确的代码将不会被执行
* 下一步Python会进行语法分析，例如当"for i in test:"中，test后面的冒号如果被写为其他符号，代码依旧不会被执行。
* 最关键的过程，在执行Python前，Python会生成.pyc文件，这个文件就是字节码，如果我们不小心修改了字节码，Python下次重新编译该程序时会和其上次生成的字节码文件进行比较，如果不匹配则会将被修改过的字节码文件进行覆盖，以确保每次编译后字节码的准确性。
* 那么什么是字节码？字节码在Python虚拟机程序里对应的是PyCodeObject对象。.pyc文件是字节码在磁盘上的表现形式。简单来说就是在编译代码的过程中，首先会将代码中的函数、类等对象分类处理，然后生成字节码文件。有了字节码文件，CPU可以直接识别字节码文件进行处理，接着Python就可执行了。

python核心（编译器）

   词法分析 --> 语法分析 --> 编译 --> 执行


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

### 条件判断
```
age = 20
if age >= 18:
    print('your age is',age)
    print('adult')
>>> ('your age is', 20)
adult
```
* 根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做。
```
Python语言是一款对缩进非常敏感的语言，给很多初学者带来了困惑，即便是很有经验的Python程序员，也可能陷入陷阱当中。最常见的情况是tab和空格的混用会导致错误，或者缩进不对，而这是用肉眼无法分别的。

在编译时会出现这样的错IndentationError:expected an indented block说明此处需要缩进，你只要在出现错误的那一行，按空格或Tab（但不能混用）键缩进就行。

往往有的人会疑问：我根本就没缩进怎么还是错，不对，该缩进的地方就要缩进，不缩进反而会出错，，比如：

if xxxxxx：

（空格）xxxxx

或者

def xxxxxx：

（空格）xxxxx

还有

for xxxxxx：

（空格）xxxxx

一句话 有冒号的下一行往往要缩进，该缩进就缩进
```

* 也可以给if添加一个else语句，意思是，如果if判断是False，不要执行if的内容，去把else执行了：
```
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')
```
* 注意不要少写了冒号`:`。
* elif是else if的缩写，完全可以有多个elif，所以if语句的完整形式就是：
```
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
```
* `if`语句执行有个特点，它是从上往下判断，如果在某个判断上是`True`，把该判断对应的语句执行后，就忽略掉剩下的`elif`和`else`
* `if`判断条件还可以简写，比如写：
```
if x:
    print('True')
```
* 只要`x`是非零数值、非空字符串、非空`list`等，就判断为`True`，否则为`False`。

### 再议 input
* 最后看一个有问题的条件判断。很多同学会用`input()`读取用户的输入，这样可以自己输入，程序运行得更有意思：
```
birth = input('birth: ')
if birth < 2000:
    print('00前')
else:
    print('00后')
```
## 循环
* Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来，看例子：
```
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
>>> Michael
Bob
Tracy
```
* 如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：
```
>>> list(range(5))
[0, 1, 2, 3, 4]
```
* 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现:
```
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
```
* 在循环内部变量n不断自减，直到变为-1时，不再满足while条件，循环退出

#### break
* 在循环中，break语句可以提前退出循环
```
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')
```
#### continue
* 在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环
