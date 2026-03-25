from routes.appointments import appointments_bp
from routes.patients import patients_bp
from routes.doctors import doctors_bp
from flask import Flask, request
from flask import jsonify
from flask_cors import CORS
import sqlite3
app = Flask(__name__)
CORS(app)
app.register_blueprint(patients_bp)
app.register_blueprint(doctors_bp)
app.register_blueprint(appointments_bp)
@app.route("/")
def home():
    return "Hospital Management Backend Running"


@app.route("/patients")
def view_patients():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()

    patients = []

    for row in rows:
        patients.append({
            "id": row[0],
            "name": row[1],
            "age": row[2],
            "gender": row[3],
            "disease": row[4]
        })

    conn.close()

    return jsonify(patients)


@app.route("/add_patient", methods=["POST"])
def add_patient():

    name = request.form["name"]
    age = request.form["age"]
    gender = request.form["gender"]
    disease = request.form["disease"]

    conn = sqlite3.connect("database.db")

    conn.execute(
        "INSERT INTO patients (name, age, gender, disease) VALUES (?, ?, ?, ?)",
        (name, age, gender, disease)
    )

    conn.commit()
    conn.close()

    return "Patient added successfully"

@app.route("/add_test_patient")
def add_test_patient():

    conn = sqlite3.connect("database.db")

    conn.execute(
        "INSERT INTO patients (name, age, gender, disease) VALUES (?, ?, ?, ?)",
        ("Rahul", 25, "Male", "Fever")
    )

    conn.commit()
    conn.close()

    return "Test patient added"

@app.route("/doctors")
def view_doctors():

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM doctors")

    doctors = cursor.fetchall()

    conn.close()

    return str(doctors)

@app.route("/add_test_doctor")
def add_test_doctor():

    conn = sqlite3.connect("database.db")

    conn.execute(
        "INSERT INTO doctors (name, specialization, experience) VALUES (?, ?, ?)",
        ("Dr.Bani Kaur", "Cardiologist", 10)
    )

    conn.commit()
    conn.close()

    return "Test doctor added"   

@app.route("/add_test_appointment")
def add_test_appointment():

    conn = sqlite3.connect("database.db")

    conn.execute(
        "INSERT INTO appointments (patient_id, doctor_id, date, time) VALUES (?, ?, ?, ?)",
        (1, 1, "2026-03-20", "10:30")
    )

    conn.commit()
    conn.close()

    return "Test appointment added"   

@app.route("/appointments")
def view_appointments():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM appointments")

    rows = cursor.fetchall()

    appointments = []

    for row in rows:
        appointments.append({
            "id": row[0],
            "patient_id": row[1],
            "doctor_id": row[2],
            "date": row[3],
            "time": row[4]
        })

    conn.close()

    return jsonify(appointments)     

@app.route("/delete_patient/<int:patient_id>")
def delete_patient(patient_id):

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM patients WHERE id=?", (patient_id,))

    conn.commit()
    conn.close()

    return f"Patient {patient_id} deleted successfully"

@app.route("/update_patient/<int:patient_id>")
def update_patient(patient_id):

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE patients SET name=?, age=?, gender=?, disease=? WHERE id=?",
        ("Pranay Gupta", 22, "Male", "Heart Problem", patient_id)
    )

    conn.commit()
    conn.close()

    return f"Patient {patient_id} updated successfully"

if __name__ == "__main__":
    app.run(debug=True)

