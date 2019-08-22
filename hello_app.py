# export FLASK_APP=hello_app.py
# flask run --host=127.0.0.1
# http://127.0.0.1:5000/static/hello.html

from flask import request, jsonify, Flask

app = Flask(__name__)

@app.route('/hello', methods=['POST'])

def hello():
    message = request.get_json(force=True)
    name = message['name']
    response = {'greeting': 'Hello, ' + name }
    print(name)
    return jsonify(response)
