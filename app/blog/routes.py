from flask import Blueprint,render_template,request,redirect,url_for
from flask_login import current_user, login_required
from sqlalchemy import asc, desc



from .forms import CreatePostForm, postComment
from app.models import Post, postComments, User

blog = Blueprint('blog',__name__,template_folder='blog_templates')

from app.models import db


@blog.route('/blog/main')
@login_required
def blogHome():
    posts = Post.query.order_by(desc(Post.date_created)).all()
    return render_template('blog.html' ,posts = posts,current=current_user.id)

@blog.route('/posts/create', methods=["GET","POST"])
@login_required
def createPost():
    user= current_user
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

    return render_template('createpost.html', form=form, user=user)

@blog.route('/posts/<int:id>', methods=['GET','POST'])
@login_required
def singlePostPage(id):
    post = Post.query.filter_by(id=id).first()
    comment = postComment()
    comments=postComments.query.order_by(desc(postComments.date_added)).all()
    users=db.session.query(User).join(postComments)
    if request.method == 'POST':
        if comment.validate_on_submit:
            com = comment.comment.data
            comnt=postComments(com,current_user.id,id)
            db.session.add(comnt)
            db.session.commit()

            return redirect(url_for('blog.singlePostPage', id=id))

    return render_template('post_page.html',p=post,users=users,comment=comment,current=current_user.id,comments=comments,id=id, title='Post Page')

@blog.route('/posts/delete/<int:id>', methods=['GET','POST'])
@login_required
def deleteComment(id):
    comment=postComments.query.filter_by(id=id).first()
    pageid=comment.postId
    if request.method == 'POST':
        
        db.session.delete(comment)
        db.session.commit()
    
    return redirect(url_for('blog.singlePostPage', id=pageid))

@blog.route('/posts/postlike/<int:id>', methods=['GET','POST'])
@login_required
def postLikeIt(id):
    post=Post.query.filter_by(id=id).first()
    if request.method=='POST':
        post.like=True
        db.session.commit()

    return redirect(url_for('blog.singlePostPage', id=id))

@blog.route('/posts/commentlike/<int:id>', methods=['GET','POST'])
@login_required
def commentLikeIt(id):
    comment=postComments.query.filter_by(id=id).first()
    pageid=comment.postId
    if request.method=='POST':
        comment.like=True
        db.session.commit()

    return redirect(url_for('blog.singlePostPage', id=pageid))

@blog.route('/posts/postdislike/<int:id>', methods=['GET','POST'])
@login_required
def postDislikeIt(id):
    post=Post.query.filter_by(id=id).first()
    if request.method=='POST':
        post.dislike=True
        db.session.commit()

    return redirect(url_for('blog.singlePostPage', id=id))

@blog.route('/posts/commentdislike/<int:id>', methods=['GET','POST'])
@login_required
def commentDislikeIt(id):
    comment=postComments.query.filter_by(id=id).first()
    pageid=comment.postId
    if request.method=='POST':
        comment.dislike=True
        db.session.commit()

    return redirect(url_for('blog.singlePostPage', id=pageid))

@blog.route('/posts/homepostlike/<int:id>', methods=['GET','POST'])
@login_required
def homePostLikeIt(id):
    post=Post.query.filter_by(id=id).first()
    if request.method=='POST':
        post.like=True
        db.session.commit()

    return redirect(url_for('blog.blogHome'))

@blog.route('/posts/homepostdislike/<int:id>', methods=['GET','POST'])
@login_required
def homePostDislikeIt(id):
    post=Post.query.filter_by(id=id).first()
    if request.method=='POST':
        post.dislike=True
        db.session.commit()

    return redirect(url_for('blog.blogHome'))

@blog.route('/posts/unlike/<int:id>',methods=['GET','POST'])
@login_required
def homePostUnlike(id):
    post=Post.query.filter_by(id=id).first()
    if request.method=='POST':
        post.like=False
        db.session.commit()
    return redirect(url_for('blog.blogHome'))

@blog.route('/posts/postsunlike/<int:id>',methods=['GET','POST'])
@login_required
def postUnlike(id):
    post=Post.query.filter_by(id=id).first()
    if request.method=='POST':
        post.like=False
        db.session.commit()
    return redirect(url_for('blog.singlePostPage',id=id))

@blog.route('/posts/commentsunlike/<int:id>',methods=['GET','POST'])
@login_required
def commentUnlike(id):
    comment=postComments.query.filter_by(id=id).first()
    pageid=comment.postId
    if request.method=='POST':
        comment.like=False
        db.session.commit()
    return redirect(url_for('blog.singlePostPage',id=pageid))

@blog.route('/posts/undislike/<int:id>',methods=['GET','POST'])
@login_required
def homePostUndislike(id):
    post=Post.query.filter_by(id=id).first()
    if request.method=='POST':
        post.dislike=False
        db.session.commit()
    return redirect(url_for('blog.blogHome'))

@blog.route('/posts/postsundislike/<int:id>',methods=['GET','POST'])
@login_required
def postUndislike(id):
    post=Post.query.filter_by(id=id).first()
    if request.method=='POST':
        post.dislike=False
        db.session.commit()
    return redirect(url_for('blog.singlePostPage', id=id))

@blog.route('/posts/commentsundislike/<int:id>',methods=['GET','POST'])
@login_required
def commentUndislike(id):
    comment=postComments.query.filter_by(id=id).first()
    pageid=comment.postId
    if request.method=='POST':
        comment.dislike=False
        db.session.commit()
    return redirect(url_for('blog.singlePostPage', id=pageid))