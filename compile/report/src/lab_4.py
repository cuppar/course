# 对PL/0，编写调试一个语法分析程序。
# 注意：1. 可选择任何一种语法分析方法（递归下降、LL（1）、算符优先、SLR（1）等）；
# 2. 对所用分析方法，选择一种合适的数据结构；
# 3. 用合适的结构存放分析出的正确的语法单位并输出；
# 4. 也可以用YACC来实现。

# 1.根据PL/0对应的文法构造出递归下降子程序
# 2.根据算递归下降子程序判断输入的程序段是否合乎语法
# 3.存储判断结果以及分析出的正确的语法单位

def seg_program(program: str) -> 'program_list':
    """将源程序分割为语句列表"""
    pass

def begin_stat(stat: str) -> None:
    """定义关键字begin的递归下降子程序"""
    pass

def if_stat(stat: str) -> None:
    """定义if关键字的递归下降子程序"""
    pass

def becomes_stat(stat: str) -> None:
    """定义赋值表达式的递归下降子程序"""
    pass

def relation_stat(stat: str) -> None:
    """定义关系表达式的递归下降子程序"""
    pass

def while_stat(stat: str) -> None:
    """定义当型循环的递归下降子程序"""
    pass

while True:
    """总控部分"""
    pass