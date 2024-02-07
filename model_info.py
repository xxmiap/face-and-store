import psycopg2
from psycopg2 import sql

def create_tables(conn):
    cursor = conn.cursor()

    # Create 'faces' table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS faces (
        id SERIAL PRIMARY KEY,
        image_path TEXT NOT NULL,
        name TEXT
    )
    """)

    # Create 'conversations' table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversations (
        id SERIAL PRIMARY KEY,
        face_id INTEGER REFERENCES faces(id),
        conversation TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    cursor.close()
    print("Tables created successfully.")

def init_db(dbname, user, password, host='localhost'):
    from db_config import create_database, connect_database

    # Create the database
    create_database(dbname, user, password, host)

    # Connect to the newly created database
    conn = connect_database(dbname, user, password, host)
    if conn:
        # Create tables
        create_tables(conn)
        conn.close()
