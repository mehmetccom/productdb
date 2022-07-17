from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
 
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    products = db.relationship('Product', backref='category', lazy='dynamic')
    def __repr__(self):
        return "<Category(%d, %s)>" % (self.id, self.name)
 
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Numeric(precision=5, scale=2), default=999.99)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __repr__(self):
        return "Product(%d, %s, %s, %5.2f, %d)" % (
                self.id, self.name, self.price, self.category_id)
                

