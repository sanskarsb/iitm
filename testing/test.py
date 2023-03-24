from flask import Flask, session, flash,redirect
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy,create_engine
from flask_restful import Resource, Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////home/sanskar/MAD1/project/database/authen.sqlite3"
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()
app.secret_key = "hello"

engine = create_engine("sqlite:////home/sanskar/MAD1/project/database/authen.sqlite3")

class Admin(db.Model):
    __tablename__ = 'admin_auth'
    admin_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    admin_email = db.Column(db.String, unique = True,primary_key = True)
    admin_password = db.Column(db.String)
class tyr(db.Model):
    __tablename__ = 'tyr'
  
    Field1 = db.Column(db.Integer,primary_key = True)


@app.route("/",methods = ["GET","POST"])
def home():
    if(request.method == "GET"):
    # admin_emails = Admin.query.all()
    # print(admin_emails[0].admin_email)
    # pr0int(admin_emails[0].admin_password)
        return render_template("home.html")
    elif(request.method == "POST"):
        try_x = request.form["sanskar"]
        print(try_x)
        print("data is added")
        return render_template("home.html")


if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        debug = True,
        port = 8000
        )