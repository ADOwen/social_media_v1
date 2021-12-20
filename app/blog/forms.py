from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,SubmitField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired


class CreatePostForm(FlaskForm):
    title = StringField('Name', validators=[DataRequired()])
    image = StringField('Image Url', validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired()])
    submit = SubmitField()

class postComment(FlaskForm):
    comment=StringField(validators=[DataRequired()])
    submit=SubmitField()

class postLike(FlaskForm):
    like=SubmitField("Like")
    
class postDislike(FlaskForm):
    dislike=SubmitField("Dislike")

    