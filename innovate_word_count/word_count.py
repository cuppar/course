import jieba
import jieba.posseg
import re
import os

# a表示形容词，d表示副词，n表示名词，p表示介词，v表示动词。


def word_count(*, input_file_path,
               output_dir_path,
               max_num=20
               ):
    # 判断输入文件是否存在
    if not os.path.exists(input_file_path):
        print('输入文件位置不存在')
        return
# 并行分词
    jieba.enable_parallel(100)
# 读文件，分词
    article_in = open(input_file_path, 'r')
    article = article_in.read()
    words = jieba.posseg.cut(article)
# 统计词频
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
# 去杂
    punctuation = []
    word_pattern = re.compile(r'\w+')
    english_pattern = re.compile(r'[a-zA-Z0-9]+')
    for word in word_freq.keys():
        if not word_pattern.match(word.word)\
                or english_pattern.match(word.word)\
                or word.word == '':
            punctuation.append(word)
    for punc in punctuation:
        word_freq.pop(punc)
# 按词频降序排列
    freq_word = []
    for word, freq in word_freq.items():
        freq_word.append((word, freq))
    freq_word.sort(key=lambda x: x[1], reverse=True)
# 按词性分类
    adjective_freq_word = []
    adverb_freq_word = []
    noun_freq_word = []
    postposition_freq_word = []
    verb_freq_word = []

    for word, freq in freq_word:
        if word.flag == 'a':
            adjective_freq_word.append((word, freq))
        elif word.flag == 'd':
            adverb_freq_word.append((word, freq))
        elif word.flag == 'n':
            noun_freq_word.append((word, freq))
        elif word.flag == 'p':
            postposition_freq_word.append((word, freq))
        elif word.flag == 'v':
            verb_freq_word.append((word, freq))
# 创建输出目录
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)
# 创建输出文件
    adjective_out = open(output_dir_path+'adjective.txt', 'wt')
    adverb_out = open(output_dir_path+'adverb.txt', 'wt')
    noun_out = open(output_dir_path+'noun.txt', 'wt')
    postposition_out = open(output_dir_path+'postposition.txt', 'wt')
    verb_out = open(output_dir_path+'verb.txt', 'wt')
# 写文件函数

    def _write_file(freq_word_list, output_path, num):
        for word, freq in freq_word_list[:num]:
            output_path.write(word.word+' -> '+str(freq)+'\n')
# 写入文件
    _write_file(adjective_freq_word, adjective_out, max_num)
    _write_file(adverb_freq_word, adverb_out, max_num)
    _write_file(noun_freq_word, noun_out, max_num)
    _write_file(postposition_freq_word, postposition_out, max_num)
    _write_file(verb_freq_word, verb_out, max_num)
# 关闭文件流
    article_in.close()
    adjective_out.close()
    adverb_out.close()
    noun_out.close()
    postposition_out.close()
    verb_out.close()


if __name__ == '__main__':
    word_count(input_file_path='./answer-content.txt',
               output_dir_path='./word_count_results/',
               max_num=50
               )
