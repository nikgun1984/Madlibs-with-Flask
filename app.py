from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import tales

app = Flask(__name__)

app.config["SECRET_KEY"] = 'whateverpassword'
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

@app.route('/')
def main_page():
    return render_template('main.html')

@app.route('/create_story')
def create_story():
    return render_template('create_story.html')

@app.route('/choose_story')
def madlibs_select():
    titles = tales
    return render_template('index.html', titles=titles)

@app.route('/form')
def madlibs_form():
    val = request.args.get('story')
    words = tales[int(val)].prompts
    return render_template('form.html',words=words, val=val)

@app.route('/your_story/<int:val>')
def your_story(val):
    text = tales[val].generate(request.args)
    return render_template('story.html',story=text)