from app import db

# design a database scheme
class Database(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    input1 = db.Column(db.Integer, nullable=False)
    input2 = db.Column(db.Integer, nullable=False)
