
import os
import sys

from os.path import abspath, dirname, pardir

# environment_path = abspath(os.path.join(dirname(__file__), pardir))
environment_path = os.path.join(dirname(__file__))
sys.path.append(environment_path)

from nexus.factory import create_app

if __name__ == '__main__':
    app = create_app()

    # app.secret_key = 'super_secret_key'
    # app.debug = True
    app.run(host='0.0.0.0', port=5000)

