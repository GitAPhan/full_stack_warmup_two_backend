from sqlite3 import Cursor
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


# get request from db
def get_blog_db():
    conn, cursor = connect_db()
    blogs = None
    status_code = 400

    try:
        cursor.execute("select id, content, username, created_at from post")
        blogs = cursor.fetchall()

        status_code = 200
    except:
        print('GET db error')

    disconnect_db(conn, cursor)

    return blogs, status_code

# post request from db
def post_blog_db(username, content):
    conn, cursor = connect_db()
    status_message = "Post db error"
    status_code = 400

    try:
        cursor.execute("insert into post (content, username) values (?,?)", [content, username])
        conn.commit()

        status_message = 'post success message'
        status_code = 200
    except:
        print('POST db error')

    disconnect_db(conn, cursor)

    return status_message, status_code
