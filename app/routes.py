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
        # add initial values to the database if it's empty
        if len([i for i in Database.query]) == 0:
            db.session.add(Database(init_values))
            db.session.commit()
            
        values = inputs[-1].__dict__
        names = eval('{' + ''.join([line.strip() for line in open('app/static/javascript/translation.js').readlines()][2:-3]) + '}')

            
        # or if the page is reloaded, send data to the template and display it
        return render_template(
            'main.html',
            values = values,
            names = names,
            language = 'EN',
        )


# clears the database on enter
@app.route('/clear')
def page_eo():
    db.session.query(Database).delete()
    db.session.commit()
    # also empty a chart file
    open('app/templates/chart.html', 'w+').close()
    return redirect('/')
