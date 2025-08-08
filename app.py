from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json
import os

app = Flask(__name__)
app.secret_key = "secret-key"

TOTAL_STEPS = 3
RESPONSES_FILE = 'responses.json'

 # function to calculate bar progress
def progress_percent(step):
    return int((step / TOTAL_STEPS) * 100)

# function for testing if data retrieves to json file
def save_response(new_data):
    responses = []
    if os.path.exists(RESPONSES_FILE):
        with open(RESPONSES_FILE, 'r') as file:
            try:
                responses = json.load(file)
            except json.JSONDecodeError:
                responses = []
    responses.append(new_data)
    with open(RESPONSES_FILE, 'w') as file:
        json.dump(responses, file, indent=4)

@app.route('/')
def index():
    return redirect(url_for('landing'))

@app.route('/step1', methods=['GET', 'POST'])
def step1():
    if request.method == 'POST':
        session['income'] = request.form['income']
        return redirect(url_for('step2'))
    progress = progress_percent(1)
    return render_template('step1.html', step=1, progress=progress, title="Income Range", 
                           question="Select your income range:", 
                           options=[
                               ("<20k", "Less than $20,000"),
                               ("20k-40k", "$20,000 - $40,000"),
                               ("40k-80k", "$40,000 - $80,000"),
                               (">80k", "More than $80,000")
                           ],
                           name="income")

@app.route('/step2', methods=['GET', 'POST'])
def step2():
    if request.method == 'POST':
        session['employment'] = request.form['employment']
        return redirect(url_for('step3'))
    progress = progress_percent(2)
    return render_template('step1.html', step=2, progress=progress, title="Employment Status",
                           question="Select your employment status:",
                           options=[
                               ("full-time", "Full Time"),
                               ("part-time", "Part Time"),
                               ("self-employed", "Self-Employed"),
                               ("retired", "Retired"),
                               ("other", "Other"),
                           ],
                           name="employment")

@app.route('/step3', methods=['GET', 'POST'])
def step3():
    if request.method == 'POST':
        session['phone'] = request.form['phone']
        data = {
            "income": session.get('income'),
            "employment": session.get('employment'),
            "phone": session.get('phone')
        }
        save_response(data)
        session.clear()
        return redirect(url_for('success'))

    progress = progress_percent(3)
    return render_template('step3.html', step=3, progress=progress)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/google')
def google_redirect():
    return redirect("https://www.google.com", code=302)

@app.route('/landing')
def landing():
    return render_template('landing.html')

@app.route('/api/survey', methods=['POST'])
def api_survey():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON received"}), 400

    required_keys = ['income', 'employment', 'phone']
    if not all(key in data for key in required_keys):
        return jsonify({"error": "Missing keys"}), 400

    save_response(data) 

    return jsonify({"message": "Survey saved successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)