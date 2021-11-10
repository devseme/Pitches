from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField,SelectField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import Required, Email, Length, EqualTo
from ..models import User
from wtforms import ValidationError
 
 
 
class PostForm(FlaskForm):
    post_title = StringField('Post title', validators=[Required()])
    content = TextAreaField('Body', validators=[Required()])
    category = SelectField('Post category',choices=[('Select a category','Select a category'),('Political aspirations', 'Political aspirations'),('Handling interviews','Handling Interviews'),('New Product','New Product'),('Business venture','Business venture')], validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')   