import pymysql
from pymysql.cursors import DictCursor
import json

class UserModel():
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="learning_rest_api",
                cursorclass=DictCursor
            )
            self.cursor = self.conn.cursor()
            print('successfully connected!')
        except Exception as e:
            print(e)

    # get all users
    def user_getall_model(self):
        self.cursor.execute("SELECT * FROM users")
        result = self.cursor.fetchall()
        if len(result)>0:
            return json.dumps(result)
        else:
            return "No Data Exist"