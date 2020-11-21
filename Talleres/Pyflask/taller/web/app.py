from flask import Flask, request, make_response, redirect, render_template, url_for

app = Flask(__name__)
@app.route("/")
@app.route("/inicio")
def inicio():
    return render_template("inicio.html")

@app.route("/personal")
def personal():
    return render_template("personal.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run()