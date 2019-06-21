from flask import Blueprint
from flask import jsonify
from flask import render_template

from app.database import Base, DBH

from app.models.course import training_course as Course

v0_courses = Blueprint('v0_courses', __name__)

@v0_courses.route('/')
def v0_showCourseIndex():
    course_collection = DBH.query(Course).all()

    # return 'Course Index'
    template_file = 'course_index.html'

    return render_template(template_file, title='Course Index', course_collection=course_collection)
