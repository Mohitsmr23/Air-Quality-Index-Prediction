
from flask import Flask, jsonify, request
from sklearn.externals import joblib
import numpy as np


app = Flask(__name__)


@app.route("/")
def hello():
    posted_data = request.get_json()
    a = posted_data['a']#('a', type = float)
    b = posted_data['b']
    c = posted_data['c']
    d = posted_data['d']
    e = posted_data['e']
    model = joblib.load('DL.model')

    prediction =str(model.predict(np.array([[a,b,c,d,e]])))
    return jsonify({'Prediction': prediction})
    


if __name__ == '__main__':
    app.run(debug=True)
