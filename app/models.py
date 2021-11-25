from app import db
from app.values import init_values

# design a database scheme
class Database(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    # creates a database column for every value in 'values.py'
    # need to assign a column manually to create a different type of column
    for value in init_values:
        exec('%s = db.Column(db.Integer, nullable=False)' % value)
    

    # sends data to corresponding database columns
    def __init__(self, values):
        for value in values:
            setattr(self, value, values[value])


# initialize the database model into the .sqlite like
db.create_all()
