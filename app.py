from flask import Flask, render_template
from quotes import quotiebois
import randomFlask
gunicorn

app = Flask(__name__)

@app.route('/')
def html_please():
    stallquote = quotiebois[random.randint(0,5)]
    return render_template('index.html', quote = stallquote )

