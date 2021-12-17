from flask import Blueprint,render_template,request,redirect,url_for
from flask_login import current_user, login_required


from .forms import CreatePostForm
from app.models import Post

blog = Blueprint('blog',__name__,template_folder='blog_templates')

from app.models import db

@blog.route('/blog/main')
def blogHome():
    posts = Post.query.all()
    return render_template('blog.html' , posts = posts)

@blog.route('/posts/create', methods=["GET","POST"])
@login_required
def createPost():
    form = CreatePostForm()
    if request.method == "POST":
            if form.validate():
                print('form was validated')
                title = form.title.data
                image = form.image.data
                content = form.content.data

                # create instance of post
                post = Post(title, image, content, current_user.id)
                # add instance of database 
                db.session.add(post)
                # commit to database like github
                db.session.commit()
            
                return redirect(url_for('blog.blogHome'))

    return render_template('createpost.html', form=form)
