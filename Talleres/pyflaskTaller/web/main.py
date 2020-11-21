from flask import Flask, request, make_response, redirect, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route("/login", methods= ("POST","GET"))
def login():
    if request.method == "POST":
        nameUser = request.form("name")
        passUser =request.form("pass")
        if (passUser== "12345"):
            return redirect(url_for("home.html"))
        else:
            return "Falló proceso de autentificación "
    else: 
        return render_template("login.html")
@app.route("/home") 
def home(): 
    return render_template("home.html")
@app.route("/personajesFav")
def personajesFav():
    return render_template("personajesFav.html")
@app.route("/lugaresFav")
def lugaresFav():
    return render_template("lugaresFav")
@app.errorhandler(404)
def not_foud(error):
    return render_template("404.html")

if __name__ =="__main__":
    app.run()


