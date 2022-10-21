from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class SkuForm(FlaskForm):
    sku_id = IntegerField('sku_id', validators=[DataRequired()])
    product = StringField('product', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    affilation = StringField('affilation', validators=[DataRequired()])
    comment = TextAreaField('comment', validators=[DataRequired()])
    submit = SubmitField('Post')
