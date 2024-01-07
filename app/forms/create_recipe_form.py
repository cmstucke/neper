from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Optional


class CreateRecipeForm(FlaskForm):
  title = StringField('Title', validators=[DataRequired])
  category = StringField('Category', validators=[Optional])
  description = StringField('Description', validators=[Optional])
  ingredients = StringField('Ingredients', validators=[DataRequired])
  steps = StringField('Steps', validators=[DataRequired])
  background = StringField('Background', validators=[Optional])
