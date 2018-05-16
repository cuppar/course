import mysql.connector


def select(sql):
    try:
        conn = mysql.connector.connect(host='127.0.0.1', user='root',
                                       password='root', database='test')
        cursor = conn.cursor()
        cursor.execute(sql)
        for line in cursor.fetchall():
            print(line[0], line[1], line[2], line[3])
    except Exception as e:
        print('出错: '+str(e), end='')
    finally:
        cursor.close()
        conn.close()


select('select * from user')


def execSql(sql):
    try:
        conn = mysql.connector.connect(host='127.0.0.1', user='root',
                                       password='root', database='test')
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print('出错: '+str(e), end='')
    finally:
        cursor.close()
        conn.close()


execSql('insert into user(user_id, user_name, sex, age)\
          values(6, "test2", 0, 22)')
select('select * from user')
