from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired


class MovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    year = IntegerField('Year')
    genre = StringField('Genre')
    rating = IntegerField('Rating')