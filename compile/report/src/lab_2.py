# 编写一个程序，用于判定给定的文法是否为LL（1）文法。
# 注意：1．文法的机内表示；
# 2. FIRST集和FOLLOW集的计算；
# 3. LL（1）预测分析表的构造。

# 测试数据：
# S->aBZ
# Z->bBS
# Z->
# B->Ab
# B->e
# A->a
# A->

# 1. 将输入的文法表示为计算机中的元组列表[('A','abc')]
# 2.计算每一个非终结符first集和follow集（字典）：{'A': set{'abc'}}
# 3.计算每一个产生式的select集(字典列表)：{'A->abc': set{'abc'}}
# 4.判断是否为LL(1)文法(对任意非终极符的不同的两个产生式求交集，为空，则为LL(1)文法)
# 5.构造预测分析表（根据select集构造表）

import sys
import re
from numpy.core.defchararray import isupper,islower


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

def cal_first(gene_list: list,Vn_list: list) -> 'first_dict':
    """计算每一个非终结符first集（字典结构）{'A': set{'abc'}，}"""
    # 为所有的非终结符初始化first集
    first_dict = {}
    for Vn in Vn_list:
        first_dict[Vn] = set()

    while True:
        # 记录每轮循环前的first集的大小
        len_list1 = len_dict(first_dict)

        # 遍历每一条产生式，计算first集
        for gene in gene_list:
            if gene[1] == '':
                first_char = ''
            else:
                first_char = gene[1][0]
            # print(first_char)
            if first_char in Vt_list:
                first_dict[gene[0]].add(first_char) # and len(gene[1]) == 1
            elif first_char == '' and len(gene[1]) == 0:
                first_dict[gene[0]].add('')
            elif first_char in Vn_list:
                # 找到产生式右部首个一定不为空的符号的位置
                # 初始化为最后一个符号
                not_null_index = len(gene[1]) - 1
                for i in range(1, len(gene[1])):
                    v = gene[1][i]
                    # 首个Vn不能推出空，或者能推出空后面的首个Vt
                    if isupper(v) and '' not in first_dict[v] or islower(v):
                        not_null_index = i
                        break
                # 计算该情况下的first集
                for i in range(0, not_null_index + 1):
                    if islower(gene[1][i]):
                        first_dict[gene[0]].add(gene[1][i])
                    else:
                        for char in first_dict[gene[1][i]]:
                            if '' in first_dict[gene[1][i]]:
                                first_dict[gene[0]].add(char)
                                first_dict[gene[0]] -= {''}
                            else:
                                first_dict[gene[0]].add(char)

        # 记录每轮循环后的first集的大小
        len_list2 = len_dict(first_dict)
        # 判断first是否增大，若全未增大，则循环结束
        if len_list1 == len_list2:
            break

    print('first集为：',first_dict)
    return first_dict


def cal_follow(gene_list: list,Vn_list:list,first_dict: dict) -> 'follow_dict':
    """计算每一个非终结符follow集（字典结构）{'A': set{'abc'}，}"""
    # 为每一个非终结符初始化follow集,初始化开始符号的follow集为#
    follow_dict = {}
    for Vn in Vn_list:
        follow_dict[Vn] = set()
    follow_dict['S'].add('#')

    while True:
        len_list1 = len_dict(follow_dict)

        # for Vn in Vn_list:
        for gene in gene_list:
            for i in range(0,len(gene[1])):
                # 指定的非终结符后还有其他符号
                if isupper(gene[1][i]) and i < len(gene[1]) - 1:
                    if islower(gene[1][i + 1]):
                        follow_dict[gene[1][i]].add(gene[1][i + 1])
                    else:
                        # 找到产生式右部的指定个非终结符后首个一定不为空的符号的位置
                        # 初始化为最后一个符号的位置
                        not_null_index = len(gene[1]) - 1
                        for j in range(i + 1, len(gene[1])):
                            v = gene[1][j]
                            # 首个Vn不能推出空，或者能推出空后面的首个Vt
                            if isupper(v) and '' not in first_dict[v] or islower(v):
                                not_null_index = j
                                break
                        # 没找到产生式右部的指定个非终结符后首个一定不为空的符号
                        if isupper(gene[1][not_null_index]) and not_null_index == len(gene[1]) - 1 and '' in first_dict[gene[1][not_null_index]]:
                            for m in range(i + 1,not_null_index + 1):
                                for char in first_dict[gene[1][m]]:
                                    follow_dict[gene[1][i]].add(char)
                                follow_dict[gene[1][i]] -= {''}
                            for char in follow_dict[gene[0]]:
                                follow_dict[gene[1][i]].add(char)
                        # 找到了产生式右部的指定的非终结符后首个一定不为空的符号
                        else:
                            # 计算该情况下的follow集
                            for n in range(i + 1, not_null_index + 1):
                                if islower(gene[1][n]):
                                    follow_dict[gene[1][i]].add(gene[1][n])
                                else:
                                    if '' in first_dict[gene[1][n]]:
                                        for char in first_dict[gene[1][n]]:
                                            follow_dict[gene[1][i]].add(char)
                                        follow_dict[gene[1][i]] -= {''}
                                    else:
                                        for char in first_dict[gene[1][n]]:
                                            follow_dict[gene[1][i]].add(char)
                # 所求的非终结符位于产生式右部的最后一位
                elif isupper(gene[1][i]) and i == len(gene[1]) - 1:
                    for char in follow_dict[gene[0]]:
                        follow_dict[gene[1][i]].add(char)

        len_list2 = len_dict(follow_dict)
        if len_list1 == len_list2:
            break
    print('follow集为：',follow_dict)
    return follow_dict

def cal_select(gene_list: list, first_dict: dict, follow_dict: dict) -> 'select_dict':
    """计算每一个产生式的select集(字典结构)：{'A->abc': set{'abc'}，}"""
    # 初始化select集
    select_dict = {}
    # for gene in gene_list:
    #     temp_gene = '->'.join(gene)
    #     select_dict[temp_gene] = set()

    for gene in gene_list:
        temp_gene = '->'.join(gene)
        select_dict[temp_gene] = set()
        # 产生式右部为空
        if gene[1] == '':
            for char in follow_dict[gene[0]]:
                select_dict[temp_gene].add(char)
                # 产生式右部第一个符号为终结符
        elif islower(gene[1][0]):
            select_dict[temp_gene].add(gene[1][0])
        # 产生式右部第一个符号为非终结符
        elif isupper(gene[1][0]):
            for v in gene[1]:
                    # 找到产生式右部首个一定不为空的符号的位置
                    # 初始化为最后一个符号
                    not_null_index = len(gene[1]) - 1
                    for i in range(1, len(gene[1])):
                        v = gene[1][i]
                        # 首个Vn不能推出空，或者能推出空后面的首个Vt
                        if isupper(v) and '' not in first_dict[v] or islower(v):
                            not_null_index = i
                            break
                    # 产生式的右部可推出空
                    if isupper(gene[1][not_null_index]) and not_null_index == len(gene[1]) - 1 and '' in first_dict[gene[1][not_null_index]]:
                        for m in (0,len(gene[1])):
                            select_dict[temp_gene].add(first_dict[gene[1][m]])
                        select_dict[temp_gene] -= {''}
                        select_dict[temp_gene].add(follow_dict[gene[0]])
                    # 产生式的右部不可推出空
                    else:
                        for n in range(0, not_null_index + 1):
                            if islower(gene[1][n]):
                                select_dict[temp_gene].add(gene[1][n])
                            else:
                                if '' in first_dict[gene[1][n]]:
                                    for char in first_dict[gene[1][n]]:
                                        select_dict[temp_gene].add(char)
                                        select_dict[temp_gene] -= {''}
                                else:
                                    for char in first_dict[gene[1][n]]:
                                        select_dict[temp_gene].add(char)

    print('select集为：',select_dict)
    return select_dict

def is_LL1(select_dict: dict) -> (bool,list):
    """判断是否为LL(1)文法"""
    is_LL1 = True
    # 将select_dict转为[(),]
    select_list = []
    for k,v in select_dict.items():
        temp_keys_list = str(k).split('->')
        select_list.append((temp_keys_list[0],v))
    # print(select_list)
    for i in range(0,len(select_list) - 1):
        for j in range(i + 1,len(select_list)):
            if select_list[i][0] == select_list[j][0]:
                for v in select_list[i][1]:
                    if v in select_list[j][1]:
                        is_LL1 = False
    return is_LL1,select_list


def make_predict_table(gram_list: list, select_list: list,Vn_list,Vt_list) -> None:
    """构造预测分析表"""
    print('=' * len(Vt_list) * 12)
    # 输出表格的第一行
    print('|\t\t|',end='')
    for i in range(0,len(Vt_list)):
        print('\t',Vt_list[i],'\t|',end='')
    print()
    # 输出第二行以及后面的内容
    for m in range(1,len(Vn_list) + 1):
        print('|\t',Vn_list[m - 1],'\t|',end='')

        # 产生式左部相同的select集的列表
        same_keys_value_list = []
        # 产生式左部相同的右部的列表
        same_keys_right_list = []
        for g in range(0,len(select_list)):
            if Vn_list[m - 1] == select_list[g][0]:
                same_keys_value_list.append(select_list[g][1])
                same_keys_right_list.append(gram_list[g][1])

        for n in range(1,len(Vt_list) + 1):
            for k in range(0,len(same_keys_value_list)):
                if Vt_list[n - 1] in same_keys_value_list[k]:
                    if same_keys_right_list[k] == '':
                        print(' ', 'null', ' |', end='')
                        break
                    else:
                        print('\t', same_keys_right_list[k], '|', end='')
                        break
            else:
                print('\t\t|', end='')
        print()
    print('=' * len(Vt_list)* 12)


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
    Vt_list.append('#')
    print('Vn为：',Vn_list)
    print('Vt为：', Vt_list)
    return Vn_list,Vt_list


def len_dict(my_dict: dict) -> list:
    """用于计算某一集合中的各个key对应的set的长度"""
    len_list = []
    for k, v in my_dict.items():
        len_list.append(len(v))
    return len_list

# 测试代码
grammer_list = make_gram()
Vn_list,Vt_list = find_V(grammer_list)
first_list = cal_first(grammer_list,Vn_list)
follow_dict = cal_follow(grammer_list,Vn_list,first_list)
select_dict = cal_select(grammer_list,first_list,follow_dict)
is_LL1,select_list = is_LL1(select_dict)
if is_LL1:
    print('输入的文法是LL（1）文法！')
    make_predict_table(grammer_list, select_list, Vn_list, Vt_list)
else:
    print('输入的文法不是LL（1）文法！')
