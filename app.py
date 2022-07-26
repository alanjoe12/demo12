from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('finalH1Bvisamodelnaive.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def home():
    SECONDARY_ENTITY_1 = request.form['SECONDARY_ENTITY_1']
    AGENT_REPRESENTING_EMPLOYER = request.form['AGENT_REPRESENTING_EMPLOYER']
    CONTINUED_EMPLOYMENT = request.form['CONTINUED_EMPLOYMENT']
    CHANGE_PREVIOUS_EMPLOYMENT = request.form['CHANGE_PREVIOUS_EMPLOYMENT']
    NEW_CONCURRENT_EMPLOYMENT = request.form['NEW_CONCURRENT_EMPLOYMENT']
    CHANGE_EMPLOYER = request.form['CHANGE_EMPLOYER']
    AMENDED_PETITION = request.form['AMENDED_PETITION']
    H1B_DEPENDENT = request.form['H1B_DEPENDENT']
    SUPPORT_H1B = request.form['SUPPORT_H1B']
    WILLFUL_VIOLATOR = request.form['WILLFUL_VIOLATOR']
    arr = np.array([[SECONDARY_ENTITY_1, AGENT_REPRESENTING_EMPLOYER, CONTINUED_EMPLOYMENT, CHANGE_PREVIOUS_EMPLOYMENT, NEW_CONCURRENT_EMPLOYMENT, CHANGE_EMPLOYER, AMENDED_PETITION, H1B_DEPENDENT, SUPPORT_H1B, WILLFUL_VIOLATOR]])
    pred = model.predict(arr)
    return render_template('after.html', data=pred)

if __name__ == "__main__":
    app.run(debug=True)