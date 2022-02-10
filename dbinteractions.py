import mariadb as db
import dbcreds as c

# connect to database function
def connect_db():
    conn = None
    cursor = None
    try:
        conn = db.connect(user=c.user,
                          password=c.password,
                          host=c.host,
                          port=c.port,
                          database=c.database)
        cursor = conn.cursor()
    except db.OperationalError:
        print("something went wrong with the DB, please try again in 5 minutes")
    except Exception:
        print("DB Connection Error: General error message")
    return conn, cursor  

# disconnect from database function
def disconnect_db(conn, cursor):
    try:
        cursor.close()
    except Exception:
        print("DB Cursor Close Error: General error message")

    try:
        conn.close()
    except Exception:
        print("DB Connection Close Error: General error message")
