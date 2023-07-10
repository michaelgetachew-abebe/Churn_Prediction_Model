from flask import Flask, request, jsonify
import pickle
import pandas as pd
from io import StringIO

app = Flask(__name__)

with open('../../notebooks/tracked/model.pkl', "rb") as f_in:
    model = pickle.load(f_in)

with open('../../notebooks/tracked/preprocessor.b', "rb") as f_in:
    dv = pickle.load(f_in)

@app.route("/predict", methods=["POST"])
def predict():
    # Load the CSV data from the request
    csv_data = request.data.decode("utf-8")
    df = pd.read_csv(StringIO(csv_data))

    # Apply the dictionary vectorizer over the dataset
    X_vectorized = dv(df)

    # Use the model to make the predictions
    predictions = model.predict(X_vectorized)

    # Return the prediction as a JSON response
    predictions = {"predictions": predictions.tolist()}

    return jsonify(predictions)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
