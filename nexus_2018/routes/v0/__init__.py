from app import app

from courses import v0_courses as _v0_courses_blueprint
from react import v0_react as _v0_react_blueprint

app.register_blueprint(_v0_courses_blueprint, url_prefix='/v0/courses')
app.register_blueprint(_v0_react_blueprint, url_prefix='/v0/react')
