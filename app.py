from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)

app.config["SECRET_KEY"] = 'whateverpassword'
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

@app.route('/')
def madlibs_form():
    return render_template('form.html')

@app.route('/your_story')
def your_story():
    place = request.args.get("place")
    noun = request.args.get("noun")
    verb = request.args.get("verb")
    adj = request.args.get("adjective")
    plur = request.args.get("plural_noun")
    ans = {
        "place":place,
        "noun":noun,
        "verb":verb,
        "adjective":adj,
        "plural_noun": plur
    }
    text = story.generate(ans)
    print(text)
    return render_template('story.html',story=text)