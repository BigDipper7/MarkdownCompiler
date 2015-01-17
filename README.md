# MarkdownCompiler
编译原理项目

组员信息
1252937 许铭淏
1253030 姚鹏飞

# 1.项目说明

## 项目基本功能

本项目主要实现了 markdown 的解析，能够正确解析的 markdown 语法最要有：

* 标题 h1 到 h3（随意扩充）
* test01的功能
* test02的功能
* test03 代码高亮


## 扩展功能

同时，我们还实现了一些 markdown 本身不具备的功能：

### 代码着色

主要使用了一个网上通用的代码高亮库syntaxhighlighter_3.0.83，在解析出代码的时候对代码进行着色处理。。。。

* 使用的库链接：https://github.com/syntaxhighlighter/syntaxhighlighter
* 很好用 但是限制在于 一 只能是html 二 是对于不同的language要引入不同的js，比较繁琐，前端还是比较好改的 但是我们手动写的时候比较的恶心 所以最后决定只要加上一个JS语法解析

测试文件和测试方法

```
测试文件位于项目目录xxx下
测试：
python run.py <filename.md>
```

## 项目特别说明

这个程序的基础是一个body标签内的statement，这个statement由若干个expression规约而成，expression间的分割符是CR，也就是‘\n+’，即每个expression都是用换行符分开的语法单位，一个expression可以是用p标签包裹起来的文本段，也可以是h1到h6不等的大小标题，还可以是一条分割线或是有序列表或无序列表，一个expression内可以包括很多不同的部分，尤其是phrase，phrase是一个由单词（factor）和各种特殊符号组成的串，在这一层级可以实现对文本的加粗，强调，代码段操作，链接等。

# 2.组队信息


## 小组成员贡献说明

### 姚鹏飞 1253030 <ypfyhs>
主要工作：test01 test02。。。

贡献率： 50%

### 许铭淏 1252937 <BigBigDipper7>
主要工作：test01 test03

贡献率： 50%
