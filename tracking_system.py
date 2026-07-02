from db_manager import DBManager
import datetime
import tkinter as tk
import random
import email_operations as eop

today = datetime.date.today()

class TrackingSystem:
    db = None
    cursor = None

    # Attempts to connect to database and returns error if connection is unsuccessful
    @classmethod
    def connect_db(cls):
        try:
            cls.db = DBManager("Student Behaviour Tracker")
            cls.cursor = cls.db.get_cursor()
            print("Connected to database successfully.")
        except Exception as e:
            print(f"Error connecting to database: {e}")

    # Fetches all student records from the DB table
    @classmethod
    def get_all_records(cls):
        cls.cursor.execute("SELECT * FROM records ORDER BY \"ID\" ASC")
        records = cls.cursor.fetchall()
        return records
    
    @classmethod
    def generate_random_id(cls):
        existing_ids = [record["ID"] for record in cls.get_all_records()]
        print(existing_ids)
        if existing_ids:
            top_id = existing_ids[-1]
            print(top_id)
            if top_id != "#9999":
                new_id = f'#{int(top_id[1:])+1: 05}'.replace(" ", "")
                return new_id
        return "#0001"

    @classmethod
    def add_student_record(cls, student_name, type, reason, date, achievements, behaviours):
        record_id = cls.generate_random_id()
        date = datetime.datetime.strptime(date.entry.get(), "%d/%m/%Y")
        cls.cursor.execute(
            """
            INSERT INTO records (
                "ID", student_name, type, reason, date, achievement_points, behaviour_points, conduct_points
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (record_id, student_name, type, reason, date, int(achievements), int(behaviours), int(achievements)-int(behaviours))
        )