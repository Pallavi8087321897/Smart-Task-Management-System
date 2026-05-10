from extensions import db
from datetime import datetime

class Task(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200))

    description = db.Column(db.String(500))

    priority = db.Column(db.String(50))

    status = db.Column(db.String(50))

    created_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )