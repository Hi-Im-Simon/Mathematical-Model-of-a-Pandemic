from flask import render_template, redirect, request 
from app import app, db
from app.models import Database


# the main page
@app.route('/', methods=['POST', 'GET'])
def page_default():
    if request.method == 'POST':
        # if submit is pressed, collect data from inputs and add it to the database
        data = Database(
            input1=request.form['input1'],
            input2=request.form['input2'],
        )

        db.session.add(data)
        db.session.commit()
        # then redirect back to the same page (it also reloads the page)
        return redirect('/')

    else:
        # or if the page is reloaded, send data to the template and display it
        return render_template(
            'main.html',
            title='The main page!',
            i1=Database.query
        )


# additional page, just to make sure subpages work properly
@app.route('/eo')
def page_eo():
    return 'harambe'
