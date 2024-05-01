from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from models import Base
from models import Admins, db, app, Compamies
from flask_login import LoginManager, login_user, logout_user, login_required
from werkzeug.security import check_password_hash

# engine = create_engine("mysql+mysqldb://pld_admin:admin_pwd@localhost/pld_admin_db", pool_pre_ping=True)

login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    return Admins.query.get(int(user_id))

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/dashboard_admin")
def dashboard_admin():
    companies = Compamies.query.all()
    return render_template("dashboard_admin.html", companies=companies)



@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        name = request.form.get("name")
        user = Compamies(username=username, email=email, name=name)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        if user.approval == None:
            return render_template("wait.html")
        else:
            redirect(url_for('dashboard'))
    return render_template("register.html")

@app.route("/login_admin", methods=["GET", "POST"])
def login_admin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = Admins.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            return redirect(url_for('dashboard_admin'))
        else:
            return render_template("login.html", error="Invalid username or password")
    if request.method == "GET":
        return render_template("login.html", action="/login_admin")

@app.route("/login_user", methods=["GET", "POST"])
def login_user():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = Compamies.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            if user.approval is None:
                return render_template("wait.html")
            else:
                return redirect(url_for('dashboard'))
        else:
            return render_template("login.html", error="Invalid username or password")
    if request.method == "GET":
        return render_template("login.html", action="/login_user")

@app.route("/approval/<id>", methods=["POST"])
def approval(id):
    if request.args.get('approval'):
        user = Compamies.query.filter_by(id=id).first()

        user.approval = bool(request.args.get('approval'))
        db.session.commit()
    return redirect(url_for('dashboard_admin'))


