# 第一部分-基础篇


## 目录：
<!-- GFM-TOC -->
* [00 综](#00-综)
* [01 起步](#01-起步)
* [02 变量和简单数据类型](#02-变量和简单数据类型)
* [03 列表简介](#03-列表简介)
* [04 操作列表](#04-操作列表)
* [05 if语句](#05-if语句)
* [06 字典](#06-字典)
* [07 用户输入和while循环](#07-用户输入和while循环)
* [08 函数](#08-函数)
* [09 类](#09-类)
* [10 文件和异常](#10-文件和异常)
* [11 测试代码](#11-测试代码)
<!-- GFM-TOC -->


## 说明
- 笔记文件为.ipybn格式，内含全部代码及相应的笔记
- .ipynb文件若加载失败，可使用此链接打开 [https://nbviewer.jupyter.org/github/...]
  - 例如：https://nbviewer.jupyter.org/github/anliux/Python_Crash_Course/blob/master/src/PartI_Basics/A_Basics_Note.ipynb

# 00 综
- [《综》](https://github.com/anliux/Python-Crash-Course/blob/master/src/PartI_Basics/A_Basics_Note.ipynb)
- [备用链接](https://nbviewer.jupyter.org/github/anliux/Python-Crash-Course/blob/master/src/PartI_Basics/A_Basics_Note.ipynb)
- 各章汇总

<!-- GFM-TOC -->
- [返回目录](#目录)
<!-- GFM-TOC -->


# 01 起步
- [第1章笔记](https://github.com/anliux/Python-Crash-Course/blob/master/src/PartI_Basics/01-%E8%B5%B7%E6%AD%A5.ipynb)
- [第1章笔记-备用链接](https://nbviewer.jupyter.org/github/anliux/Python-Crash-Course/blob/master/src/PartI_Basics/01-%E8%B5%B7%E6%AD%A5.ipynb)
- 知识点：
  - 打印hello world：`print('要打印的内容')`
  - 注意点：单双引号均可，没有分号。
  - 打印的参数化：`print('min=%d' %min(digits))`
  - 换行：\n放在引号内打印 -- `print('\n')`
  - 制表符：\t放在引号内打印 -- `print('\t')`

<!-- GFM-TOC -->
- [返回目录](#目录)
<!-- GFM-TOC -->



# 02 变量和简单数据类型
- [第2章笔记](https://github.com/anliux/Python-Crash-Course/blob/master/src/PartI_Basics/02-%E5%8F%98%E9%87%8F%E5%92%8C%E7%AE%80%E5%8D%95%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B.ipynb)
- [第2章笔记-备用链接](https://nbviewer.jupyter.org/github/anliux/Python-Crash-Course/blob/master/src/PartI_Basics/02-%E5%8F%98%E9%87%8F%E5%92%8C%E7%AE%80%E5%8D%95%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B.ipynb)
- 知识点：
  - 汇总：
    - 认识变量、变量名规则、单双引号、字符串（大小写、拼接、空白）、数字（简单计算-除法、次方）、注释（单行多行）
  - python变量名：
    - 大写无妨，尽量用小写；
    - 字母数字下划线，数字不能开头，中间不能空格，并且慎用小写字母L和大写字母O(与数字0,1非常相似)
  - Python约定的文件名：
    - 使用小写字母和下划线
  - 引号：
    - 单引号双引号均可，灵活使用有助于撇号的使用，单双均可在外。
    - 单双引号的灵活使用：普通用单；双嵌套单，英语中常用的缩写一撇等等
  - 字符串：（大小写、拼接、空白）
    - 格式：`变量.方法名()`
    - title() - 改为首字母大写、其余小写
    - upper() - 改为所有字母大写
    - lower() - 改为所有字母小写
    - + ：拼接字符串
    - 制表符：\t
    - 换行： \n
    - strip() - 删除空白
    - rstrip() - 删除右边的空白
    - lstrip() - 删除左边的空白
  - 数字：（简单计算-除法、次方）
    - py3的float不能精确显示（例如：0.1 + 0.2=0.30000000000000004）
    - 整数相除，结果为float类型（Python2的整数相除为int型，同其他语言）
    - 两个星号 * ：乘方，相当于^
    - 用+号连接str和int时，将int转为str：当int x, str(x)后在加号连接
  - Python之禅
    - 美胜于丑。
    - 显式优于隐式。
    - 简单胜于复杂。
    - 复杂总比复杂好。
    - 平的比嵌套的好。
    - 稀疏胜于稠密。
    - 可读性计数。
    - 特殊情况不足以打破规则。
    - 尽管实用性胜过纯洁性。
    - 错误永远不会悄悄地过去。
    - 除非明确沉默。
    - 面对歧义，拒绝猜测的诱惑。
    - 应该有一种——最好只有一种——显而易见的方法来做到这一点。
    - 不过，如果不是荷兰语的话，这种方式一开始可能并不明显。
    - 现在总比没有好。
    - 虽然从来没有比现在更好。
    - 如果实现很难解释，那是个坏主意。
    - 如果实现很容易解释，这可能是一个好主意。
    - 名称空间是一个非常好的主意——让我们做更多的事情吧！

<!-- GFM-TOC -->
- [返回目录](#目录)
<!-- GFM-TOC -->



# 03 列表简介
- [第3章笔记](https://github.com/anliux/Python-Crash-Course/blob/master/src/PartI_Basics/03-%E5%88%97%E8%A1%A8%E7%AE%80%E4%BB%8B.ipynb)
- [第3章笔记-备用链接](https://nbviewer.jupyter.org/github/anliux/Python-Crash-Course/blob/master/src/PartI_Basics/03-%E5%88%97%E8%A1%A8%E7%AE%80%E4%BB%8B.ipynb)
- 知识点：
  - 汇总：列表的认识、创建、访问单个元素、修改、添加、删除、字母表排序、反转排序、求列表长度、索引注意事项
  - 认识列表：
    - 用方括号（[ ] ）来表示列表，并用逗号来分隔其中的元素，print时包括方括号、引号、逗号等
    - 由一系列按特定顺序排列的元素组成; 可以将任何东西加入列表中
  - 创建和访问列表：
    - 列表的格式：listname = [ , , , , ] --- 方括号，逗号隔开
    - 列表的访问：listname[n] -- 按索引n访问列表
    - 索引从0开始（同数组），负数表示倒数第几个
  - 修改、添加、删除列表元素
    - 修改：listname[n] = '新' -- 将索引n对应的元素换位'新'
    - 添加：listname.append('新') -- 将'新'添加到list的末尾
      - 动态地创建列表：先创建空列表，然后一系列append添加 -- listname=[] \\ listname.append('新') \\ listname.append('xxx')
      - 注：append不能连续使用，只能一个一个append，否则报错。
    - 插入：listname.insert(n, '新') -- 在listname的索引n处插入新元素'新'
    - 删除：del语句；pop()方法；remove()方法
      - pop有返回值，remove没有返回值
      - del listname[n]：知道要删除的元素在列表中的位置时使用。删除后无法再访问它。
      - a = listname.pop()：类似弹栈，弹出最后一个，并且返回该元素的值；弹出后仍能使用或访问这个值
      - a = listname.pop(n)：弹出索引n对应的元素；弹出后仍能使用
      - listname.remove('列表中某元素')：只知道要删除元素的值，不知道索引时；移除列表中某个值的第一个匹配项；没有返回值
  - 列表的各种排序
    - 各种方式的排序：sort(); sorted(); reverse()
    - listname.sort()：永久性排序，字母表顺序，a前z后，大写前小写后
    - listname.sort(reverse = True)：永久性排序，字母表逆序
    - sorted(listname)：临时性排序，字母表顺序，可赋值给变量后使用
    - sorted(listname, reverse = True)：临时性排序，字母表逆序
    - listname.reverse()：永久性修改，但随时可以恢复；倒着打印，注意是反转列表顺序，与字母表顺序无关
    - len(listname)：返回列表长度，可赋值给变量后使用
  - 索引：
    - 1、索引从0开始
    - 2、‘-1’在任何时候都可以用来指向最后一个元素，除非列表为空才报错
    - 3、发生索引错误却找不到解决方法时，可将列表或其长度打印出来，可以与自己以为的截然不同

<!-- GFM-TOC -->
- [返回目录](#目录)
<!-- GFM-TOC -->



# 04 操作列表
- [第4章笔记](https://nbviewer.jupyter.org/github/anliux/Python-Crash-Course/blob/master/src/PartI_Basics/03-%E5%88%97%E8%A1%A8%E7%AE%80%E4%BB%8B.ipynb)
- [第4章笔记-备用链接](https://nbviewer.jupyter.org/github/anliux/Python-Crash-Course/blob/master/src/PartI_Basics/04-%E6%93%8D%E4%BD%9C%E5%88%97%E8%A1%A8.ipynb)
- 知识点：
  - 汇总：
    - for循环、缩进注意点、数值列表创建、数学统计（最值、求和）、列表解析、列表切片、元组、代码格式优化
  - for循环遍历：
    - 刚开始使用循环时请牢记，对列表中的每个元素，都将执行循环指定的步骤，而不管列表包含多少个元素。
    - 如果列表包含一百万个元素，Python就重复执行指定的步骤一百万次，且通常速度非常快。
    - 格式：for n-任意名字 in listname: 某语句
    - 示例：`for magician in magicians:     print(magician)`
  - 避免缩进错误:
    - Python根据缩进来判断代码行与前一个代码行的关系
    - 常见错误：
      - 1-忘记缩进
      - 2-忘记缩进额外的代码行
      - 3-不必要的缩进
      - 4-循环后不必要的缩进
      - 5-遗漏冒号（python有冒号，无分号，用缩进代替大括号，注意别混淆了）
  - 数值列表：
    - range(start, stop, step)：创建一个整数列表，一般用在 for 循环中
      - 例如：`for value in range(1,5): #生成1-4`
    - range()：默认从0开始，默认step为1，这两个都可以省略(step优先省略)，stop必须有，不包括stop本值
    - list(range(n))：将range()的结果直接转换为列表，可存储在变量中以后使用
      - 例如：`numbers = list(range(1,6))`，打印numbers结果为：[1, 2, 3, 4, 5]
    - 用range()创建任意数据集：新建空列表--for循环-append
  - 数学统计：
    - min(listname)-最小值；
    - max(listname)-最大值；
    - sum(listname)-求和
  - 列表解析：
    - 将 for 循环和创建新元素的代码合并成一行，并自动附加新元素。
    - 创建列表： `listname = [value计算或表达式 for value in range(n)]`
    - 代码示例：`squares = [value**2 for value in range(1,11)]`，打印结果为：[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
  - 列表切片：
    - 切片：m n -- 索引值 
    - 端点值：左闭右开，从0开始，包含第一个索引值，不包含第二个索引值。
    - listname[m:n] -- 从索引值m处取到索引n的前一个元素（第m-1个到第n个）
    - listname[:n] -- 没有指定m时，默认从列表第一个元素开始
    - listname[m:] -- 没有指定n时，默认取到列表的最后一个元素
    - listname[-m:] -- m或n为负数时，从倒数第三位取到最后一个元素
    - listname[:] -- 取所有元素（是全新副本不是关联，相当于复制但区别于copy deepcopy等等）
      - 注：浅拷贝和深拷贝涉及到改变对本体的影响。
      - 参考：[Python-直接赋值、浅拷贝和深度拷贝解析](https://www.cnblogs.com/anliux/p/12834845.html)
  - 元组：
    - 列表：适合存储可能变化的数据集，使用方括号标识
      - 考点：列表不可作为字典的key，键要求唯一、不可变
    - 元组：不可变的列表称为元组，使用圆括号标识
      - 相比列表，元组是更简单的数据结构。如需存储的一组值在程序的整个生命周期内都不变，可使用元组
    - 格式：tuplename = ( , , , )
      - 索引值从0开始，由`变量名[index]`的格式获取
    - 不可以修改元组的值：tuplename[n] = m -- 会报错
    - 虽然不可以修改元组，但是可以对存储元组的变量重新赋值
      - dimensions = (200,50)
      - dimensions[0] = 400 # 报错
      - dimensions = (400,50) # 顺利改变dimensions的值
  - 格式设置指南：
    - Python改进提案 （Python Enhancement Proposal，PEP）
    - 缩进：4个空格为一级缩进
    - 行长：建议每行不超过80字符
    - 空行：python解释器不关心但影响可读性，尽量合理
    - 其他  
    
<!-- GFM-TOC -->
- [返回目录](#目录)
<!-- GFM-TOC -->



# 05 if语句
- [第5章笔记](https://github.com/anliux/Python-Crash-Course/blob/master/src/PartI_Basics/05-if%E8%AF%AD%E5%8F%A5.ipynb)
- [第5章笔记-备用链接](https://nbviewer.jupyter.org/github/anliux/Python-Crash-Course/blob/master/src/PartI_Basics/05-if%E8%AF%AD%E5%8F%A5.ipynb)
- 知识点：
  - 汇总：
    - if语句，if-else，if-elif，多个if，各种if嵌套，
    - 条件测试（布尔表达式），比较数值大小，多个条件（and，or），
    - 检测特定值是/不包含在列表中/列表是否为空/一个列表是否在另一个列表中，
    - if格式（空格增加可读性）
  - if语句格式：
    - `if xxx: xxx else: xxx`
    - 示例：` if car == 'bmw':    print(car.upper())`
  - 条件测试(布尔表达式)
    - 每条 if 语句的核心都是一个值为True 或False 的表达式，这种表达式被称为条件测试
    - if 条件测试(布尔表达式，就是一个为True 或者 False的表达式)
    - 数值大小比较：正常比较，如> >= < <=
      - 注：== 检查是否相等时考虑大小写，可以使用`变量名.lower()`等来消除大小写的影响。
    - 检查多个条件：and 或者 or组合，符合数学中的“与”和“或”的规则
    - 检查特定值是否包含在列表中: 'x' in list_name - 结果：True or False
    - 检查特定值是否不包含在列表中：关键字 not in - 'x' not in list_name - 结果：True or False，不包含时返回True
  - if语句结构：
    - if-else结构：非此即彼
    - if-elif-...-else结构: if嵌套
    - if... if... if...：测试多个条件，即不同于if-else语句，符合多个if条件时使用。
  - 使用if语句处理列表：
    - 检查特殊元素：for a in listname:  if a == 'sth':  (如果b列表中包含sth，就怎样)
    - 检查列表不是空的：if listname: ... 
    - 检查一个列表a是否在另一个列表b中：for a in a_list: if a in b_list: ..
  - 设置if语句的格式：
    - 在诸如== 、>= 和<= 等比较运算符两边各添加一个空格，例如，if age < 4: 要比if age<4: 好
  
<!-- GFM-TOC -->
- [返回目录](#目录)
<!-- GFM-TOC -->



# 06 字典
- [第6章笔记](https://github.com/anliux/Python-Crash-Course/blob/master/src/PartI_Basics/06-%E5%AD%97%E5%85%B8.ipynb)
- [第6章笔记-备用链接](https://nbviewer.jupyter.org/github/anliux/Python-Crash-Course/blob/master/src/PartI_Basics/06-%E5%AD%97%E5%85%B8.ipynb)
- 知识点：
  - 汇总：
    - 字典，键唯一值不要求，字典无序，访问，添加，修改，删除，语句过长拆分，for遍历的三种方法，字典和列表的各种相互嵌套
  - 一个简单的字典
    - 格式：dictname = {'键': '值', '键': '值', '键': '值', … '键': '值'}
    - 访问：dictname['键']，可赋值给变量存储后使用
    - 考点：
      - 键必须是唯一的，但值则不必。
      - 值可以取任何数据类型，但键必须是不可变的
      - 键：如字符串，数字或元组。
      - 值：可将python中任何对象用作字典中的值，比如数字、字符串、列表、字典等。
  - 使用字典：
    - 字典：‘键值对’，放在花括号里{}，每个键都与一个值相关联，可使用键来访问与之相关联的值。
    - 键-值：两个相关联的值，指定键时，返回与之相关联的值；键和值冒号分隔，键-值对之间逗号分隔。
    - 在一个字典中，键值对的数量没有限制
    - 访问字典中的值：dictname['键']，返回相关联的值
    - 字典是无序的，而列表是有序的（可通过索引0-n进行访问，添加也是append到末尾，insert到对应位置）
    - 添加键值对：dictname['键'] = '值'，然后就将这对键值对添加到字典中的任意位置了
      - 注：排列与添加顺序无关，字典是无序的
    - 创建空字典后添加：dictname = {} 然后 dictname['键'] = '值'....进行添加
    - 修改字典中的元素：dictname['键'] = '新值'
    - 删除字典中的元素：del dictname['键'] -- `del 字典名[键]`，就可以将该字典中的键值对删除
    - 过长的一行语句的拆分，如print(XXX ，+ \\ + 下一行四个空格+内容)
  - 遍历字典:
    - 遍历：for循环
      - 1-items()方法：所有键-值对
      - 2-keys()方法：所有键（可省略，加上使代码可读性更好）
      - 3-values()方法：所有值；
      - 4-set()函数：剔除重复元素
    - items() 方法：
      - 以列表形式返回可遍历的(键, 值) 元组数组（并非直接的列表，若要返回列表值还需调用list函数）
      - items() 方法返回值：dict_items([('last', 'fermi'), ... , ('username', 'efermi')]) -- 元组里的列表里的以键值对为单位的元组
      - items() + for循环：
        - 格式：for a, b in list.items():... 无论如何命名，a和b一前一后分别对应键和值
    - keys() 方法：
      - 返回字典中的键
      - keys() + for循环：
        - 格式：for a in dictname.keys(): ... 
          - 提取字典dictname中的所有键，并依次将其存储到变量a中；遍历字典默认遍历键，keys()可省略
        - 可在for循环中对返回的键进行排序。可使用函数sorted()来获取特定顺序排列的键列表的副本
          - 格式：`for name in sorted(favorite_languages.keys()): xxx`
    - values() 方法：
      - 返回一个值列表，不包含任何键。
      - values() + for循环：
        - 格式：for a in dictname.values(): ... for语句提取字典中的每个值，并将它们依次存储到变量a中。
        - 注：字典无序，因此返回的值无序。
    - set()方法：
      - (起因：键必须是唯一的，但值则不必。值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。)
      - 使用集合（set）可剔除重复项 - 类似于列表，但每个元素都是独一无二的
      - set()：对包含重复元素的列表调用set()，可找出列表中独一无二的元素，并使用这些元素创建一个集合
      - 格式：for a in set(dictname.values()): ...
      - 注：字典无序，因此返回的值无序。
  - 嵌套：
    - 将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套
    - 可以在列表中嵌套字典、在字典中嵌套列表、在字典中嵌套字典
    - 在列表中嵌套字典：
      - 格式：dict_1 = {} dict_2 = {} dict_3 = {} listname = [dict_1, dict_2, dict_3]
    - 在字典中嵌套列表：当需要在字典中将一个键关联到多个值时
      - 格式：dictname = {'键':'值', '键': [a, b, c, ... , m]} --- 例子中第二个键关联到a-m等多个值
      - 此时若用for循环遍历字典，需要两层for循环，因为键值对中的值有多个元素，因此需要for循环来遍历取出。
    - 在字典中嵌套字典：
      - 格式：dictname = { '键1': {字典1}, '键2': {字典2}, ... , '键n': {字典n} }

<!-- GFM-TOC -->
- [返回目录](#目录)
<!-- GFM-TOC -->



# 07 用户输入和while循环
- [第7章笔记](https://github.com/anliux/Python-Crash-Course/blob/master/src/PartI_Basics/07-%E7%94%A8%E6%88%B7%E8%BE%93%E5%85%A5%E5%92%8Cwhile%E5%BE%AA%E7%8E%AF.ipynb)
- [第7章笔记-备用链接](https://nbviewer.jupyter.org/github/anliux/Python-Crash-Course/blob/master/src/PartI_Basics/07-%E7%94%A8%E6%88%B7%E8%BE%93%E5%85%A5%E5%92%8Cwhile%E5%BE%AA%E7%8E%AF.ipynb)
- 知识点：
  - 汇总：
    - input()，求模运算%，
    - while循环，标志(封装的布尔表达式)，break退出循环，
    - while循环处理字典和列表（列表间移动元素、删除列表中多次出现的元素、input填充字典）
  - 函数input()的工作原理：
    - 让程序暂停运行，等待用户输入一些文本。获取用户输入后，将其存储在一个变量中。回车继续运行。
    - input(参数)：暂停程序，展示括号中的参数，等待用户输入，回车继续运行，并返回输入的值
      - 例如：`message = input('Tell me something, and I will repeat it back to you: ')`
    - input()：默认返回值是字符串，可用int()将str转为数值型，可将存储input返回值的变量放在int()中，或直接int(input())
  - 求模运算符：
    - % ：将两数相除并返回余数 
    - 格式：m % n
  - while循环概述：
    - for循环：用于针对集合中的每个元素都一个代码块
    - while循环：不断运行，直到指定的条件不满足为止
      - while循环格式：while 语句: xxx xxx .. xx(可内含多条语句)
    - 标志：定义一个变量，用于判断整个程序是否处于活动状态，这个变量称为‘标志’
      - 标志的好处：while只需检查标志一个条件，并将所有测试 (是否发生了应将标志设置为False的事件) 都放在其他地方，使程序更为整洁
      - 代码示例：`active = True \\ while active:  \\  message = input(prompt) \\  if message == 'quit': active = False`
    - break退出循环：立即退出循环，不再运行循环中余下的代码，也不管条件测试的结果如何
      - break循环：可以用在任何Python循环中，例如，退出遍历列表或字典的for循环
    - continue：
      - 在循环中使用continue：返回到循环开头，并根据条件测试结果决定是否继续执行循环
      - 场景：当符合某if条件时，直接结束本次循环并跳到下一次循环的判断阶段，即跳过continue后的语句。
  - 使用while循环来处理列表和字典：
    - 在列表之间移动元素： 
      - 示例：while list_1: a = list_1.pop() list_2.append(a) --- 可将list_1中的元素逐渐移动到list_2中
    - 删除一个列表中多次出现的元素：
      - 示例：while 'xx' in listname: listname.remove('xx')
      - 代码示例：`while 'cat' in pets: \\  pets.remove('cat')`
    - 使用用户输入填充字典：
      - 创建空字典 \\ 标志=True \\ while 标志: xx xxx xx input \\ if xx: 标志 = False

<!-- GFM-TOC -->
- [返回目录](#目录)
<!-- GFM-TOC -->



# 08 函数
- [第8章笔记](https://github.com/anliux/Python-Crash-Course/blob/master/src/PartI_Basics/08-%E5%87%BD%E6%95%B0.ipynb)
- [第8章笔记-备用链接](https://nbviewer.jupyter.org/github/anliux/Python-Crash-Course/blob/master/src/PartI_Basics/08-%E5%87%BD%E6%95%B0.ipynb)
- 知识点：
  - 汇总：
    - 函数定义，函数调用(位置实参，关键字实参)，形参默认值，等效的函数调用(多种方法)，避免实参错误(数量等)，
    - 返回值(封装功能、使用默认值来让调用实参可选、返回字典列表等对象，与while循环等结构结合)，
    - 传递列表(在函数中修改列表、切片获取列表副本以保留原列表)，
    - 传递任意数量实参(与位置实参、关键字实参结合、一个星号任意数量，两个星号空字典)，
    - 模块导入(导入整个模块、特定函数、as指定模块或函数名、导入模块中所有函数)，函数编写规则
  - 定义函数的格式：
    - def 函数名(参数，有无均可): xx xx ... xx
  - 传递实参：
    - 1-位置实参：要求实参的顺序与形参的顺序相同
    - 2-关键字实参：每个实参都由变量名和值组成
    - 其他：还可使用列表和字典等...
  - 主要针对调用函数时，实参的写法：
    - 位置实参：基于实参的顺序，根据位置对应函数定义中的各个形参
      - 代码示例：`describe_pet('hamster', 'harry')`
    - 关键字实参：传递给函数的名称-值对，直接在实参中将名称和值关联起来，因此不会混淆，无需考虑位置
      - 代码示例：`describe_pet(animal_type='hamster', pet_name='harry')`
  - 形参默认值：
    - 调用函数中提供实参时，使用指定实参值；否则，使用形参的默认值
    - 调用：可任选位置实参或关键字实参；形参默认值可简化函数的调用
    - 注意：若使用默认值，函数定义时，形参列表先列出没有默认值的，再列出有默认值的，以便正确地解读位置实参
      - 形参的顺序是先名字后类型，因此当只包含一个实参，依然会被视为位置实参；也可以使用关键字实参。
    - 代码示例：`def describe_pet(pet_name, animal_type='dog')`
  - 等效的函数调用：
    - 即：使用不同的传参方式，得到相同的结果。
    - 可混合使用位置实参、关键字实参、默认值等。
  - 避免实参错误：
    - 当提供的实参多于或少于函数完成其工作所需的信息时，将出现实参不匹配错误 - 会报错
    - 学会读错误提示，并从源程序中找出错误之处 
  - 返回值
    - 返回值的作用：将繁杂的工作封装到函数，从而简化主程序
    - 格式：a = xxxxxxxx return a
    - 使用默认值来让实参变成可选的，使函数调用时，只在必要时才提供额外的信息
      - 代码示例：`def get_formatted_name(first_name, last_name, middle_name=''): `
      - 针对有无中间名的情况，在函数中进行判定，`if middle_name: \\  full_name = .. \\ else ... `
      - 可选值让函数能够处理各种不同情形的同时，确保函数调用尽可能简单
    - 函数可返回任何类型的值，包括列表和字典等较复杂的数据结构
      - 格式：z = {} / [] / ... (任意类型，列表、字典等) return a
    - 可将函数同任何Python结构结合起来使用：while，if等等
      - 如下while嵌套if语句感觉很巧妙
      - 格式：while True: xxx if input = q break..... if input = q break..
  - 传递列表：
    - 可将列表等对象作为实参传递给函数
      - 向函数传递列表很有用，这种列表包含的可能是名字、数字或更复杂的对象（如字典）
    - 在函数中修改列表：
      - 比如把一个列表中的元素移动到另一个列表，并做一些其他修改，封装在函数中
      - 依然是pop()和append()
    - 禁止函数修改列表：
      - 思路--调用函数时，向函数传递列表的副本而不是原件，这样函数所做的任何修改都只影响副本，而可保留原件
    - 要将列表的副本传递给函数：
      - 切片法 -- 格式：function_name(list_name[:])
      - 代码示例：`print_models(unprinted_designs[:], completed_models)`
  - 传递任意数量实参：
    - 格式：形参写为"星号+参数名" 
      - 例如：`*paraname`，则不管调用语句提供多少实参，这个形参都将它们收入囊中
      - 代码示例：
        - `def make_pizza(*toppings): xxx`
        - `make_pizza('mushrooms','green peppers','extra cheese')`
    - 位置实参+任意数量实参：
      - 任意数量实参的形参放在最后：先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中
      - 代码示例：
        - `def make_pizza(size, *toppings):`
        - `make_pizza(12, 'mushrooms','green peppers','extra cheese')`
    - 任意数量的关键字实参：
      - 任意数量且预先不知道信息类型，将函数编写成能够接受任意数量的 '键-值' 对 - 调用语句提供了多少就接受多少
      - 格式：形参`**dictname` -- 两个星号创建一个空字典，并用for循环将 键值对 封装到这个字典中
      - 代码示例：
         - `def build_profile(first, last, **user_info):`
         - `user_profile = build_profile('albert', 'einstein',location='princeton', field='physics')`
  - 将函数存储在模块中：
    - 模块：将函数封装在独立的 `*.py` 文件中，使用时，import到主程序中。模块，即独立的py文件
    - 导入整个模块：
      - 导入格式：import modulename -- eg:`import pizza`
      - 调用格式：module_name.function_name()  -- eg:`pizza.make_pizza(16, 'pepperoni')`
    - 导入特定函数：
      - 导入格式：from module_name import function_name
      - 调用格式：function_name()
    - 导入任意数量的函数，逗号分隔函数名
      - 导入格式：from module_name import function_0, function_1, function_2
      - 调用格式：function_name()
    - 使用as给函数指定别名：
      - 导入格式：from module_name import function_name as fn
      - 调用格式：fn()
    - 使用as给模块指定别名：
      - 导入格式：import module_name as mn
      - 调用格式：mn.function_name()
    - 导入模块中的所有函数：
      - 导入格式：from module_name import *
      - 调用格式：function_name()
      - 如果模块中有函数的名称与你的项目中使用的名称相同，可能覆盖，而不是分别导入所有的函数 使用并非自己编写的大型模块时，最好不要采用这种导入方法： （此处只介绍方法，方便在阅读代码时知道在做什么，但自己写代码时不建议使用）
    - 小结：直接导入模块（py文件名）时，调用要写模块名；导入模块中的具体功能时，调用时直接使用功能名。
  - 函数编写指南：
    - 1-函数名：描述性，且只使用小写字母和下划线（模块名同）
    - 2-注释：紧跟在定义后，简要阐述功能，并采用文档字符串格式（三引号）
    - 3-形参指定默认值时，等号两边不要有空格
    - 4-函数调用中的关键字实参，等号使用同上一条
    - 5-每一行长度不超过79字符
      - 形参很多，导致函数定义长度超过时，在函数定义中输入左括号，回车，
      - 并在下一行按两次Tab键，将形参列表和只缩进一层的函数体区分开
    - 6-程序包含多个函数时，可使用两个空行将相邻的函数分开，这样更容易看清楚¶
    - 7-所有的import语句都应放在文件开头，唯一例外的情形是，在文件开头使用注释来描述整个程序时
    
<!-- GFM-TOC -->
- [返回目录](#目录)
<!-- GFM-TOC -->



# 09 类
- [第9章笔记](https://github.com/anliux/Python-Crash-Course/blob/master/src/PartI_Basics/09-%E7%B1%BB.ipynb)
- [第9章笔记-备用链接](https://nbviewer.jupyter.org/github/anliux/Python-Crash-Course/blob/master/src/PartI_Basics/09-%E7%B1%BB.ipynb)
- 知识点：
  - 汇总：
    - 类名首字母大写，方法(类中的函数)，init()，self，创建实例，命名规则，
    - 访问属性和调用方法(句点表示法)，创建多个实例，
    - 类中的每个属性都必须有初始值，有默认值的属性没有形参，修改属性的值的三种方法：实例修改；方法修改；方法递增，
    - 继承(super，super().__ init __(xx,xx)，子类的调用)，将实例作为类的属性及其调用，调用作为子类的属性之一的xx类的实例，
    - 导入类(一个模块中存储一个或多个类，导入单个类或多个类，导入整个模块，导入模块中的所有类，在一个模块中导入另一个模块类似嵌套)，
    - Python标准库，类编码风格
  - 创建和使用类：
    - 使用类几乎可以模拟任何东西，之后可用类来创建特定的实例
    - 命名规则：Python中首字母大写的名称是类
    - 方法：类中的函数。与上一章函数的区别是，调用的方式
    - init()：一个特殊的方法，每当根据类创建新实例时，都会自动运行，首尾各两个下划线，避免默认的方法与普通方法名称冲突
      - 格式示例：`def __init__(self, name, age): xxx \\ self.name = name  \\  self.age = age`
      - self：自动传递，因此只需要给除了self之外的其他形参提供值
      - init()下的self.xx为属性值的初始化
      - 以self为前缀的变量都可供类中的所有方法使用，还可通过类的任何实例来访问这些变量，像这样可通过实例访问的变量称为属性
  - 根据类创建实例：
    - 可将类视为有关如何创建实例的说明
      - `class Dog():  def __init__(self, name, age):`
      - `my_dog = Dog('willie', 6)`
    - 使用实参调用类中的方法init()，并未显式地return但默认返回一个实例，并存储在自定义的变量中
  - 命名规则：
    - 首字母大写（Dog）默认指类，小写默认指根据类创建的实例（my_dog）
  - 访问属性：
    - 句点表示法 eg：my_dog.name
  - 调用方法：
    - 句点表示法 eg：my_dog.sit()
  - 创建多个实例：
    - 每个实例都是独立的个体，拥有自己的一组属性，即使属性相同。
    - 可按需根据一个类创建任意数量的实例，条件是将每个实例都存储在不同的变量中，或占用列表或字典的不同位置
  - 使用类和实例
    - 类中的每个属性都必须有初始值，哪怕这个值是0或空字符
    - 有默认值的属性没有形参：如设置默认值，可在方法init()内指定这种初始值。并且在定义括号中无需包含为它提供初始值的形参
      - eg： 在init()中定义默认值 self.odometer_reading = 0，则def行无需包含odometer_reading这个形参
  - 修改属性的值：
    - 三种方法：直接通过实例修改；通过方法进行设置；通过方法进行递增（增加特定的值）
    - 法一：直接修改属性的值
      - 通过实例直接访问它，使用句点表示法直接访问并设置汽车的属性odometer_reading
      - eg：my_new_car.odometer_reading = 23
    - 法二：通过方法修改属性的值
      - 定义更新属性的方法，则无需直接访问属性，而将值传递给一个方法，由它在内部进行更新
      - eg：def update_odometer(self, mileage):xxxxx 调用：my_new_car.update_odometer(45)
    - 法三：通过方法对属性的值进行递增，与法二类似
      - eg：def increment_odometer(self,miles): self.odometer_reading += miles
      - """将里程表读数增加指定的量"""
      - 调用：my_used_car.increment_odometer(100) --- 将里程表数值在原有基础上增加100(100是实参)
  - 继承
    - 原有的类-父类；新类-子类
      - 子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法
    - 创建子类：
      - 创建子类时，父类必须包含在当前文件中，且位于子类前面
      - 创建子类的实例时，首先需要给父类的所有属性赋值
      - 定义子类时，必须在括号内指定父类的名称
        - 示例：`class ElectricCar(Car):`
      - super()：一个特殊函数，帮助将父类和子类关联起来。
        - 父类也称为超类（superclass），名称super由此得名
      - super(). __ init __ (xx, xx, xx) 
        - 这行代码位于子类的init()下，调用父类方法init()，xx是父类形参，让子类实例包含父类的所有属性
      - 在子类中除init外，可def子类特有的方法，也可以重写父类已有、但子类要求功能不同的方法(父类已有且相同的不再赘述)
        - 示例：`self.battery_size = 70` 功能重写略
    - 子类调用：
      - abc.function_name() -- 这个function可以是父类的，也可以是子类的
    - 将实例用作属性：
      - 将类的一部分作为一个独立的类提取出来
      - eg：battery属性功能很多，故独立放到另一个类Battery中，并将一个Battery实例用作ElectricCar类的一个属性(最后一句关键)
    - 将实例用作属性的定义类：
      - def Car() \\ def Battery() \\ def ElectricCar(Car) \\
      - 其中ElectricCar类中的init部分，除了继承父类的super().__init__(xx,xx,xx..)外，还要有一句：
        - self.battery = Battery()  -- 创建一个新的Battery实例，并存储在属性self.battery中
        - 此时，每当子类的__init__()方法被调用时，都将执行该操作。
        - 因此现在每个ElectricCar实例都包含一个自己创建的Battery实例
      - 调用作为子类的属性之一的Battery类的实例：
        - my_tesla.battery.describe_battery()，my_tesla存储实例
        - 这行代码在实例my_tesla中查找属性battery，并对储存在该属性中的Batter实例调用方法describe_battery()
        - battery在ElectricCar的init中初始化了
        - 故这里可以作为实例的一个属性使用，并且更深入地调用Battery中的功能describe_battery()
  - 导入类
    - Python允许你将类存储在模块中，然后在主程序中导入所需的模块
      - 注：第8章导入是将函数存储在模块中，from filename import xx_function，导入函数，而这里是import class
        - 设独立文件中的某模块：module_name.py ---- 内含多个类 Class_1, Class_2, .. , Class_n
    - 导入单个类：
      - from module_name import Class_1
      - 在一个模块中存储多个类，并导入其中一个：from module_name import Class_i
      - 从一个模块中导入多个类：from module_name import Class_1, Class_2, Class_n
      - 创建实例并调用：a = Class_i() \\ a.function_j().... 
      - 直接Class创建；直接function调用，不用带类名
    - 导入整个模块：import module_name
      - 创建实例并调用：a = module_name.Class_i() \\ a.function_i().... 
      - 创建声明模块名和类名；直接function调用，不用带类名
    - 导入模块中的所有类：from module_name import * (和所有函数的区别是什么..)
      - 不推荐星号import，如需从一个模块中导入很多类，最好导入整个模块，并使用 module_name.Class_name来访问类
    - 在一个模块中导入另一个模块：当有import关系的类分布在不同文件中时
      - 创建实例并调用：直接Class创建；直接function调用，不用带类名
      - module_1.py: Class_1  module_2.py: from module_1 import Class_1  Class_2
      - a = Class_1()    b = Class_2()    
      - a.function_1()    b.function_2()
    - 注：只有导入整个模块时需要在创建时声明模块名和类名，其他情况都是只声明类名；调用都是直接function调用，不用带类名
  - Python标准库
  - 类编码风格：
    - 你必须熟悉有些与类相关的编码风格问题，在你编写的程序较复杂时尤其如此。
    - 类名应采用驼峰命名法 ，即将类名中的每个单词的首字母都大写，而不使用下划线。
    - 实例名和模块名都采用小写格式，并在单词之间加上下划线。
    - 对于每个类，都应紧跟在类定义后面包含一个文档字符串。这种文档字符串简要地描述类的功能，并遵循编写函数的文档字符串时采用的格式约定。 每个模块也都应包含一个文档字符串，对其中的类可用于做什么进行描述。
    - 可使用空行来组织代码，但不要滥用。 在类中，可使用一个空行来分隔方法；而在模块中，可使用两个空行来分隔类。
    - 需要同时导入标准库中的模块和你编写的模块时，先编写导入标准库模块的import 语句，再添加一个空行，然后编写导入你自己编写的模块的import 语句。 在包含多条import 语句的程序中，这种做法让人更容易明白程序使用的各个模块都来自何方。
  
<!-- GFM-TOC -->
- [返回目录](#目录)
<!-- GFM-TOC -->



# 10 文件和异常
- [第10章笔记](https://github.com/anliux/Python-Crash-Course/blob/master/src/PartI_Basics/10-%E6%96%87%E4%BB%B6%E5%92%8C%E5%BC%82%E5%B8%B8.ipynb)
- [第10章笔记-备用链接](https://nbviewer.jupyter.org/github/anliux/Python-Crash-Course/blob/master/src/PartI_Basics/10-%E6%96%87%E4%BB%B6%E5%92%8C%E5%BC%82%E5%B8%B8.ipynb)
- 知识点：
  - 汇总：
    - open()打开文件并返回文件对象、绝对路径和相对路径、不同系统中路径的斜杠或反斜杠、
    - with关键字与close()、read()读取文件并返回字符串、strip()删除空格、逐行读取、readline()、readliens()、
    - 读取文本文件默认为字符串若需要数字需转换、open(filename,'w')、
    - 模式实参、写入模式注意覆盖、只能将字符串写入文本文件(必要时str转换)、写入多行(write()语句中添加换行、制表符、空格等)、
    - 附加模式'a'(不覆盖原有内容，将新写入添加到末尾)、指定文件名不存在时自动新建并写入、
    - try-except-else代码块(格式、功能等)、split()方法、pass语句(什么都不做语句)、
    - JSON文件的写入和读取(json.dump()和json.load())、及时考虑错误处理(读取文件时考虑FileNotFoundError等可能的错误)、
    - 代码重构
  - 从文件中读取数据的常用功能：
    - rstrip()方法：删除字符串末尾多余的空行（如10.1.1）
    - strip()方法：删除字符串两边的空格（如10.1.5）
    - readline()-读取每个字符； 
    - readlines()-读取每一行 ---- 一般用在for循环中（如10.1.4）
  - 读取整个文件：
    - 示例：`with open('pi_digits.txt') as file_object:`
      - 函数open()：传入要打开的文件的名称，返回一个‘表示文件的对象’，并存储在指定变量中(file_object)
      - open()之后Python会在当前执行的文件所在的目录找那个查找指定的文件
      - open()是默认打开当前文件夹下的文件，否则需要提供文件路径
    - 示例续：`contents = file_object.read()
      - 前面拿到文件对象后，这一步使用方法read()读取这个文件的全部内容，并将其作为一个‘长字符串’存储在变量中`
  - 不同系统中路径的斜杠和反斜杠：
    - Windows系统中，在文件路径中使用反斜杠（ \ ）而不是斜杠（ / ）
  - 当前文件夹下文件打开：
    - 格式：with open('filename.txt') as file_object:xxx
  - 非当前文件夹下文件打开：
    - 相对路径和绝对路径
  - 绝对路径和相对路径：
    - 绝对路径：程序在电脑中的完整路径那种路径
    - 相对路径：在当前py程序文件目录下有的文件夹路径，可以直接省略程序文件所在，直接写文件夹名字+文件名
  - 相对路径：省略程序所在路径的部分（绝对路径中前面的部分可以省略）
    - 格式：with open('text_files\filename.txt') as file_object:
    - 打开的是程序所在路径下的text_files的文件夹，名为filename.txt的文件时
  - 绝对路径：提供完整的路径。注意win系统中使用反斜杠，linux和OS X中使用斜杠
    - 格式：绝对路径内容太长可单独存放在变量中先。
    - 首先将路径单独存放在变量中：`file_path = '/home/ehmatthes/other_files/text_files/filename.txt' `
    - with打开文件时，将路径变量传入：`with open(file_path) as file_object: xxx`
  - 关键字with：在不再需要访问文件后将其关闭。
    - 若手动使用close()关闭，可能存在过早或过晚关闭文件导致的错误，用with结构则不存在这样的问题
  - 读取文件 
    - 格式：abc = file_object.read()
    - open拿到文件对象后，使用方法read()读取这个文件的全部内容，并作为一个‘长字符串’存储在变量abc中
    - rstrip()方法：删除字符串末尾多余的空行
    - strip()方法：删除字符串两边的空格(没记错的话应该是这样，lstrip()是删除左边的空格)
  - 逐行读取：for循环+line方法（rstrip配合食用）
    - 格式：for line in file_object: # file_object
    - 注：for line in listname: xxx -- 这里listname是按行的，for语句默认逐行读取了，略迷
  - 将读取到的各行存储在列表中：
    - with关键字：open()返回的文件对象只在with代码块内可用
    - 如想在with代码块外访问文件内容，可在with代码块内将文件的各行存储在一个列表中
    - 代码示例：
      - with open(filename) as file_object:
      - lines = file_object.readlines() # 读取每一行并存储在变量lines中作为一个列表
      - readline() - 读取单个字符，readlines() - 读取每一行
    - 注：读取文本文件时，将其中所有文本都默认为字符串。可按需使用int()或float()将其转换为数字
  - 生日在pi中小代码片段
  - 写入文件：write()方法：写入
    - 写入格式：with open(filename,'w') as file_object: file_object.write('xxxxx.')
      - open的第一个实参是要打开的文件的名称；第二个实参表示打开这个文件所用的模式
    - 模式实参：读取模式'r'，写入模式'w'，附加模式'a'，读取+写入模式'r+'
      - 省略了模式实参时，将以默认的只读模式打开文件
    - 当要写入的文件不存在时，函数open()将自动创建它
    - w模式要小心：如果指定文件已存在，在返回文件对象前清空（覆盖？？）该文件
    - 只能将字符串写入文本文件中。
    - 若要将数值数据存储到文本文件中，必须先使用str()将其转换为字符串
  - 写入多行：
    - write()不会在写入的文本末尾添加换行符，需要在语句中包含换行符、制表符、空格等
  - 附加到文件：
    - 用附加模式'a'打开文件：写入到文件的行都将添加到文件末尾。
    - 如果指定的文件不存在，将创建一个空文件
  - 异常
    - 异常概述：
      - 当发生让Python不知所措的错误时，它都会创建一个异常对象。
      - 如果你编写了处理该异常的代码，程序将继续运行。
      - 否则，程序将停止，并显示一个traceback，其中包含有关异常的报告
    - try-except-else代码块：
      - 出现异常，程序也将继续运行，并显示编写好的友好的错误信息。
      - try-except-else代码块：类似于if-else代码块，可帮助程序友好、安全地执行
        - 安全：将可能发生错误的除法部分放到try-except代码块中，防止恶意崩坏
      - 格式：try: xxx except xxxError: yyy else: zzz
        - 尝试执行xxx：如果xxx错误，则yyy；否则，zzz
      - try顺序执行：
        - 如果出现except错误，执行except语句；
        - 如果没有出现except错误，跳过except部分，继续执行(若有else，执行else语句)；
        - try必执行，except相当于if xx，else可省略
  - split()方法：根据一个字符串，按照空格创建一个单词列表
    - split()方法：将字符串按照空格划分，创建为单词列表(字符列表)(没有空格按一个单词创建)
    - 格式：a = strname.split() -- 根据strname中的字符串生成单词列表
  - 多个文件：def封装功能并配合for循环食用
  - pass语句：可在代码块中使用来让Python什么都不要做
    eg：except xxxError: pass
       则预设错误出现时，什么都不做，继续执行程序的其他部分
       凭借经验可判断该在程序的什么地方包含异常处理块，以及出现错误时该向用户提供多少相关的信息
  - 存储数据
    - JSON：一种在程序之间共享数据的简单方式
      - JSON(JavaScript Object Notation)格式最初是为JavaScript开发的，随后成了一种常见格式，被包括Python在内的众多语言采用。
      - 使用前需要导入json模块：import json
      - json的写入和读取：json.dump()--写入；json.load()--读取
      - 注：菜鸟教程里的是复数，括号里的参数也很多设置dumps，loads
    - 写入格式：
      - `with open(filename, 'w') as f_obj: # 以写入模式打开这个文件。若文件不存在，将新建这个文件`
      - `json.dump(listname, f_obj) # 使用函数json.dump()将列表listname存储到文件numbers.json中`
    - 读取格式：
      - `with open(filename) as f_obj:`
      - `a = json.load(f_obj) # 将读取到的json文件内容存储到变量a中`
    - open()--如果文件不存在，读取模式不会创建新文件会报错，写入模式会创建新文件
      - 为保护程序，需要将FileNotFoundError写入try-except代码块中
      - 具体：try-读取文件，except-FileNotFoundError：以写入模式读取。
  - 重构：
    - 多个功能时，可重构，将不同功能def封装到单个函数中

<!-- GFM-TOC -->
- [返回目录](#目录)
<!-- GFM-TOC -->



# 11 测试代码  
(注：各种报错，待整理)
- [第11章笔记]()

<!-- GFM-TOC -->
- [返回目录](#目录)
<!-- GFM-TOC -->



### END
