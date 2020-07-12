from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_world():
        return "Hello EE, This is Santosh!"

if __name__ == "__main__":
        app.run(host='0.0.0.0')
