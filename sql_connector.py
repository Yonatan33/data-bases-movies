import mysql.connector


class SQLConnector:

    def __init__(self):
        self.connector = mysql.connector.connect(
            host='127.0.0.1',
            port=3305,
            user='DbMysql31',
            password='DbMysql31',
            database='DbMysql31',
        )
        self.cursor = self.connector.cursor()

    def execute_query(self, cmd):
        self.cursor.execute(cmd)

    def close(self):
        self.connector.close()


