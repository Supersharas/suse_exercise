
import json

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

@app.route("/status")
def status():
    return json.dumps({'user':'admin', 'result':'OK - healthy'})

@app.route("/metrics")
def metrics():
    user_count = 140
    user_count_active = 60
    return json.dumps({'user':'admin', 'data':{"UserCount": user_count, "UserCountActive": user_count_active}})
