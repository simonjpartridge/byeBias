from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

from scraper import default

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.route('/proc')
def lala():
    return "proc"


@app.route('/defa')
def fghrghfh():
    return default.return_yo()


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
