from app import app

from v0 import _api_v0_courses_blueprint as _api_courses_blueprint

#api_v0 = Blueprint('api_v0', __name__)

app.register_blueprint(_api_courses_blueprint, url_prefix='/api/courses')
