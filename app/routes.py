from flask import render_template, redirect, request 
from app import app, db
from app.models import Database
#import init_values


# the main page
@app.route('/', methods=['POST', 'GET'])
def page_default():
    if request.method == 'POST':
        # if submit is pressed, collect data from inputs and add it to the database
        data = Database(
            mask_rate = request.form['mask_rate'],
            mask_fall_rate = request.form['mask_fall_rate'],
        )

        db.session.add(data)
        db.session.commit()
        # then redirect back to the same page (it also reloads the page)
        return redirect('/')

    else:
        # add initial values if database is empty
        if len([i for i in Database.query]) > 0:
            initials = Database.query[-1]
        else:
            initials = Database(
                # initial values declared here
                mask_rate=0.1,
                mask_fall_rate=0.5,
            )
            db.session.add(initials)
            db.session.commit()
        
        # or if the page is reloaded, send data to the template and display it
        return render_template(
            'main.html',
            title='The main page!',
            keys=Database.__table__.columns.keys(),
            inputs=Database.query,
            initials=initials
        )


# clears the database on enter and returns harambe 🐒
@app.route('/clear')
def page_eo():
    db.session.query(Database).delete()
    db.session.commit()
    return 'harambe'
