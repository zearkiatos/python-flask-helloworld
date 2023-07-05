from flask import Flask, request, make_response, redirect, render_template, abort, session, url_for, flash
from flask_bootstrap import Bootstrap
import os
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import unittest

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = os.environ.get('SUPER_SECRET')

todos = ['Practice Python', 'Practice Javascript', 'Practice ReactJS']


class LoginForm (FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password',  validators=[DataRequired()])
    submit = SubmitField('Submit')


NOT_FOUND = 404
INTERNAL_SERVER_ERROR = 500


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)
    pass


@app.errorhandler(NOT_FOUND)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(INTERNAL_SERVER_ERROR)
def internal_server_error(error):
    return render_template('500.html', error=error)


@app.route("/")
def index():
    user_ip = request.remote_addr
    if not session.get('user_ip'):
        session['user_ip'] = user_ip
    response = make_response(redirect("/user-ip-page"))

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
        user_ip = session.get("user_ip")
        return "Your IP es {}".format(user_ip)
    except Exception:
        abort(INTERNAL_SERVER_ERROR)


@app.route("/user-ip-page")
def user_ip_page():
    try:
        user_ip = session.get("user_ip")
        context = {
            'user_ip': user_ip,
            'todos': todos,
        }
        return render_template("hello.html", **context)
    except Exception:
        abort(INTERNAL_SERVER_ERROR)


@app.route("/login", methods=['GET', 'POST'])
def login():
    try:
        user_ip = session.get("user_ip")
        login_form = LoginForm()
        username = session.get('username')
        context = {
            'user_ip': user_ip,
            'todos': todos,
            'login_form': login_form,
            'username': username
        }

        if login_form.validate_on_submit():
            username = login_form.username.data
            session['username'] = username

            flash('User saved successful')
            return redirect(url_for('login'))

        return render_template("login.html", **context)
    except Exception:
        abort(INTERNAL_SERVER_ERROR)


@app.route("/force-internal-server-error")
def force_internal_server_error():
    abort(INTERNAL_SERVER_ERROR)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
