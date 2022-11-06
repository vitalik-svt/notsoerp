from erp import db
from datetime import datetime

######################### Store schema #########################


class Sku_inf(db.Model):
    __table_args__ = {'schema': 'store'}
    recid = db.Column(db.Integer, primary_key=True, autoincrement=True)
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
    __table_args__ = {'schema': 'store'}
    recid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sku_id = db.Column(db.Integer, nullable=False)
    component_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Sku_comp('{self.id}', '{self.name}')"