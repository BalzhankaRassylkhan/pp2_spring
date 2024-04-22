import psycopg2
from config import load_config

def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except psycopg2.DatabaseError as db_error:
        print("Database error:", db_error)
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    try:
        config = load_config()
        connect(config)
    except Exception as e:
        print("Error:", e)
