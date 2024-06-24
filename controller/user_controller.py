from app import app
from model.user_model import UserModel
from flask import request, jsonify

obj = UserModel()

@app.route('/user/getall')
def user_getall():
    return obj.user_getall_model()


@app.route('/user/adduser', methods=['POST'])
def user_adduser():
    data = request.form
    return obj.user_adduser_model(data)