from app import db

# design a database scheme
class Database(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mask_rate = db.Column(db.Integer, nullable=False)
    mask_fall_rate = db.Column(db.Integer, nullable=False)
