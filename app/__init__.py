import os
import sys
from os.path import dirname, normpath, pardir, realpath
from flask import Flask, request

from flask import render_template

app = Flask(__name__)

#import routes

@app.route('/home')
def showHome():
    return 'Nexus Home'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def showDefault(path):
    template_file = 'react_index.html'

    baseURL = ""

    if request.script_root != "":
        baseURL = normpath(os.path.join(request.script_root, pardir))

    if baseURL == "/":
        baseURL = ""

    return render_template(template_file, baseURL=baseURL)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
