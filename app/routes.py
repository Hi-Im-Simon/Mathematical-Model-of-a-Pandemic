from flask import render_template, redirect, request 
from app import app, db
from app.models import Database
from app.values import init_values


# the main page
@app.route('/', methods=['POST', 'GET'])
def page_default():
    if request.method == 'POST':
        # if submit is pressed, collect data from inputs and add it to the database
        input_values = {}
        for key in init_values.keys():
            input_values[key] = request.form[key]
        data = Database(input_values)

        db.session.add(data)
        db.session.commit()
        # then redirect back to the same page (it also reloads the page)
        return redirect('/')

    else:
        inputs = Database.query
        # add initial values if database is empty
        if len([i for i in Database.query]) > 0:
            initials = inputs[-1]
        else:
            initials = Database(init_values)
            db.session.add(initials)
            db.session.commit()
            
        # or if the page is reloaded, send data to the template and display it
        return render_template(
            'main.html',
            title = 'The main page!',
            inputs = inputs,
            initials = initials,
        )


# clears the database on enter and returns harambe 🐒
@app.route('/clear')
def page_eo():
    db.session.query(Database).delete()
    db.session.commit()
    return 'harambe'
