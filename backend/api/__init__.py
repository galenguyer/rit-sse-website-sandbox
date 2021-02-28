""" A small flask Hello World """

import os

from flask import Flask, jsonify, session, redirect, url_for
from flask import make_response, request
from authlib.integrations.flask_client import OAuth

APP = Flask(__name__)

# Load file based configuration overrides if present
if os.path.exists(os.path.join(os.getcwd(), 'config.py')):
    APP.config.from_pyfile(os.path.join(os.getcwd(), 'config.py'))
else:
    APP.config.from_pyfile(os.path.join(os.getcwd(), 'config.env.py'))

APP.secret_key = APP.config['SECRET_KEY']

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
