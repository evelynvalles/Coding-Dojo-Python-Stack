from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.surveys import Survey

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def process():
    if Survey.is_valid(request.form):
        Survey.save(request.form)
        return redirect('/result')
    return redirect('/')

@app.route('/result')
def results():
    survey = Survey.get_last_survey()
    print(survey)
    return render_template('result.html', survey=survey)