# Hello Python!


## 简介
> [Python简介](http://c.biancheng.net/view/2165.html)

### 解释型与编译型
- 解释型
  > 解释型指的是每当运行，就把编程语言转换成机器语言，执行一次翻译一次，这使得解释型语言运行不够快速，但可以跨平台。
- 编译型
  > 编译型与解释型正好相反，编译型是完成编写后，直接翻译成机器语言，保存在一个文件中，每当要运行程序时就执行含有机器语言的文件。


---


## 环境搭建

#### ~~自求多福~~

Windows参考官网：[Windows下Python安装](http://c.biancheng.net/view/4161.html)

Mac os 使用brew安装：`brew install python` 或参考 [Mac下Python安装](http://c.biancheng.net/view/4164.html)

Linux 安装方式自行百度（因为不同发行版差距较大，需要自行匹配），推荐[Linux下Python安装](http://c.biancheng.net/view/4162.html)

IDE选择：[Python IDE选择](https://zhuanlan.zhihu.com/p/96778253)，我个人用的是Vim，贴张图：
![avatar](/home/jerry/Pictures/markdown/实例.png)


---


## 一些需要记住的单词

| word   | mean |
|--------|------|
| print  | 打印 |
| syntax | 语法 |
| error  | 错误 |


---


## 我的第一行代码
新创建一个文件` hello_world.py `，在其中输入以下代码：
```python
print("Hello world!")
```
现在，保存退出，回到终端，输入` python hello_world.py `并回车，你会看到这样的输出：
```
Hello world!
```
当然，你也有可能看到这样的输出:
```
  File "hello_world.py", line 1
    print（“Hello world!”）
               ^
SyntaxError: invalid character in identifier
```
这是因为你使用的是中文输入法打的标点符号，Python不是中国开发的语言，自然不会允许中文标点的存在。如果你看到这个错误，请把这行代码删除，用英文输入法重新打一遍。


#### 分析
现在，让我们逐行来分析代码与错误：
- `print("Hello world!") `让我们从控制台（终端）输出 `Hello world! `。print是一个函数，你可以把它看成一个盒子，里面有三样要重要的东西：
  - `value` 这个最重要，我们能让 `print`（打印） 把它输出在终端，注意，它可以有多个
  - `sep` 间隔，即连接几个 `value` 之的东西， 默认是空格
  - `end` 结尾，即你想在打印完 `value` 后再打印的东西，默认是回车

    示例：
    ```python
    print("Hello",'world' sep=', ', end='!')
    ```
    它将输出：
    ```
    Hello, world!
    ```
- `python hello_world.py` 这句话是让你运行 `hello_world.py` 。运行的格式是这样的 `python filename(你要运行的文件名)`
- 当你的程序出现错误时，Python会尽力去帮你找出错误，比如看：
  - `File "hello_world.py", line 1`， 意思是说在文件`hello_world.py`中，第一行有错误。
  - `print（“Hello world!”）`，是说你这句代码有错误。
  - `SyntaxError: invalid character in identifier`，意思是`语法错误：无法标识的字符。`，现在再看一看你的代码，是不是能找出错误了呢？


---


## 小练习
> 让你的程序输出`你好！！！世界！！！`，要求使用`sep`, `end`。祝你好运！
