from flask import Blueprint, jsonify
from models.db import get_db_connection

doctors_bp = Blueprint('doctors', __name__)

@doctors_bp.route("/doctors")
def view_doctors():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM doctors")
    rows = cursor.fetchall()

    doctors = []

    for row in rows:
        doctors.append({
            "id": row[0],
            "name": row[1],
            "specialization": row[2],
            "experience": row[3]
        })

    conn.close()

    return jsonify(doctors)



@doctors_bp.route("/update_doctor/<int:doctor_id>")
def update_doctor(doctor_id):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE doctors SET name=?, specialization=?, experience=? WHERE id=?",
        ("Dr.Bani Kaur", "Cardiologist", 9, doctor_id)
    )

    conn.commit()
    conn.close()

    return f"Doctor {doctor_id} updated successfully"


@doctors_bp.route("/delete_doctor/<int:doctor_id>")
def delete_doctor(doctor_id):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM doctors WHERE id=?", (doctor_id,))

    conn.commit()
    conn.close()

    return f"Doctor {doctor_id} deleted successfully"