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


@app.route('/user/updateuser', methods=['PUT'])
def user_updateuser():
    data = request.form
    return obj.user_updateuser_model(data)


@app.route('/user/deleteuser/<id>', methods=['DELETE'])
def user_deleteuser(id):
    return obj.user_deleteuser_model(id)


@app.route('/user/patchuser/<id>', methods=['PATCH'])
def user_patchuser(id):
    data = request.form
    return obj.user_patchuser_model(data, id)


@app.route('/user/getall/limit/<int:limit>/page/<int:page>', methods=['GET'])
def user_pagination(limit,page):
    return obj.user_pagination_model(limit, page)