import pymysql
from pymysql.cursors import DictCursor
from flask import make_response

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
            return make_response({'payload':result}, 200)
        else:
            return make_response({"message":"No Data Exist"}, 204)
        

    # adding new user 
    def user_adduser_model(self, data):
        try:
            self.cursor.execute(f"""
                INSERT INTO users(name, email)
                VALUES('{data['name']}', '{data['email']}')
            """)
            self.conn.commit()
            return make_response({"message":"User Added Successfully!"}, 201)
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
                return make_response({"message":"User Updated Successfully!"}, 200)
            else:
                return make_response({"message":"Nothing to Update!"}, 204)
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
                return make_response({"message":"User DELETE Successfully!"}, 200)
            else:
                return make_response({"message":"Nothing to Delete!"}, 204)
        except Exception as e:
            print(e)


    # patch - update only what is provided 
    def user_patchuser_model(self, data, id):
        try:
            query = "UPDATE users SET "

            for key,value in data.items():
                query += f"{key}='{value}',"

            query = query[:-1] + f" WHERE id={id}"

            self.cursor.execute(query)
            self.conn.commit()

            if self.cursor.rowcount>0:
                return make_response({'message':'User Updated Successfully!'}, 200)
            else:
                    return make_response({"message":"Nothing to Update!"}, 204)
        except Exception as e:
            print(e)


    # pagination 
    def user_pagination_model(self, limit, page):
        try:
            start = (limit * page) - limit
            query = f"""SELECT * FROM users LIMIT {start}, {limit}"""
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            if len(result) > 0:
                return make_response({"payload":result, 'limit':limit, 'page':page},200)
            else:
                return make_response({'message':'No Data Exist on this page'}, 204)
        except Exception as e:
            print(e)