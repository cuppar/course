from flask import Flask, render_template, request
from vsearch import search4letters
import time
import mysql.connector
import functools


class MySQLConnector:
    def __init__(self, **props):
        self.props = props

    def __enter__(self):
        self.conn = mysql.connector.connect(**self.props)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exception_type, exception_value, traceback):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


logined = False
username = ''


def userAuthentication(func):
    @functools.wraps(func)
    def wrapper(*args, **kwords):
        if logined:
            return func(*args, **kwords)
        else:
            return render_template('comfirmLogin.html')
    return wrapper


app = Flask(__name__)


@app.route('/login')
def login() -> 'html':
    return render_template('login.html')


@app.route('/logout')
def logout():
    global logined
    logined = False
    return render_template('login.html')


@app.route('/log')
@userAuthentication
def log():
    return render_template('log.html')


@app.route('/timeLog', methods=['post'])
def timeLog():
    time_input = request.form['time']
    sql = 'select * from log where time like "'+time_input+'%"'
    html = """\
<table>
  <thead>
    <tr>
        <th>user</th>
        <th>phrase</th>
        <th>letters</th>
        <th>results</th>
        <th>time</th>
        <th>ip</th>
    </tr>
  </thead>
  <tbody>
    """
    with MySQLConnector(**{'host': 'localhost', 'user': 'root',
                           'password': 'root', 'database': 'vsearch'}) as cursor:
        cursor.execute(sql)
        for user, phrase, letters, results, time, ip in cursor:
            html+="""\
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
    </tr>
            """%(user, phrase, letters, results, time, ip)
        html+="""\
  </tbody>
</table>
        """

    return render_template('log.html', logResults=html, state='time')

@app.route('/ipLog', methods=['post'])
def ipLog():
    ip_input = request.form['ip']
    sql = 'select * from log where ip="'+ip_input+'"'
    html = """\
<table>
  <thead>
    <tr>
        <th>user</th>
        <th>phrase</th>
        <th>letters</th>
        <th>results</th>
        <th>time</th>
        <th>ip</th>
    </tr>
  </thead>
  <tbody>
    """
    with MySQLConnector(**{'host': 'localhost', 'user': 'root',
                           'password': 'root', 'database': 'vsearch'}) as cursor:
        cursor.execute(sql)
        for user, phrase, letters, results, time, ip in cursor:
            html+="""\
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
    </tr>
            """%(user, phrase, letters, results, time, ip)
        html+="""\
  </tbody>
</table>
        """

    return render_template('log.html', logResults=html, state='ip')


@app.route('/authentication', methods=['POST'])
def authentication():
    global username
    username = request.form['username']
    password = request.form['password']
    user_map = {}
    with MySQLConnector(**{'host': 'localhost', 'user': 'root',
                           'password': 'root', 'database': 'vsearch'}) as cursor:
        sql = 'select * from user;'
        cursor.execute(sql)
        for name, pwd in cursor:
            user_map[name] = pwd
    if username in user_map.keys() and password == user_map[username]:
        global logined
        logined = True
        return render_template('entry.html', the_title=username+', Welcome to search4letters on the web!')
    else:
        return render_template('loginFail.html')


@app.route('/search4', methods=['POST'])
@userAuthentication
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))

    request_ip = str(request.remote_addr)
    accept_time = time.strftime(
        '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    with MySQLConnector(**{'host': 'localhost', 'user': 'root',
                           'password': 'root', 'database': 'vsearch'}) as cursor:
        sql = "insert into log(user, phrase, letters, results, time, ip) \
        value('"+username+"', '"+phrase+"', '"+letters+"', \""+results+"\", '"+accept_time+"', '"+request_ip+"');"
        cursor.execute(sql)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results, )


@app.route('/')
@app.route('/entry')
@userAuthentication
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title=username+', Welcome to search4letters on the web!')


if __name__ == '__main__':
    app.run(debug=True, port=8080)  # 自动监听修改重启
