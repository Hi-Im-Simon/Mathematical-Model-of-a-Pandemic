import os

from flask import render_template, redirect, request 
from app import app, db
from app.models import Database
from app.values import init_values


# the main page
@app.route('/', methods=['POST', 'GET'])
def page_default():
    # to make sure that the language.js file exists
    if not os.path.isfile('app/static/javascript/_language.js'):
        open('app/static/javascript/_language.js', 'w+', encoding='utf-8').write(f"var chosen_language = 'EN';")
    if request.method == 'POST':
        # if submit in the language form is pressed, change the value in the language.js file
        if 'language' in request.form:
            open('app/static/javascript/_language.js', 'w', encoding='utf-8').write(f"var chosen_language = '{ request.form['language'] }';")
        else:
            # if submit in the main form is pressed, collect data from inputs and add it to the database
            input_values = {}
            for key in init_values.keys():
                input_values[key] = request.form[key]
            data = Database(input_values)
            db.session.add(data)
            db.session.commit()
            # then redirect back to the same page (it also reloads the page)
            return redirect('/')
    
    inputs = Database.query      
    
    # add initial values to the database if it's empty
    if len([i for i in Database.query]) == 0:
        db.session.add(Database(init_values))
        db.session.commit()
        
    values = inputs[-1].__dict__
    names = eval('{' + ''.join([line.strip() for line in open('app/static/javascript/translation.js', encoding='utf-8').readlines()][2:-3]) + '}')
    language = open('app/static/javascript/_language.js', 'r', encoding='utf-8').readlines()[0].split()[-1].strip(';').strip("'")
    
    # creates a file to hold the database content for JS
    open('app/static/javascript/_database.js', 'w+', encoding='utf-8').close()
    js_db = open('app/static/javascript/_database.js', 'a', encoding='utf-8')
    js_db.write("var db = {\n")
    for line in values:
        if line != '_sa_instance_state':
            js_db.write(f"\t{ line }: { [inputs[i].__dict__[line] for i in range(1, inputs.count())] },\n")
    js_db.write("}\n")
    js_db.close()
        
    # or if the page is reloaded, send data to the template and display it
    return render_template(
        'main.html',
        values = values,
        names = names,
        language = language,
    )


# clears the database on enter
@app.route('/clear')
def page_clear():
    db.session.query(Database).delete()
    db.session.commit()
    return redirect('/')
