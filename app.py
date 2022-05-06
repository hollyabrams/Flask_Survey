from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET-KEY'] = 'secret'

debug = DebugToolbarExtension(app)

