from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


# YOUR ROUTES GO HERE
@app.route('/')
def homepage():
    """Return homepage."""
    return render_template("index.html")


@app.route('/application-form')
def application():
    position_list = ["Software Engineer", "QA Engineer", "Product Manager"]

    answer_yes = request.args.get("yes")
    # print request.args
    answer_no = request.args.get("no")
    if answer_yes:
        return render_template("application-response.html", position_list=position_list)
    if answer_no:
        return render_template("goodbye.html")


@app.route('/application-success', methods = ['POST'])
def success():
    firstname = request.form.get("firstname")
    print firstname
    lastname = request.form.get("lastname")
    salary = request.form.get("salary")
    position = request.form.get("position")
    return render_template("submission.html", firstname=firstname, lastname=lastname, salary=salary, position=position)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
