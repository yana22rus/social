from flask import Blueprint, render_template, flash, request, redirect, url_for, abort
from werkzeug.security import generate_password_hash, check_password_hash
from project.db import *
from datetime import datetime

authorization_bp = Blueprint("news", __name__, template_folder="templates")


@authorization_bp.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        hash = generate_password_hash(request.form["password"])
        login = request.form["login"]
        email = request.form["email"]
        time_registration = datetime.now()

        cursor.execute("INSERT INTO Users (login,hash_password,email,time_registration) VALUES (?,?,?,?)",
                       (login, hash, email, time_registration))
        connection.commit()

    return render_template("authorization.html")


@authorization_bp.route("/login", methods=["GET", "POST"])
def login():
    login = request.form.get("login")
    password = request.form.get("password")

    if login and password:

        user = f"""SELECT * FROM Users WHERE login='{login}';"""

        hash_password = cur.execute(f"""SELECT * FROM Users WHERE hash_password='{password}';""")

        if user and check_password_hash(hash_password, password):
            print(123)
            return "123"

    return render_template("login.html")
