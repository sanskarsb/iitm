from flask import Flask , redirect , url_for
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

#FOR database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////home/sanskar/MAD1/project/database/authen.sqlite3"
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()


class Admin(db.Model):
    __tablename__ = 'admin_auth'
    admin_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    admin_email = db.Column(db.String, unique = True,primary_key = True)
    admin_password = db.Column(db.String)

class Venue(db.Model):
    __tablename__ = 'venues'
    v_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    name = db.Column(db.String,unique = True)
    place = db.Column(db.String)
    capacity = db.Column(db.Integer)




@app.route("/admin",methods=["GET","POST"])
def admin():
    if(request.method == "GET"):
        return render_template("admin_login.html")
    elif(request.method == "POST"):
        admin_auth = Admin.query.all()
        n = len(admin_auth)
        flag = 0
        try_email = request.form["admin_email"]
        try_password = request.form["admin_password"]
        for i in range(0,n):
            if(try_email == admin_auth[i].admin_email):
                if(try_password == admin_auth[i].admin_password):
                    flag = 1
        print(flag)
        if(flag == 1):
            return redirect(url_for('dash'))
        else:
            return render_template("admin_login.html")

@app.route("/dashboard",methods=["GET","POST"])
def dash():
    return render_template("admin_dashboard.html")
    

@app.route("/user",methods=["GET","POST"])
def user():
    if(request.method == "GET"):
        return render_template("user_login.html")
    elif(request.method == "POST"):
        user_email = request.form["user_email"]
        user_password = request.form["user_password"]
        return render_template("user_login.html")




@app.route("/venueeditingform",methods = ["GET","POST"])
def venueeditingform():
    if(request.method == "GET"):
        return render_template("venueform.html")
        
    elif(request.method == "POST"):
        try_name = request.form["venuename"]
        try_place = request.form["venueplace"]
        try_capacity = request.form["venuecapacity"]
        print(try_name,try_place,try_capacity)
        data = Venue(name = try_name,place = try_place, capacity = try_capacity)
        db.session.add(data)
        db.session.commit()
        data.verified = True
        db.session.commit()
        print("data is added")
        return redirect(url_for('venueediting'))

@app.route("/venueediting",methods = ["GET","POST"])
def venueediting():
    if(request.method == "GET"):
        ven = Venue.query.all()
        items = len(ven)
        print(items)
        if(items == 0):
            return render_template("venue.html")
        elif(items > 0):
            print("IN ELIFFF")
            return render_template("venue.html",venuelist = ven)
    elif(request.method == "POST"):
        return redirect (url_for('venueeditingform'))
    
##########################################################################################
##########################################################################################
##########################################################################################\


@app.route("/addshow",methods = ["GET","POST"])
def addshow():
    if(request.method == "GET"):
        return render_template("addshow.html")
    elif(request.method == "POST"):
        try_showname = request.form["showname"]
        try_showrating = request.form["showrating"]
        try_showtag = request.form["showtags"]
        try_ticketprice = request.form["showticketprice"]

        return render_template("addshow.html")



if __name__ == "__main__":
    app.debug = True
    app.run()