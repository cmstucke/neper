from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Optional


class RecipeImageForm(FlaskForm):
  caption = StringField('Caption', validators=[DataRequired])
  category = StringField('Category', validators=[DataRequired])
  image_url = StringField('Description', validators=[DataRequired])
