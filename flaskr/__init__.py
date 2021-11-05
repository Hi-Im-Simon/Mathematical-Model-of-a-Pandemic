from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from werkzeug.utils import redirect


# create the app
# instance_relative_config tells the app that configuration files are relative to the instance folder
app = Flask(__name__, instance_relative_config=True)

# configurate the app
# config a database file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# avoid error messages
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create a SQLAlchemy database handler
db = SQLAlchemy(app)


# design a database scheme
class Database(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    input1 = db.Column(db.Integer, nullable=False)
    input2 = db.Column(db.Integer, nullable=False)


# the main page
@app.route('/', methods=['POST', 'GET'])
def page_default():
    if request.method == 'POST':
        # if submit is pressed, collect data from inputs and add it to the database
        data = Database(
            input1 = request.form['input1'],
            input2 = request.form['input2'],
        )

        db.session.add(data)
        db.session.commit()
        # then redirect back to the same page (it also reloads the page)
        return redirect('/')

    else:
        # or if the page is reloaded, send data to the template and display it
        return render_template(
            'main.html',
            title = 'The main page!',
            i1 = Database.query
        )

# additional page, just to make sure subpages work properly
@app.route('/eo')
def page_eo():
    return 'harambe'
