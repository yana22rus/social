from flask import Flask, Blueprint, render_template, flash, request, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# db = SQLAlchemy(app)


from project.authorization.authorization import authorization_bp

app.register_blueprint(authorization_bp)



app.run(debug=True)
