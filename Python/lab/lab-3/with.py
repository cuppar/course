import mysql.connector


class UseDataBase:
    def __init__(self, props):
        self.props = props

    def __enter__(self):
        self.conn = mysql.connector.connect(**self.props)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_ty, exc_val, tb):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


props = {
    'host': 'localhost',
    'database': 'test',
    'user': 'root',
    'password': 'root'
}

with UseDataBase(props) as cursor:
    cursor.execute(
        'insert into user(user_id, user_name, sex, age)\
          values(5, "test", 1, 33)'
    )
    cursor.execute(
        'select * from user'
    )
    for (user_id, user_name, sex, age) in cursor:
        print('user_id:', user_id, 'user_name:', user_name,
              'sex:', sex, 'age', age)
