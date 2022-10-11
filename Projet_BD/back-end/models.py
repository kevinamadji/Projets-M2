from  flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Personnage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(80), nullable=False)
    niveau = db.Column(db.String(120), nullable=False)
    item = db.relationship('Item', backref= 'proprio')
    
    def __repr__(self):
        return '<User %r>' % self.username
    

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(80), nullable=False)
    poids = db.Column(db.Integer, unique=True, default=0)
    personnage_id = db.Column(db.Integer, db.ForeignKey('personnage.id'))
    
    def __init__(self, nom, poids):
        self.nom = nom
        self.poids = poids
        
    def __repr__(self):
        return '<Nom: %r>' % self.nom
    