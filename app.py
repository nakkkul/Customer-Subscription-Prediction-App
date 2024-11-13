from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
with open('XgBmodel.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    age = int(request.form['age'])
    default = 1 if request.form['default'] == 'yes' else 0
    balance = float(request.form['balance'])
    house_loan = 1 if request.form['house_loan'] == 'yes' else 0
    pers_loan = 1 if request.form['pers_loan'] == 'yes' else 0
    last_contact_month = int(request.form['last_contact_month'])
    contact_duration = float(request.form['contact_duration'])
    campaign = int(request.form['campaign'])
    passed_days = float(request.form['passed_days'])
    previous_days = float(request.form['previous_days'])

    # One-hot encoding for job categories
    job_options = ['blue-collar', 'entrepreneur', 'housemaid', 'management', 'retired', 
                   'self-employed', 'services', 'student', 'technician', 'unemployed', 'unknown']
    job_input = request.form['job']
    job_encoded = [1 if job_input == job else 0 for job in job_options]

    # One-hot encoding for marital status
    marital_status_options = ['married', 'single', 'divorced']
    marital_status_input = request.form['marital_status']
    marital_encoded = [
        1 if marital_status_input == 'married' else 0,
        1 if marital_status_input == 'single' else 0,
        1 if marital_status_input == 'divorced' else 0,  # Added "divorced" encoding
    ]

    # One-hot encoding for education level
    education_options = ['primary', 'secondary', 'tertiary', 'unknown']
    education_input = request.form['education']
    education_encoded = [
        1 if education_input == 'secondary' else 0,
        1 if education_input == 'tertiary' else 0,
        1 if education_input == 'unknown' else 0,
    ]

    # One-hot encoding for contact type
    contact_options = ['unknown', 'cellular', 'telephone']
    contact_input = request.form['contact']
    contact_encoded = [
        1 if contact_input == 'telephone' else 0,
        1 if contact_input == 'unknown' else 0,
    ]

    # One-hot encoding for previous outcome
    prev_out_come_options = ['unknown', 'failure', 'other', 'success']
    prev_out_come_input = request.form['prev_out_come']
    prev_out_come_encoded = [
        1 if prev_out_come_input == 'other' else 0,
        1 if prev_out_come_input == 'success' else 0,
        1 if prev_out_come_input == 'unknown' else 0,
    ]

    # Combine all features
    features = [
        age, default, balance, house_loan, pers_loan, last_contact_month,
        contact_duration, campaign, passed_days, previous_days
    ] + job_encoded + marital_encoded + education_encoded + contact_encoded + prev_out_come_encoded
    
    # Reshape for prediction
    input_data = np.array(features).reshape(1, -1)

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Return result
    result = 'Subscribed' if prediction == 1 else 'Not Subscribed'
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
