from app import app
from model.user_model import UserModel

obj = UserModel()

@app.route('/user/getall')
def user_getall():
    return obj.user_getall_model()