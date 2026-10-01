import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    connection = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
    )
    return connection

def load_record(conn, record: dict, snapshot_time: int) -> None:
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO sin_flight_snapshots (icao24, callsign, longitude, latitude, altitude, snapshot_time, phase)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (icao24, snapshot_time) DO NOTHING
        """,
        (
            record["icao24"],
            record["callsign"],
            record["longitude"],
            record["latitude"],
            record["altitude"],
            snapshot_time,
            record["phase"],
        )
    )
    conn.commit()