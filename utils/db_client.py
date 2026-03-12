import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

class DBClient:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        self.cursor = self.conn.cursor()

    def get_all_bookings(self):
        self.cursor.execute("SELECT * FROM bookings")
        return self.cursor.fetchall()

    def get_booking_by_id(self, booking_id: int):
        self.cursor.execute(
            "SELECT * FROM bookings WHERE id = %s",
            (booking_id,)
        )
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()