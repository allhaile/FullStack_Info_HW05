# Importing flask library
from app import app
from flask import Flask, redirect, make_response, render_template, url_for, session, request, escape, flash
import os
app.secret_key = os.environ.get('SECRET_KEY') or 'hard to guess string'

@app.route('/')
@app.route('/index')
def index():
    username = ''
    if 'username' in session:
        username = session['username']
        return render_template('survey.html', name=username)
    else:
        return render_template('login.html')

    # if (): #check if the user is already in session, if so, direct the user to survey.html Hint: render_template with a variable

@app.route('/login', methods =['GET','POST']) # You need to specify something here for the function to get requests
def login():
    # Here, you need to have logic like if there's a post request method, store the username and email from the form into
    if request.method == 'POST':
        session['username'] = request.form['username']
        username = session['username']

        session['email'] = request.form['email']
        return render_template('survey.html', name=username)
    else:
    # session dictionary
        return render_template('index.html')

@app.route('/logout')
def logout():
	session.pop('username', None)
	session.pop('email', None)
	return redirect(url_for('index'))

@app.route('/submit-survey', methods=['GET', 'POST'])
def submitSurvey():
    username = ''
    email = ''
    if 'username' in session: #check if user in session
        username = session.get('username')
        surveyResponse = {}
        surveyResponse['food'] = request.form.get('food')
        surveyResponse['color'] = request.form.get('color')
        surveyResponse['vacation'] = request.form.get('vacation')

        surveyResponse['fe-before'] = request.form.get('feBefore')
        surveyResponse['fe-after'] = request.form.get('feAfter')

        if surveyResponse['fe-after'] < surveyResponse['fe-before']:
            surveyResponse['results'] = "Bummer, not much improvement. No worries let's keep learning!"
        else:
            surveyResponse['results'] = "Awesome! You've improved! Let's keep learning!"
        return render_template('results.html', surveyResponse=surveyResponse, name=username) # pass in variables to the template
    else:
        return render_template('login.html')

@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404
