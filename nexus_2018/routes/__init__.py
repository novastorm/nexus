from app import app

import api

from v0 import _v0_courses_blueprint as _courses_blueprint
from v0 import _v0_react_blueprint as _react_blueprint

app.register_blueprint(_courses_blueprint, url_prefix='/courses')
app.register_blueprint(_react_blueprint, url_prefix='/react')
