from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,SubmitField
from wtforms.validators import DataRequired

class CreatePostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    image = StringField('Image Url')
    content = StringField('Content', validators=[DataRequired()])
    submit = SubmitField()
    