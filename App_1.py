# App 1 - Flask sample

from flask import Flask
app = Flask(__name__)


@app.route('/sample')
def runnning():
    return 'Flash is running!'