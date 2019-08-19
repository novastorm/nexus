from flask import Blueprint
from flask import jsonify

from app.database import Base, DBH

from app.models.course import training_course as Course

api_v0_courses = Blueprint('api_v0_courses', __name__)

@api_v0_courses.route('/')
def api_0_showCourseCollection():
    courseCollection = DBH.query(Course).all()
    # return courseCollection

    return jsonify(
        courseList=[record.serialize for record in courseCollection]
        )
