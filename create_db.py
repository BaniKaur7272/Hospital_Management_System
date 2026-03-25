import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Patients table
cursor.execute("""
CREATE TABLE IF NOT EXISTS patients(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
gender TEXT,
disease TEXT
)
""")

# Doctors table
cursor.execute("""
CREATE TABLE IF NOT EXISTS doctors(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
specialization TEXT,
experience INTEGER
)
""")

# Appointments table
cursor.execute("""
CREATE TABLE IF NOT EXISTS appointments(
id INTEGER PRIMARY KEY AUTOINCREMENT,
patient_id INTEGER,
doctor_id INTEGER,
date TEXT,
time TEXT
)
""")

conn.commit()
conn.close()

print("All tables created successfully")