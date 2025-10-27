import sqlite3

class Database:
    def __init__(self, db_name="students.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pib TEXT,
            group_number TEXT,
            birth_date TEXT,
            address TEXT,
            subjects TEXT,
            real_avg REAL,
            desired_avg REAL
        )
        """)
        self.conn.commit()

    def insert_student(self, data: dict):
        self.cursor.execute("""
        INSERT INTO students (pib, group_number, birth_date, address, subjects, real_avg, desired_avg)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            data["PIB"],
            data["Group"],
            data["BirthDate"],
            data["Address"],
            ', '.join(data["Subjects"]),
            data["RealAvg"],
            data["DesiredAvg"]
        ))
        self.conn.commit()

    def update_student(self, student_id: int, field: str, value):
        self.cursor.execute(f"UPDATE students SET {field} = ? WHERE id = ?", (value, student_id))
        self.conn.commit()

    def delete_student(self, student_id: int):
        self.cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        self.conn.commit()

    def show_all(self):
        self.cursor.execute("SELECT * FROM students")
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()