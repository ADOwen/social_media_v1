from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,SubmitField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired


class CreatePostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    image = StringField('Image Url')
    content = StringField('Content', validators=[DataRequired()])
    submit = SubmitField()

class postComment(FlaskForm):
    comment=StringField(validators=[DataRequired()])
    submit=SubmitField()

class postLike(FlaskForm):
    like=SubmitField("Like")
    
class postDislike(FlaskForm):
    dislike=SubmitField("Dislike")

    