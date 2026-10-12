from flask import Flask, request, render_template
import pickle

import numpy as np

app = Flask(__name__, template_folder='./templates', static_folder='./static')

Pkl_Filename = "rf_tuned.pkl"
with open(Pkl_Filename, 'rb') as file:
    model = pickle.load(file)

@app.route('/')

def hello_world():
    return render_template('home.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    try:
        age = int(request.form['age'])
        gender = int(request.form['Gender'])
        bmi = float(request.form['bmi'])
        children = int(request.form['children'])
        smoker = int(request.form['smoker'])
        region_ui = int(request.form['region'])
    except (KeyError, ValueError, TypeError):
        return render_template('op.html', pred='Please check your inputs: Age and BMI must be numbers, Children a whole number, and Gender, Smoker and Region must be chosen from the dropdowns.')

    if not (0 <= age <= 120) or not (10 <= bmi <= 60) or not (0 <= children <= 10) or gender not in (0, 1) or smoker not in (0, 1) or region_ui not in (0, 1, 2, 3):
        return render_template('op.html', pred='Please enter realistic values: Age 0-120, BMI 10-60, Children 0-10, and valid Gender / Smoker / Region options.')

    # Map dropdown values to the model's training encoding
    # (model was trained with: sex male=0/female=1; region northwest=0/northeast=1/southeast=2/southwest=3)
    sex = 1 if gender == 0 else 0
    region = {0: 1, 1: 0, 2: 2, 3: 3}[region_ui]

    features = np.array([[age, sex, bmi, children, smoker, region]])
    print(features)
    pred = model.predict(features)[0]
    print(pred)

    if pred < 0:
        return render_template('op.html', pred='Error calculating Amount!')
    else:
        return render_template('op.html', pred='Expected amount is {0:.3f}'.format(pred))

if __name__ == '__main__':
    app.run(debug=True)
