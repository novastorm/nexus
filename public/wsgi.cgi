#!/home/mfd/project/4mfd-webapp/.venv/bin/python
#!/usr/bin/python
import os
import sys
from os.path import realpath, dirname, pardir

environment_path = os.path.abspath(os.path.join(dirname(realpath(__file__)), pardir))
sys.path.append(environment_path)

from wsgiref.handlers import CGIHandler

activate_this = ('%s/%s' % (environment_path, '.venv/bin/activate_this.py'))
with open(activate_this) as f:
    exec(f.read(), {'__file__': activate_this})

from app import app

app.secret_key = '\xf3L\xf6\xda\x88J\x04\xf8}\x15\xe1\xbfF\x8dI\x9e\x05\xc8q\xa2T\x14\x06a'

CGIHandler().run(app)

