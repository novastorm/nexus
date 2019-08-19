
import os
import sys
from os.path import dirname, normpath, pardir, realpath

from sqlite3 import dbapi2 as sqlite3
from flask import Blueprint, request, session, g, redirect, url_for, abort, \
    render_template, flash, current_app

bp = Blueprint('misc', __name__)

@bp.route('/', defaults={'path': ''})
@bp.route('/<path:path>')
def showHome(path):
    return 'Nexus Home'


@bp.route('/react')
def showReact():
    template_file = 'react_index.html'

    baseURL = ""

    if request.script_root != "":
        baseURL = normpath(os.path.join(request.script_root, pardir))

    if baseURL == "/":
        baseURL = ""

    return render_template(template_file, baseURL=baseURL)
