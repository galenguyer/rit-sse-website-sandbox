""" A small flask Hello World """

import os
import logging

from flask import Flask, jsonify, session, redirect, url_for
from flask import make_response, request
from flask_sqlalchemy import SQLAlchemy
from authlib.integrations.flask_client import OAuth

APP = Flask(__name__)

# Load default configuration and any environment variable overrides
_root_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
APP.config.from_pyfile(os.path.join(_root_dir, 'config.env.py'))

# Load file based configuration overrides if present
_pyfile_config = os.path.join(_root_dir, 'config.py')
if os.path.exists(_pyfile_config):
    APP.config.from_pyfile(_pyfile_config)

# Logger configuration
logging.getLogger().setLevel(APP.config['LOG_LEVEL'])
logging.getLogger().info('Launching rit-sse-api')

db = SQLAlchemy(APP)
logging.getLogger().info('SQLAlchemy pointed at ' + repr(db.engine.url))

from . import models
from .models import Link, Quote

db.create_all()

oauth = OAuth(APP)
oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'email'
    }
)

@APP.route('/api/v0/user')
def _get_api_v0_user():
    user = session.get('user')
    return jsonify(user)


@APP.route('/api/v0/login')
def _get_api_v0_login():
    redirect_uri = url_for('_get_api_v0_callback', _external=True)
    session['redirect'] = request.args.get('redirect')
    return oauth.google.authorize_redirect(redirect_uri)

@APP.route('/api/v0/callback')
def _get_api_v0_callback():
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token)
    session['user'] = user
    resp = make_response(redirect(session['redirect'] if session['redirect'] is not None else '/'))
    session.pop('redirect')
    resp.set_cookie('email', user['email'])
    return resp

@APP.route('/api/v0/golinks')
def _get_api_v0_golinks():
    return jsonify([link.to_dict() for link in Link.get_all()])

@APP.route('/api/v0/quotes')
def _get_api_v0_quotes():
    return jsonify([quote.to_dict() for quote in Quote.get_all()])
