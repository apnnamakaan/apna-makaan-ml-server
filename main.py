from flask import Flask, jsonify,request
import os
import ml

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"status": "true","author":"Atanu Debnath","about":"house price predicit api"})

@app.route('/predict')
def predect():
    estimate = ml.predict(request)
    return jsonify({"estimate": estimate})
  
if __name__ == '__main__':
    app.run(debug=False,host='127.0.0.1', port=os.getenv("PORT", default=8082))
