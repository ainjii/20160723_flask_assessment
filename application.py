from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index_page():
    """Show an index page."""

    return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route("/application")
def application_page():
    return render_template('application-form.html')

@app.route("/application_response", methods=["POST"])
def application_received():
    first = request.form.get('firstname', None)
    last = request.form.get('lastname', None)
    position = request.form.get('position', None)
    salary = request.form.get('salary', 0)

    return render_template('application-response.html',
                           first=first,
                           last=last,
                           position=position,
                           salary=salary)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
