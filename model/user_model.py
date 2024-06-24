import pymysql
from pymysql.cursors import DictCursor

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
            return {'payload':result}
        else:
            return {"message":"No Data Exist"}
        

    # adding new user 
    def user_adduser_model(self, data):
        try:
            self.cursor.execute(f"""
                INSERT INTO users(name, email)
                VALUES('{data['name']}', '{data['email']}')
            """)
            self.conn.commit()
            return {"message":"User Added Successfully!"}
        except Exception as e:
            print(e)


    # updating existing user 
    def user_updateuser_model(self, data):
        try:
            self.cursor.execute(f"""
                UPDATE users SET name='{data['name']}', email='{data['email']}'
                WHERE id = {data['id']}
            """)
            self.conn.commit()
            if self.cursor.rowcount>0:
                return {"message":"User Updated Successfully!"}
            else:
                return {"message":"Nothing to Update!"}
        except Exception as e:
            print(e)


    # deleting existing user 
    def user_deleteuser_model(self, id):
        try:
            self.cursor.execute(f"""
                DELETE FROM users
                WHERE id = {id}
            """)
            self.conn.commit()
            if self.cursor.rowcount>0:
                return {"message":"User DELETE Successfully!"}
            else:
                return {"message":"Nothing to Delete!"}
        except Exception as e:
            print(e)