from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField,  SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Length, Email, DataRequired
from flask_wtf.file import FileField, FileRequired, FileField, FileAllowed
from werkzeug.utils import secure_filename


class UserForm(FlaskForm):
	propertytitle = StringField('Property Title', validators=[InputRequired(), Length(max=30)])
	description = TextAreaField('Description', validators=[DataRequired(), Length(max=150)])
	noofrooms = StringField('No. of Rooms', validators=[InputRequired(), Length(max=30)])
	noofbathrooms = StringField('No. of Bathrooms', validators=[InputRequired(), Length(max=30)])
	price = StringField('Price', validators=[InputRequired(), Length(max=60)])
	propertytype = SelectField('Property Type', choices=[('House', 'House'), ('Apartment', 'Apartment')], validators=[InputRequired()])
	location = StringField('Location', validators=[InputRequired(), Length(max=40)])
	property_picture= FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg','png','jpeg'], 'Only images allowed!')])
	submit= SubmitField('Add Property')