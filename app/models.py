from app import db

# design a database scheme
class Database(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # for each new entry, add its initial value to `values.py` and create its input in a form template
    mask_rate = db.Column(db.Integer, nullable=False)
    mask_fall_rate = db.Column(db.Integer, nullable=False)

    def __init__(self, values):
        self.mask_rate = values['mask_rate']
        self.mask_fall_rate = values['mask_fall_rate']
