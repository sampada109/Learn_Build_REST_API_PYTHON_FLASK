import pymysql

class UserModel():
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="learning_rest_api"
            )
            self.cursor = self.conn.cursor()
            print('successfully connected!')
        except Exception as e:
            print(e)