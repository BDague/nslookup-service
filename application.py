from flask import Flask, render_template, request
from nslookup import nameserverlookup
from database import DatabaseInterface

data = DatabaseInterface()

application = Flask(__name__, template_folder='templates')


@application.route('/', methods=['GET'])
@application.route('/lookup', methods=['GET'])
def no_name():
    return render_template('index.html', lookup=None, looked=data.table)


@application.route('/lookup', methods=['POST', 'PUT'])
def has_name_lookup():
    name = request.form.get('lookUpName')
    #If we already looked up the name, just pull it out of the cache.
    if name in data.table:
        return render_template('index.html', lookup=data.table[name], looked=data.table)

    #Otherwise do a real lookup and add it to the database for later
    address = nameserverlookup(name) 
    data.add(name, address)
    return render_template('index.html', lookup=address, looked=data.table)

@application.route('/lookup/<site>', methods=['DELETE'])
def remove_from_cache(site):
    data.remove(site)
    return render_template('index.html', lookup=None, looked=data.table)
    

if __name__ == '__main__':
    application.run()
