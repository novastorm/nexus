from flask import Blueprint
from flask import jsonify
from flask import render_template

from app.database import Base, DBH

from app.models.course import training_course as Course

v0_react = Blueprint('v0_react', __name__)

@v0_react.route('/')
def v0_showCourseIndex():
    template_file = 'react_index.html'

    return render_template(template_file)
