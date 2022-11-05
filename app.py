from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import  stories
from random import choice

app = Flask(__name__)
app.config['SECRET_KEY'] = "do*not*tell"

debug = DebugToolbarExtension(app)

story = choice(stories)

@app.route('/')
@app.route('/get_mad')
def get_mad():
    prompts = story.prompts
    return render_template("story_form.html", prompts = prompts)

@app.route('/go_mad')
def go_mad():
    text = story.generate(request.args)
    return render_template("story_mad.html", gone_mad = text)