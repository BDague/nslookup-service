from flask import Flask, jsonify, render_template, request, make_response, abort
from nslookup import nameserverlookup
from database import DatabaseInterface

data = DatabaseInterface()

application = Flask(__name__, template_folder='templates')


@application.route('/', methods=['GET'])
def no_name():
    return render_template('index.html', lookup=None, looked=data.table)


@application.route('/', methods=['POST'])
def has_name_lookup():
    name = request.form.get('lookUpName')
    #If we already looked up the name, just pull it out of the cache.
    if name in data.table:
        return render_template('index.html', lookup=data.table[name], looked=data.table)

    #Otherwise do a real lookup and add it to the database for later
    address = nameserverlookup(name) 
    data.add(address)
    return render_template('index.html', lookup=address, looked=data.table)

@application.route('/lookup', methods=['GET'])
def get_names():
    return jsonify(data.table)

@application.route('/lookup/<name>', methods=['GET'])
def get_name(name):
    info = jsonify([address for address in data.table if address['name'] == name])

    if not info:
        abort(404)

    return info

@application.route('/lookup/<name>', methods=['POST'])
def post_name(name):
    new_lookup =  nameserverlookup(name)
    data.add(new_lookup)
    return jsonify(new_lookup), 201

@application.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': "Not found."}), 404)

@application.route('/lookup/<site>', methods=['DELETE'])
def remove_from_cache(site):
    data.remove(site)
    return render_template('index.html', lookup=None, looked=data.table)
    

if __name__ == '__main__':
    application.run()
