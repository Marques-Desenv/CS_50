from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/gabriel")
def gabriel():
    return "Hello, Gabriel!"


if __name__ == '__main__':
    app.run()