# Variable

> 变量是用户自定义的一个值，你可以用它来做任何事情。


---


## 一些需要记住的单词
| words     | means  |
|-----------|--------|
| define    | 定义   |
| invalid   | 无效的 |
| directory | 文件夹 |
| file      | 文件   |


---


## 了解Python的宗旨
你可以在Python shell中(通过在终端输入 `python` 来打开它)输入 `import this` 来查看它。
下面是译文：
```
Tim Peters Beautiful撰写的Python宗旨
美丽胜过丑陋。
显式胜于隐式。
简单胜于复杂。
复杂胜于复杂。
扁平比嵌套更好。
稀疏胜于密集。
可读性很重要。
特殊情况不足以违反规则。
实用性胜过形式，但我们要把这两样的都做的很好。
错误绝不能忽视。
面对模棱两可的想法，我们要选择较完美的。
应该有一种-最好只有一种-显而易见的方法。
有总比没有好。
如果你实现的结果难以解释，那是个坏主意。
如果你实现的结果易于解释，则可能是个好主意。
遵守命名规则是一个很棒的主意-让我们做更多这些吧！
```
你不需要全部理解它们，但试着去理解，去执行是个好主意。


---


## Python代码执行顺序
从左到右，从上到下


---


## 命名规则
> 官方建议给文件命名时，应只有小写字母，数字和下划线（代替空格），且不能以数字开头。给变量命名时也是如此，要尽量做到“见名知意”。这是`pep8`规范，你可以去了解一下，它是什么，因为以后你会经常听到这个词。


---


## 给变量赋值及变量的应用
我们用`=`给变量赋值。
举个栗子：

新建一个叫 `variable.py` （注意，不要遗漏`.py`，它是Python文件的后缀，能告诉Python解释器怎么运行它），键入以下内容：
```python
message = "你好，世界！"
```

我们还可以把它重定义会添加，如：
```python
message = "Hello world!"
message = message + "你好，世界！"
```
现在，message的值就是
```
Hello world!
你好，世界！
```

Now，你的文件里就会有一个叫 `message` 的东西啦！你甚至可以打印它:
```python
print(message)
```

这个时候运行此文件：`python variable.py`（详情参见[Python教程第一期——Hello world!](https://blog.csdn.net/Jerry_David/article/details/108218070)） ，你将看到这样的输出：
```
Hello world!
你好，世界！
```
当然，你也可能看到这个错误：
```
Traceback (most recent call last):
  File "variable.py", line 2, in <module>
    print(mesage)
NameError: name 'mesage' is not defined
```
这是因为你的变量名写错了，仔细检查一下你的代码，把它改正吧！


---


## 小练习
> 合理的运用变量，让程序输出
> ```
> 我开始学Python啦！
> 它非常有趣！
> ```
