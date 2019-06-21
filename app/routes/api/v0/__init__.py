from app import app

from courses import api_v0_courses as _api_v0_courses_blueprint

#api_v0 = Blueprint('api_v0', __name__)

app.register_blueprint(_api_v0_courses_blueprint, url_prefix='/api/v0/courses')
