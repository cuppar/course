import jieba
import jieba.posseg
import jieba.analyse
import re
#---------------------------------------------------------
# 普通分词
# seg_list = jieba.cut('小明硕士毕业于中国科学院计算所，后在日本京都大学深造。')
# print('Full Mode: '+'/'.join(seg_list))
# seg_list2 = jieba.cut('小明硕士毕业于中国科学院计算所，后在日本京都大学深造。')
# print('Full Mode: '+'/'.join(seg_list2))

#-----------------------------------------------------
# 导入自定义字典
# seg_list3=jieba.cut('如何评价复仇者联盟3。')
# print('Origin:'+'/'.join(seg_list3))

# jieba.load_userdict('/home/cuppar/projects/course/innovate/myDict.txt')
# seg_list4=jieba.cut('如何评价复仇者联盟3。')
# print('Revise:'+'/'.join(seg_list4))
#--------------------------------------------
# 调整词频
# print('Origin:'+'/'.join(jieba.cut('如果放到post中将出错', HMM=False)))
# True
# jieba.suggest_freq(('中', '将'), tune=True)
# print('Revise:'+'/'.join(jieba.cut('如果放到post中将出错', HMM=False)))

# ------------------------------------------
# 添加关键词
# Original='/'.join(jieba.cut('江苏市长江大桥参加了长江大桥的通车仪式。', HMM=False))
# print('Original: '+Original)

# print('HMM=False: '+'/'.join(jieba.cut('江苏市长江大桥参加了长江大桥的通车仪式。', HMM=False)))
# print('HMM=True: '+'/'.join(jieba.cut('江苏市长江大桥参加了长江大桥的通车仪式。', HMM=True)))

# # jieba.add_word('江大桥', freq=20000, tag=None)
# # print('add_word: '+'/'.join(jieba.cut('江苏市长江大桥参加了长江大桥的通车仪式。', HMM=False)))

# jieba.load_userdict('/home/cuppar/projects/course/innovate/shizhang.txt')
# print('loadUserDict: '+'/'.join(jieba.cut('江苏市长江大桥参加了长江大桥的通车仪式。', HMM=False)))
#-----------------------------------------------
# a表示形容词，d表示副词，n表示名词，p表示介词，v表示动词。
# words = jieba.posseg.cut('我爱北京天安门')
# for w in words:
#     print('%s %s' % (w.word, w.flag))
#----------------------------------------------
# f = open('/home/cuppar/projects/course/innovate/extractTags.txt', 'r').read()
# seg = jieba.analyse.extract_tags(f, topK=20, withWeight=True)
# for tag, weight in seg:
#     print('%s %s' % (tag, weight))
# -----------------------------------------------
# jieba.enable_parallel(4)
# f = open('/home/cuppar/projects/course/innovate/extractTags.txt', 'r').read()
# seg = jieba.analyse.extract_tags(f, topK=20, withWeight=True)
# for tag, weight in seg:
#     print('%s %s' % (tag, weight))
#--------------------------------------------------
# result = jieba.tokenize(u'永和服装饰品有限公司')
# for tk in result:
#     print('%s \t start at: %d \t end at: %d' % (tk[0], tk[1], tk[2]))
#-------------------------------------------
# result = jieba.tokenize(u'永和服装饰品有限公司', mode='search')
# for tk in result:
#     print('%s \t start at: %d \t end at: %d' % (tk[0], tk[1], tk[2]))
#--------------------------------------------
# jieba.initialize()
# print('/'.join(jieba.cut('你好，我是何志颖。')))
#---------------------------------------------
# 统计词频
jieba.enable_parallel(10)
article = open(
    '/home/cuppar/projects/course/innovate/answer-content.txt', 'r').read()
words = jieba.posseg.cut(article)

word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

punctuation = []
word_pattern = re.compile(r'\w+')
english_pattern = re.compile(r'[a-zA-Z0-9]+')
print(word_freq.keys())
for word in word_freq.keys():
    if not word_pattern.match(word.word)\
            or english_pattern.match(word.word)\
            or word.word == ''\
            or len(word.word) <= 1:
        punctuation.append(word)
print(punctuation)
for punc in punctuation:
    word_freq.pop(punc)

freq_word = []
for word, freq in word_freq.items():
    freq_word.append((word, freq))
freq_word.sort(key=lambda x: x[1], reverse=True)

max_number = int(input(u"需要前几个高频词？"))

output = open(
    '/home/cuppar/projects/course/innovate/word-freq-result.txt', 'wt')
for word, freq in freq_word[: max_number]:
    output.write(word.word+'/'+word.flag+' -> '+str(freq)+'\n')
    print(word.word+'/'+word.flag+' -> '+str(freq))
#----------------------------------------------
