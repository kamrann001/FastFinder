from flask import Flask
from FlaskProject2.BusinessLayer.tapazDisplayer import displayTapaz
from FlaskProject2.BusinessLayer.amazonDisplayer import displayAmazon

app = Flask(__name__)

from FlaskProject2 import routes