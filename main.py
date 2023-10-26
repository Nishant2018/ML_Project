from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__,static_folder='static')

# Load your trained machine learning model (replace 'your_model.pkl' with the actual model file)
model = joblib.load('my_model.pkl')

@app.route('/',methods=["GET"])
def home():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from the form
    studytime = float(request.form['studytime'])
    Medu = float(request.form['Medu'])
    higher = request.form['higher']
    failures = float(request.form['failures'])
    G1 = float(request.form['G1'])
    G2 = float(request.form['G2'])

    # Create a DataFrame with the input data
    input_data = pd.DataFrame({
        'studytime': [studytime],
        'Medu': [Medu],
        'higher': [higher],
        'failures': [failures],
        'G1': [G1],
        'G2': [G2]
    })

    # Make predictions using the model
    prediction = model.predict(input_data)

    return render_template('index.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
