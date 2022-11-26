from erp import db
from datetime import datetime
from sqlalchemy import UniqueConstraint

######################### Store schema #########################


class Sku_inf(db.Model):
    __table_args__ = {'schema': 'store'}
    recid = db.Column(db.Integer, autoincrement=True, primary_key=True)
    sku_id = db.Column(db.Integer, unique=True)
    product = db.Column(db.String(127), nullable = False)
    name = db.Column(db.String(511), nullable = False)
    affilation = db.Column(db.String(127), nullable = False)
    image = db.Column(db.String(127), nullable=True)
    comment = db.Column(db.Text, nullable = False)
    dtm = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    
    def __repr__(self):
        return f"Sku_inf('{self.sku_id}', '{self.name}')"

class Sku_comp(db.Model):
    recid = db.Column(db.Integer, autoincrement=True, primary_key=True)
    sku_id = db.Column(db.Integer, db.ForeignKey(Sku_inf.sku_id))
    component_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    dtm = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    # constraints and other table-related options
    __table_args__ = (UniqueConstraint('sku_id', 'component_id', name='_sku_component_constraint')
                   , {'schema': 'store'})

    # relationship
    sku = db.relationship('Sku_inf', backref=db.backref('components', lazy='dynamic', collection_class=list))

    def __repr__(self):
        return f"Sku_comp('{self.sku_id}', '{self.component_id}', '{self.quantity}')"