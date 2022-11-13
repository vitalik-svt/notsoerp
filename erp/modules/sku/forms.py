from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField, IntegerField, FileField, FloatField, FieldList, FormField
from wtforms.validators import DataRequired


class _SkuComponentForm(FlaskForm):
    component_id = IntegerField('component_id', validators=[DataRequired()])
    quantity = FloatField('quantity', validators=[DataRequired()])

class AddSkuForm(FlaskForm):
    # sku info
    sku_id = IntegerField('sku_id', validators=[DataRequired()])
    product = StringField('product', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    affilation = StringField('affilation', validators=[DataRequired()])
    comment = TextAreaField('comment')
    image = FileField('catalogue sku image', validators=[FileAllowed(['jpg', 'png', 'bmp'])])
    # sku comp
    sku_components = FieldList(FormField(_SkuComponentForm), min_entries=1, max_entries=50)
    # submit button
    submit = SubmitField('Add sku')
