from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)


@app.route("/")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect("/user-ip-page"))
    response.set_cookie("user_ip", user_ip)

    return response


@app.route("/hello")
def hello():
    return "Hello World! 👋 🌎 Flask 🌶️"


@app.route("/user-ip")
def user_ip():
    user_ip = request.cookies.get("user_ip")
    return "Your IP es {}".format(user_ip)


@app.route("/user-ip-page")
def user_ip_page():
    user_ip = request.cookies.get("user_ip")
    return render_template("hello.html", user_ip=user_ip)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
