from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World"

@app.route('/user/signup')
def user_signup():
    return "This is user sign-up page"


if __name__ == "__main__":
    app.run(debug = True)