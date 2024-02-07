import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def create_database(dbname, user, password, host='localhost'):
    try:
        # Connect to the default 'postgres' database to create a new database
        conn = psycopg2.connect(dbname='postgres', user=user, password=password, host=host)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        cursor = conn.cursor()
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(dbname)))
        cursor.close()
        conn.close()

        print(f"Database '{dbname}' created successfully.")
    except Exception as e:
        print(f"Error creating database: {e}")

def connect_database(dbname, user, password, host='localhost'):
    try:
        # Connect to the database
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
        print(f"Connected to database '{dbname}' successfully.")
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None
