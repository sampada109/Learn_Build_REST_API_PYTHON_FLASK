from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World"

# Import user_controller at the end to avoid circular import issues
import controller.user_controller

