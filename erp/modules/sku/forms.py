from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField, IntegerField, FileField
from wtforms.validators import DataRequired


class SkuForm(FlaskForm):
    sku_id = IntegerField('sku_id', validators=[DataRequired()])
    product = StringField('product', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    affilation = StringField('affilation', validators=[DataRequired()])
    comment = TextAreaField('comment')
    image = FileField('catalogue sku image', validators=[FileAllowed(['jpg', 'png', 'bmp'])])
    submit = SubmitField('Add sku')
