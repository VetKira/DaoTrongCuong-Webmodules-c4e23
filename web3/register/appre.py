from flask import Flask, render_template , request
import mlabre
from register import Register
from gmail import GMail, Message 

gmail = GMail("yolovl.cf@gmail.com","yolovl.123")

mlabre.connect()



app = Flask(__name__)

@app.route("/register", methods = ["GET","POST"])
def register():
    if request.method =="GET" :
        return render_template("register.html")
    elif request.method =="POST":
        form = request.form
        u = form["username"]
        p = form["password"]
        e = form["email"]
        
        exist_user = Register.objects(username=u).first()
        if exist_user != None:
            return "user exists"
        else :
            r = Register(username = u , password = p , email = e)
            r.save()
            msg = Message("ban da dang ky thanh cong",to = e,text = "ban da dang ky thanh cong")
            gmail.send(msg) 
            return "Succesfull"
if __name__ == "__main__":
    app.run(debug=True)


