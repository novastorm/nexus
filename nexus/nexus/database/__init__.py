from sqlite3 import dbapi2 as sqlite3
from flask import Blueprint, request, session, g, redirect, url_for, abort, \
    render_template, flash, current_app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db():
    '''Connect to specified database.'''
    return db


def init_db():
    '''Initialize database'''
    db = get_db()
    db.create_all()


def get_db():
    '''Open new database connection if ones does not exist in current
    application context.
    '''
    if not hasattr(g, '_database'):
        g._database = connect_db()
    return g._database
    