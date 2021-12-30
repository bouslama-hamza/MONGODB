from flask import Flask ,render_template , request
from flask_pymongo import PyMongo
app = Flask(__name__)

app.config["SECRET_KEY"] = 'UNS654SD22W81WD2F1S4E3FF1SDF'

app.config["MONGO_URI"]  = "mongodb://localhost:27017/NATURE"
mongo = PyMongo(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/service")
def service():
    return render_template("services.html")

@app.route("/contact" , methods = ['GET' , 'POST'])
def contact():
    if request.method == 'POST':
        client = mongo.db.USERS
        client.insert_one({"FullName" : request.form.get("name") , "Email" : request.form.get("email") , "Message" : request.form.get("message")})
        message = "Message A Etait Bien Recu"
        return render_template("contact.html" , message = message)
    return render_template("contact.html")

@app.route("/admin" , methods = ['GET' , 'POST'])
def admin():
    if request.method == 'POST':
        admin = mongo.db.ADMIN
        is_exists = admin.find_one({"Email" : request.form.get("email") , "Password" : request.form.get("password")})
        if is_exists:
            test = mongo.db.USERS
            info = test.find()
            return render_template("adminlogin.html" , info = info)
        else:
            message = "Invalid , Merci De Voir Votre Information"
            
            return render_template("admin.html" , message = message )
    return render_template("admin.html")

@app.route("/app")
def apps():
    test = mongo.db.USERS
    info = test.find()
    return render_template("adminlogin.html" , info = info)

#route for manage account
@app.route("/Manage Account" , methods = ['GET','POST'])
def Manage():
    if request.method == 'POST':
        test = mongo.db.Employer
        First = request.form.get("name")
        Last  = request.form.get("l_name")
        email  = request.form.get("email")
        password  = request.form.get("password")
        phone = request.form.get("phone")
        test.insert_one(
            {
                "FirstName" : First,
                "LastName" : Last,
                "Email" : email,
                "Password" : password,
                "Phone" : phone,
            })
        alert = "Le Compte A ete Bien Crier"
        return render_template("manage_account.html" , alert = alert)
    return render_template("manage_account.html")

#route for modifier account
@app.route("/Active account" , methods = ['GET','POST'])
def active_account():
    if request.method == 'POST':
        test = mongo.db.ADMIN
        First = request.form.get("ch_name")
        Last  = request.form.get("ch_l_name")
        email  = request.form.get("ch_email")
        password  = request.form.get("ch_password")
        phone = request.form.get("ch_phone")
        myquery = { "fullname": "AdminForet" }
        newvalues = { "$set": {
                        "FirstName": First ,
                        "LastName" : Last,
                        "Email" : email,
                        "Password" : password, 
                        "Phone" : phone,  
                    }}
        test.update_one(myquery , newvalues)
        message = "Profile A Etait Editer"
        return render_template("active_account.html" ,message = message)
    return render_template("active_account.html")

if __name__ == '__main__':
    app.run(debug=True , port= 8000)