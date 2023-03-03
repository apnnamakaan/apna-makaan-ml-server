from flask import Flask, jsonify,request
from flask_mysqldb import MySQL
import os

import db
import ml

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_PORT'] = 6227
app.config['MYSQL_USER']= os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD']= os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB']= os.getenv('MYSQL_DB')
app.config["MYSQL_CURSORCLASS"] = os.getenv('MYSQL_CURSORCLASS')

mysql = MySQL(app)


@app.route('/')
def index():
    return jsonify({"status": "true","author":"Atanu Debnath","about":"house price predicit api"})

@app.route('/predict')
def predect():
    estimate = ml.predict(request)
    return jsonify({"estimate": estimate})
  
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0' port=os.getenv("PORT", default=8082))
