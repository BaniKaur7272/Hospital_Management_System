from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/patients")
def patients():
    return render_template("patients.html")

@app.route("/doctors")
def doctors():
    return render_template("doctors.html")

@app.route("/appointments")
def appointments():
    return render_template("appointments.html")

if __name__ == "__main__":
    app.run(debug=True)