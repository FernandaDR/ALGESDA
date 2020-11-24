from flask import Flask, request, make_response, redirect, render_template, url_for

app = Flask(__name__)

@app.route("/")
def baseRoute():
    return render_template("homeParcial.html")

@app.route("/conocenos")
def conocenos():
    return render_template("conocenos.html")

@app.route("/contactanos")
def contactanos():
    return render_template("contactanos.html")

@app.route("/doctores")
def doctores():
    return render_template("doctores.html")

@app.route("/pacientes")
def pacientes():
    return render_template("pacientes.html")

@app.route("/datoCurioso")
def datoCurioso():
    return render_template("datoCurioso.html")

if __name__ == "__main__":
    app.run()