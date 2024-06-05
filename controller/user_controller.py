from app import app

@app.route('/user/signup')
def user_signup():
    return "This is user sign-up page"