# 设计并实现一个PL/0语言的词法分析器， 对读入的PL/0源程序，输出相应的Token二元式序列。
import re

"""建立单词符号与单词符号种别的对应关系"""

base_sym_dict = {
    'begin': 'beginsym',
    'const': 'constsym',
    'end': 'endsym',
    'odd': 'oddsym',
    'read': 'readsym',
    'var': 'varsym',
    'write': 'writesym',
    'call': 'callsym',
    'do': 'dosym',
    'if': 'ifsym',
    'proc': 'procsym',
    'then': 'thensym',
    'while': 'whilesym',
    '+': 'plus',
    '*': 'times',
    '(': 'lparen',
    '=': 'equal',
    '<': 'less_than',
    '>': 'greater_than',
    '<=': 'less_equal',
    '>=': 'greater_equal',
    '.': 'period',
    ';': 'semicolon',
    '-': 'minus',
    '/': 'divide',
    ')': 'rparen',
    ',': 'comma',
    '#': 'neq',
    ':=': 'becomes'
}
def seq_source_program(source_program: str) -> 'sym_list':
    """将输入的源程序转为符号列表"""
    # sym_list = source_program.split(' ')
    # 按 = 、:=、空格将源程序字符串分割，并保留这些分隔符
    sym_list = re.split('(=|:=|\+|-|\*|\/|<=|>=|<|>|\(|\)|\.|,|;|#|\s+)',soure_program.strip())
    # 去除分割结果中的空格
    sym_list = list(filter(lambda x : not str(x).isspace(),sym_list))
    return sym_list

def classify_token(sym_list: list) -> 'result_list':
    """生成二元组--token"""
    result_list = []
    for sym in sym_list:
        # 单词符号在基本符号表中
        if sym in base_sym_dict.keys():
            result_list.append((base_sym_dict[sym],))
        # 单词符号是数字
        elif str(sym).isdigit():
            result_list.append(('number',sym))
        # 单词符号是标识符
        else:
            if sym != '':
                result_list.append(('ident',sym))
    return result_list

# 测试代码
soure_program = input('请输入您的源代码：')
sym_list = seq_source_program(soure_program)
result_list = classify_token(sym_list)
print('该词法分析程序的输出如下：')
for token in result_list:
    print(token)



