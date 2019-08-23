# App 1 - Flask sample

# export FLASK_APP=App_1.py
# flask run --host=127.0.0.1
# localhost:5000/sample

from flask import Flask
app = Flask(__name__)


@app.route('/sample')
def runnning():
    return 'Flash is running!'
