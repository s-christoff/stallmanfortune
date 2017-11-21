Stallman Fortune Cookie:

Generates a Stallman quote, deployed on Heroku

[ X ] Create a Flask App that returns Stallman Quote and image of Stallman

[ X ] Deploy to Heroku

[ ] Refactor?


Steps:

Created a list of quotes and stored them in `quotes.py`.

Created `app.py` to initialize flask and piped random quote into the index.html by generating in the `html_please` function.

Making use of jinja2 that Flask has, called that variable.

Created runtime.txt which specifies Python runtime, requirements.txt which specifies what the application needs to run, and Procfile which is the execution command all for Heroku.

Followed Heroku command line steps.

[Success](https://stallmanfortune.herokuapp.com/)!

