from flask import Flask, request, make_response, redirect, render_template, abort, session
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = os.environ.get('SUPER_SECRET')

todos = ['Practice Python', 'Practice Javascript', 'Practice ReactJS']

NOT_FOUND = 404
INTERNAL_SERVER_ERROR=500


@app.errorhandler(NOT_FOUND)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(INTERNAL_SERVER_ERROR)
def internal_server_error(error):
    return render_template('500.html', error=error)


@app.route("/")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect("/user-ip-page"))
    session['user_ip'] = user_ip

    return response


@app.route("/hello")
def hello():
    try:
        return "Hello World! 👋 🌎 Flask 🌶️"
    except Exception:
        abort(INTERNAL_SERVER_ERROR)


@app.route("/user-ip")
def user_ip():
    try:
        user_ip = request.cookies.get("user_ip")
        return "Your IP es {}".format(user_ip)
    except Exception:
        abort(INTERNAL_SERVER_ERROR)


@app.route("/user-ip-page")
def user_ip_page():
    try:
        user_ip = session.get("user_ip")
        context = {
            'user_ip': user_ip,
            'todos': todos
        }
        return render_template("hello.html", **context)
    except Exception:
        abort(INTERNAL_SERVER_ERROR)

@app.route("/force-internal-server-error")
def force_internal_server_error():
    abort(INTERNAL_SERVER_ERROR)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
