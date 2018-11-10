from flask import Flask, render_template, request
from nslookup import nameserverlookup

app = Flask(__name__, template_folder = 'templates')

@app.route('/lookup', methods=['GET']) 
def no_name():
    return render_template( 'index.html', lookup=None)

@app.route('/lookup', methods=['POST'])
def has_name_lookup():
    name = nameserverlookup(request.form.get('lookUpName'))
    return render_template('index.html', lookup=name)
