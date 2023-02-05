from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World! 👋 🌎 Flask 🌶️"

@app.route("/user-ip")
def user_ip():
    user_ip = request.remote_addr
    return "Your IP es {}".format(user_ip)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
