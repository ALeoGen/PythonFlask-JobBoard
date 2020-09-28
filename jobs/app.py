from flask import flask
from flask import render_template

route('/')
route('/jobs')
def jobs():
    render_template('index.html')