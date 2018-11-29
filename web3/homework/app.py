from flask import Flask, render_template , request
import mlab
from bike import Bike

mlab.connect()

app = Flask(__name__)

@app.route("/new_bike", methods = ["GET","POST"])
def new_bike():
    if request.method == "GET" :
        return render_template("bike.html")
    elif request.method == "POST":
        form = request.form
        m = form["model"]
        d = form["daily"]
        i = form["image"]
        y = form["year"]
        b = Bike(model = m, daily = d, image = i, year = y)
        b.save()
        return "Success"

if __name__ == "__main__":
    app.run(debug=True)
