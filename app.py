from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/tweede")
def tweede():
    vara = 5
    print(vara)
    vara+=24
    return "<p>Heel wat anders"+str(vara)+"</p>"

@app.route("/welkefiets/<hetmerk>")
def welkefiets(hetmerk):
    return "<p>Deze fietz "+hetmerk+"</p>"