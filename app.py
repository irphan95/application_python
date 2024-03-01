from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to Jenkins Tutorials<h1/>"

if __name__ == '__main__':
    app.run(debug=True,host='192.168.10.128'
