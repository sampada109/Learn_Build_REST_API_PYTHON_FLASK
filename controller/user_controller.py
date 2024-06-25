from app import app
from model.user_model import UserModel
from flask import request, jsonify
from datetime import datetime

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


@app.route('/user/upload/avatar/<id>', methods=['PUT'])
def user_avatar(id):
    file = request.files['avatar']   #requesting to access only the value of uploaded file
    uniqueTime = str(datetime.now().timestamp()).replace(".","")     #generating a unique string of datetime
    ext = file.filename.split(".")[-1]  #extracting filename and by spliting the filename wrt '.' and getting a list and only storing the last which is extension 
    filepath = f'user{id}_{uniqueTime}.{ext}'
    saving = f'uploads/{filepath}'
    file.save(saving)
    return obj.user_upload_avatar(id, saving)