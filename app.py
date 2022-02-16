from flask import Flask, request, Response
import dbinteractions as db
import json
import sys

app = Flask(__name__)

# post request
@app.post('/blog')
def post_blog():
    # user input
    username = request.json['username']
    content = request.json['content']

    post_status_message, post_status_code = db.post_blog_db(username, content)

    post_status_message_json = json.dumps(post_status_message, default=str)

    return Response(post_status_message_json, mimetype="plain/text", status=post_status_code)

# get request
@app.get('/blog')
def get_blog():
    blogs = []

    blogs, get_status_code = db.get_blog_db()

    blogs_json = json.dumps(blogs, default=str)

    return Response(blogs_json, mimetype="application/json", status=get_status_code)

# testing/production mode code
if len(sys.argv) > 1:
    mode = sys.argv[1]
else:
    print(
        "You must pass a mode to run this python script. Either 'testing' or 'production'"
    )
    exit()

if mode == "testing":
    from flask_cors import CORS

    CORS(app)
    print("running in testing mode")
    app.run(debug=True)
else:
    print("Invalid mode: Please run using either 'testing' or 'production'")
    exit()
