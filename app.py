from flask import Flask, request
import ml

app=Flask(__name__)

@app.route('/')
def home():
    return {"status": "true","author":"Atanu Debnath","about":"house price predicit api"}

@app.route('/predict')
def predic():
    city = str(request.args.get('city'))
    area = float(request.args.get('area'))
    bed = int(request.args.get('bed'))
    bath = int(request.args.get('bath'))
    garage =  int(request.args.get('garage'))

    return {"estimate" : ml.predict(city,area,bed,bath,garage)}

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8082)