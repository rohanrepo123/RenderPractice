import pandas as pd
import numpy as np
from  data import model
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import classification_report

from sklearn.preprocessing import OrdinalEncoder
# from sklearn

from flask import Flask, request, jsonify ,render_template
import joblib
import numpy as np
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)  # Allow requests from your HTML page

# Load your saved scikit-learn model
model = joblib.load("model.pkl")
@app.route("/")
def home():
    return render_template('apps.html')

@app.route("/process", methods=["POST"])
def process():
    try:
        data = request.get_json()

        # Extract features from request JSON
        gre = float(data.get("gre"))
        toefl = float(data.get("toefl"))
        university_rating = float(data.get("university_rating"))
        sop = float(data.get("sop"))
        lor = float(data.get("lor"))
        cgpa = float(data.get("cgpa"))
        research = int(data.get("research"))

        # Create feature array for prediction
        features = np.array([[gre, toefl, university_rating, sop, lor, cgpa, research]])

        # Make prediction
        prediction = model.predict(features)[0]

        # Return JSON response
        x= jsonify({"prediction": round(float(prediction), 2)})
        print(x)
        return jsonify({"prediction": round(float(prediction), 2)})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
