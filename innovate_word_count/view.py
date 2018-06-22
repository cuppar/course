from flask import Flask, render_template, request
import word_count


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():

    # 数据库---用问题ID和问题内容填充questions变量
    questions = '<tr><td>1</td><td>你认为世界上最厉害的人是谁？</td><tr>'
    return render_template('entry.html', title='知乎问题答案分析', questions=questions)


@app.route('/search', methods=['POST'])
def search():
    question_id = request.form['question-id']
    max_num = int(request.form['max-num'])
    record_txt_path = ''
    result_dir_path = './word_count_results/'
# ------数据库写在下面，input: 问题ID---------------------------
# -----output: 1.待处理文本的txt文件路径-2.用问题ID和问题内容填充questions变量
    questions = '<tr><td>1</td><td>你认为世界上最厉害的人是谁？</td><tr>'
    if question_id == '1':
        # 把响应id的问题答案写入下面这个路径的文件即可
        record_txt_path = './answer-content.txt'
# -------------------------数据库写在上面-------------------------------------
    word_count.word_count(
        input_file_path=record_txt_path,
        output_dir_path=result_dir_path,
        max_num=max_num
    )

    def _txt_to_html(txt_path, title):
        txt_in = open(txt_path)

        def _read_file(file_in) -> 'html-str':
            result = ''
            for line in file_in:
                result += '<tr><td>'+line.strip()+'</td></tr>\n'
            return result

        html = _read_file(txt_in)
        html = '<table class="result-table" border="1"><tr><th>' + \
            title+'</th></tr>\n'+html+'</table>'
        txt_in.close()
        return html

    adjective_html = _txt_to_html(result_dir_path + 'adjective.txt', '形容词')
    adverb_html = _txt_to_html(result_dir_path + 'adverb.txt', '副词')
    noun_html = _txt_to_html(result_dir_path + 'noun.txt', '名词')
    postposition_html = _txt_to_html(
        result_dir_path + 'postposition.txt', '介词')
    verb_html = _txt_to_html(result_dir_path + 'verb.txt', '动词')

    results_html = '''
<div class="row">
    <div class="col">%s</div>
    <div class="col">%s</div>
    <div class="col">%s</div>
    <div class="col">%s</div>
    <div class="col">%s</div>
</div>
    ''' % (adjective_html, adverb_html, noun_html, postposition_html, verb_html)

    return render_template('entry.html', title='知乎问题答案分析',
                           results=results_html, questions=questions)


if __name__ == '__main__':
    app.run(debug=True)
