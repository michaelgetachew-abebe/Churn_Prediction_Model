from flask import Flask, request, jsonify
import pickle
import pandas as pd
from sklearn.feature_extraction import DictVectorizer

app = Flask(__name__)

with open('../../notebooks/tracked/model.pkl', "rb") as f_in:
    model = pickle.load(f_in)

# with open('../../notebooks/tracked/preprocessor.b', "rb") as f_in:
#     dv = pickle.load(f_in)

@app.route("/predict", methods=["POST"])
def predict():
    json_data = request.get_json()

    df = pd.read_json(json_data)
    # Apply the dictionary vectorizer over the dataset
    # dv = DictVectorizer(sparse=False)
    # X_vectorized = dv.transform(df)

    # Use the model to make the predictions
    predictions = model.predict(df)

    # Return the prediction as a JSON response
    predictions = {"predictions": predictions.tolist()}

    return jsonify(predictions)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
