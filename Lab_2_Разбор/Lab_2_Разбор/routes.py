"""
Routes and views for the bottle application.
"""

from bottle import route, view, template
from datetime import datetime

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""    
    year=datetime.now().year
    return template('index.tpl',year=year, message ="Write to us!")
    

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )
