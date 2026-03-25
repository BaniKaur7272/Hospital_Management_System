from flask import Blueprint, jsonify
from models.db import get_db_connection

appointments_bp = Blueprint('appointments', __name__)

@appointments_bp.route("/appointments")
def view_appointments():

    conn = get_db_connection()
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

@appointments_bp.route("/add_appointment")
def add_appointment():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO appointments (patient_id, doctor_id, date, time) VALUES (?, ?, ?, ?)",
        (1, 1, "2026-03-25", "11:00")
    )

    conn.commit()
    conn.close()

    return "Appointment added successfully"

@appointments_bp.route("/delete_appointment/<int:appointment_id>")
def delete_appointment(appointment_id):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM appointments WHERE id=?", (appointment_id,))

    conn.commit()
    conn.close()

    return f"Appointment {appointment_id} deleted successfully"

