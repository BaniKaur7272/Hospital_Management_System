from flask import Blueprint, jsonify
from models.db import get_db_connection

patients_bp = Blueprint('patients', __name__)

@patients_bp.route("/patients")
def view_patients():

    conn = get_db_connection()
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