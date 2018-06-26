# 编写一个程序，用于判定给定的文法是否为算符优先文法。
# 注意：1．文法的机内表示；
# 2. FIRSTVT集和LASTVT集的计算；
# 3. 算符优先关系矩阵的构造。

# 1.将文本字符串转为文法的机内表示
# 2.FIRSTVT集和LASTVT集的计算；
# 3.计算终极符之间的关系
# 4.判定是否为算符优先矩阵
# 5. 构造算符优先关系矩阵

# 测试数据：
#S->a
# S->^
# S->(T)
# T->T,S
# T->S
# P->#S#

# E->E+E
# E->E*E
# E->(E)
# E->i

import sys
import re
from numpy.core.defchararray import isupper, islower


def make_gram() -> 'gene_list':
    """将输入的文法表示为计算机中的字典列表--产生式[('A','abc')]"""
    gene_list = []
    print('合法产生式的格式：A->c')
    print('请输入合法的文法的产生式（换行后，ctrl+d即可结束输入）：')
    for line in sys.stdin:
        # 按下换行键后，ctrl+d,输入结束
        try:
            temp_list = str(line).strip().split('->')
            temp_inner_dict = (temp_list[0], temp_list[1])
            gene_list.append(temp_inner_dict)
        except Exception as e:
            print('将输入的字符串转为计算机可识别的文法形式时，发生了错误：',str(e))
    print('输入的文法表示为：',gene_list)
    return gene_list

def cal_firstVt(gram_list: list,Vn_list:list,Vt_list:list) -> 'firstVt_dict':
    """计算每一个终结符的firstVt--{'a': set({'abc''})}"""
    # 初始化每一个终结符的firstVt集
    firstVt_dict = {}
    for v in Vn_list:
        firstVt_dict[v] = set()

    while True:
        # 循坏开始前，记录每个非终结符的firstvt集的长度
        len_list1 = len_dict(firstVt_dict)
        for gene in gram_list:
            # 产生式的右部含有终结符
            if has_Vt(gene):
                # 找出首个终结符
                first_vt = list(filter(lambda x: not isupper(x),gene[1]))[0]
                firstVt_dict[gene[0]].add(first_vt)
            # 产生式右部为空的情况
            elif gene[1] == '':
                pass
            else:
                # 产生式的右部不含终结符
                # 找出首个非终结符
                first_vn = list(filter(lambda x: isupper(x),gene[1]))[0]
                for char in firstVt_dict[first_vn]:
                    firstVt_dict[gene[0]].add(char)

        # 循坏开始后，记录每个非终结符的firstvt集的长度
        len_list2 = len_dict(firstVt_dict)
        # 如果每个非终结符的firstvt集都没有再变化，则计算完毕
        if len_list1 == len_list2:
            break

    print('firstVt集为:',firstVt_dict)
    return firstVt_dict


def cal_lastVt(gram_list: list,Vn_list,Vt_list) -> 'lastVt_dict':
    """计算每一个终结符的lastVt--{'a': {'abc''}}"""
    # 初始化每一个终结符的lastVt集
    lastVt_dict = {}
    for v in Vn_list:
        lastVt_dict[v] = set()

    while True:
        # 循坏开始前，记录每个非终结符的lastVt集的长度
        len_list1 = len_dict(lastVt_dict)
        for gene in gram_list:
            # 产生式的右部含有终结符
            if has_Vt(gene):
                # 找出最后一个终结符
                temp_list = list(filter(lambda x: not isupper(x), gene[1]))
                last_vt = temp_list[len(temp_list) - 1]
                lastVt_dict[gene[0]].add(last_vt)
            # 产生式右部为空的情况
            elif gene[1] == '':
                pass
            else:
                # 产生式的右部不含终结符
                # 找出最后一个非终结符
                temp_list = list(filter(lambda x: isupper(x), gene[1]))
                last_vn = temp_list[len(temp_list) - 1]
                for char in lastVt_dict[last_vn]:
                    lastVt_dict[gene[0]].add(char)

        # 循坏开始后，记录每个非终结符的lastVt集的长度
        len_list2 = len_dict(lastVt_dict)
        # 如果每个非终结符的lastVt集都没有再变化，则计算完毕
        if len_list1 == len_list2:
            break

    print('lastVt集为:', lastVt_dict)
    return lastVt_dict

def classify_status(gram_list: list,firstVt_dict,lastVt_dict) -> '[[set(),'>',set()]]':
    """计算终结符之间的关系"""
    status_list = []
    for gene in gram_list:
        if len(gene[1]) >= 2:
            for i in range(0,len(gene[1]) - 1):
                if not isupper(gene[1][i]) and not isupper(gene[1][i + 1]):
                    temp_set1 = set()
                    temp_set2 = set()
                    temp_set1.add(gene[1][i])
                    temp_set2.add(gene[1][i + 1])
                    temp_list = []
                    temp_list.append(temp_set1)
                    temp_list.append('=')
                    temp_list.append(temp_set2)
                    status_list.append(temp_list)
                elif not isupper(gene[1][i]) and isupper(gene[1][i + 1]):
                    temp_set1 = set()
                    temp_set2 = set()
                    temp_set1.add(gene[1][i])
                    temp_list = []
                    temp_list.append(temp_set1)
                    temp_list.append('<')
                    temp_list.append(firstVt_dict[gene[1][i + 1]])
                    # print('temp_list:',temp_list)
                    # print('status_list',status_list)
                    status_list.append(temp_list)
                    # print('status_list',status_list)
                elif isupper(gene[1][i]) and not isupper(gene[1][i + 1]):
                    temp_set1 = set()
                    temp_set2 = set()
                    temp_set2.add(gene[1][i + 1])
                    temp_list = []
                    temp_list.append(lastVt_dict[gene[1][i]])
                    temp_list.append('>')
                    temp_list.append(temp_set2)
                    status_list.append(temp_list)
        if len(gene[1]) >= 3:
            for i in range(0,len(gene[1]) - 2):
                # print(gene[1][i])
                if not isupper(gene[1][i]) and isupper(gene[1][i + 1]) and not isupper(gene[1][i + 2]):
                    temp_set1 = set()
                    temp_set2 = set()
                    temp_set1.add(gene[1][i])
                    temp_set2.add(gene[1][i + 2])
                    temp_list = []
                    temp_list.append(temp_set1)
                    temp_list.append('=')
                    temp_list.append(temp_set2)
                    status_list.append(temp_list)

    print('各终结符之间的优先关系：')
    for status in status_list:
        print(str(status))
    return status_list

def isOG(gram_list: list)->bool:
    """判断输入的文法是否为算符文法"""
    for gene in gram_list:
        # 若某一产生式有两个或两个以上的非终结符连在一起，则，该文法不是算符文法
        if re.match('[A-Z]{2,}',gene[1]):
            return False
    return True

def has_space(gram_list: list)->bool:
    """判断输入的文法中是否含有空产生式"""
    for gene in gram_list:
        if gene[1] == '':
            return True
    return False

def isOPG(gram_list: list,status_list: list)->bool:
    """判断输入的文法是否为算符优先文法"""
    OG = isOG(gram_list)
    Space = has_space(gram_list)
    # print('OG:', OG, 'Space:', Space)
    # 该文法不是OG文法
    if not OG:
        print('该文法不是OG文法，故，也不是OPG文法！')
        return False
    # 含有空产生式的OG
    elif OG and Space:
        print('该文法是空产生式的OG文法，故，不是OPG文法')
        return False
    # 不含有空产生式的OG
    elif OG and not Space:
        len_list = len(status_list)
        for i in range(0,len_list - 1):
            for j in range(i + 1, len_list):
                for v1 in status_list[i][0]:
                    for v2 in status_list[j][0]:
                        if v1 == v2:
                            for v3 in status_list[i][2]:
                                for v4 in status_list[j][2]:
                                    if v3 == v4 and status_list[i][1] != status_list[j][1]:
                                        print('该文法不满足算符优先文法的定义，不是OPG！')
                                        return False
        print('该文法满足算符优先文法的定义，是OPG！')
        return True

    else:
        print('该文法满足算符优先文法的定义，是OPG！')
        return True

def make_OPG_table(Vt_list:list,status_list:list)->None:
    """构造算符优先关系矩阵"""
    print('=' * len(Vt_list) * 10)
    # 输出表格的第一行
    print('|\t\t|', end='')
    # 列数
    for i in range(1, len(Vt_list) + 1):
        print('\t', Vt_list[i - 1], '\t|', end='')
    print()
    # 输出第二行以及后面的内容
    # 行数
    for j in range(1, len(Vt_list) + 1):
        print('|\t', Vt_list[j - 1], '\t|', end='')

        for n in range(1, len(Vt_list) + 1):
            for m in range(0,len(status_list)):
                if Vt_list[n - 1] in status_list[m][2] and Vt_list[j - 1] in status_list[m][0]:
                    print('\t', status_list[m][1], '\t|', end='')
                    break
            else:
                print('\t\t|', end='')
        print()

    print('=' * len(Vt_list) * 10)


def find_V(grammer_list: list) -> 'Vn_list,Vt_list':
    """找出文法中的所有非终结符和终结符"""
    # 非终结符列表
    Vn_list = []
    Vn_set = set()
    # 终结符列表
    Vt_list = []
    Vt_set = set()
    # 所有符号的列表
    total_list = []
    for i in grammer_list:
        # 将元组转为列表
        temp_list = list(i)
        # 将所有列表转为一个列表
        total_list.extend(temp_list)
        # 将列表转为字符串
        total_str = ''.join(total_list)
        # 将所有符号组成的字符串转为列表中的单个字符
        for char in total_str:
            # 筛选出字符列表中的终结符和非终结符
            if isupper(char):
                Vn_set.add(char)
            else:
                Vt_set.add(char)
    Vn_list = list(Vn_set)
    Vt_list = list(Vt_set)
    print('Vn为：',Vn_list)
    print('Vt为：', Vt_list)
    return Vn_list,Vt_list


def has_Vt(gene: tuple)->bool:
    """#判断产生式的右部是否含有终结符"""
    temp_vt_list = list(filter(lambda x: not isupper(x),gene[1]))
    if temp_vt_list != []:
        return True
    else:
        return False

def len_dict(my_dict: dict) -> list:
    """用于计算某一集合中的各个key对应的set的长度"""
    len_list = []
    for k, v in my_dict.items():
        len_list.append(len(v))
    return len_list

# 测试代码
gram_list = make_gram()
Vn_list,Vt_list = find_V(gram_list)
firstVt_dict = cal_firstVt(gram_list,Vn_list,Vt_list)
lastVt_dict = cal_lastVt(gram_list,Vn_list,Vt_list)
status_list = classify_status(gram_list,firstVt_dict,lastVt_dict)
isOPG = isOPG(gram_list,status_list)
if isOPG:
    print('算符优先矩阵如下：')
    make_OPG_table(Vt_list,status_list)
