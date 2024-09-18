from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# To run:
# cd example_code/other_frameworks
# set FLASK_APP=flask_simple
# flask run
