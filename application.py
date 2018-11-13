from flask import Flask, render_template, request
from nslookup import nameserverlookup

application = Flask(__name__, template_folder='templates')


@application.route('/', methods=['GET'])
@application.route('/lookup', methods=['GET'])
def no_name():
    return render_template('index.html', lookup=None)


@application.route('/lookup', methods=['POST'])
def has_name_lookup():
    name = nameserverlookup(request.form.get('lookUpName'))
    return render_template('index.html', lookup=name)


if __name__ == '__main__':
    application.run()
