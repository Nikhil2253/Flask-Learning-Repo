from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()
db.create_all()

class User(db.Model):
    id= db.Column(db.Integer, primary_key= True)
    name= db.Column(db.String(100), nullable=False)
    email= db.Column(db.String(200), unique=True)
    posts= db.relationship('Post', backref='author', lazy= True)

#Basic Queries in the Flask DB Connection
# User.query.all()
# User.query.filter_by()
# User.query.commit()
# User.query.get()
