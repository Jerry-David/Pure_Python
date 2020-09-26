# 字符串及其操作
> 在前面的笔记中，大家已经多次看见由两个引号包裹起来的内容，它叫做——字符串。


## 字符串的定义
所谓字符串，就是由两个引号包含的内容。注意：这个引号可以是单引号，也可以是双引号，但不能是中文中的引号。
比如：

`"Hello world!"`
这是一个字符串。

`"Hello world!"`
这也是一个字符串。

这种灵活性可以让你尽可能随意的定义字符串：
```
"This's a string."

'Jerry said: "This is a string too!"'
```

但这样是不行的：
```
'This isn't a string!'
"Jerry said: "This isn't a string!""
```
小思考：这个问题该怎么解决呢？


---


## 字符串使用：转义字符
转义字符是字符串里的一种特殊字符，它通常有着特殊含义。
```
\n 换行， \t 插入制表符（四个空格）， \" 在双引号中输出双引号， \' 在单引号中输出单引号（即上一章节问题答案）， \\ 在字符串中输出”\“
```
当然，如果你想在字符串中把它们看作普通字符，不让它们发挥转义字符的作用的话，你就可以在字符串前面加上一个`r`，这样无论你字符串里的转义字符是什么，Python都会看成普通文本。

例：
```python
print("Hello\n\tworld!\", \', \\")
print(r"Hello\n\tworld!\", \', \\")
```

输出：
```
Hello
        world!", ', \

Hello\n\tworld!\", \', \\
```

---


## 字符串使用：操作字符串
1. 更改大小写
  - title() `"hello world!".title()`， 将会以单词为单位，把每个单词都首字母大写。输出：`Hello World!`
  - upper() `"hello world!".upper()`，会把每个字符都大写。输出：`HELLO WORLD!`
  - lower() `"Hello wORld!".lower()`，会把每个字符都小写。输出：`hello world!`

2. 删除空格
  现在打开`python-shell`，运行以下代码
  - rstrip() `" python ".rstrip()`，将会删除字符串右边的空白。
  - lstrip() `" python ".lstrip()`，将会删除字符串左边的空白。
  - strip() `" python ".strip`，将会删除字符串中所有的空白。


---


## 字符串使用：合并拼接字符串
在大多数情况下，你会想拼接字符串。我们可以用`+`来实现这个操作

示例：
```python
print("Hello" + " " + "world" + "!")
```
输出：
```
Hello world!
```
