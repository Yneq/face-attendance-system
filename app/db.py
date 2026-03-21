import psycopg2


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