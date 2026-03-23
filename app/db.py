import psycopg2
from datetime import datetime, timedelta

def get_connection():
    conn = psycopg2.connect(
        dbname="face_attendance",
        user="postgres",
        password="244466666",
        host="localhost",
        port="5432"
    )
    return conn


def insert_attendance(employee_name):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO attendance_logs (employee_name)
        VALUES (%s)
        """,
        (employee_name,)
    )

    conn.commit()
    cur.close()
    conn.close()

def get_all_logs():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT employee_name, checkin_time
        FROM attendance_logs
        ORDER BY checkin_time DESC
    """)

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows


def is_recently_checked_in(employee_name, seconds=60):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT checkin_time
        FROM attendance_logs
        WHERE employee_name = %s
        ORDER BY checkin_time DESC
        LIMIT 1
    """, (employee_name,))

    result = cur.fetchone()

    cur.close()
    conn.close()

    if result is None:
        return False

    last_time = result[0]
    now = datetime.now()

    diff = (now - last_time).total_seconds()

    return diff < seconds