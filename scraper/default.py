from flask import Flask
from newspaper import article
app = Flask(__name__)
app.config['DEBUG'] = True



# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""


    return 'Hello World!'


@app.route('proc')
def processArticle:
    art = article(url="http://www.huffingtonpost.com/entry/trump-cut-mortgage-insurance_us_5882765ee4b0e3a73568f0a4")

    art.download()
    art.parse()
    print(art.text)


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404