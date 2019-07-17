from flask import (Blueprint, render_template,
                   url_for, flash, redirect,
                   request, abort)
from flask_login import current_user, login_required
from app import _db
from app.models import Post
from app.Posts.forms import PostForm


posts = Blueprint('posts', __name__)


@posts.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        _post = Post(title=form.title.data, content=form.content.data, user_id=current_user.id)
        _db.session.add(_post)
        _db.session.commit()
        flash('Your post has been created!!', 'success')
        return redirect(url_for('main.home_page'))
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')


@posts.route('/post/<int:post_id>')
def post(post_id):
    _post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=_post.title, post=_post)


@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    _post = Post.query.get_or_404(post_id)
    if _post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        _post.title = form.title.data
        _post.content = form.content.data
        _db.session.commit()
        flash('Your Post has been updated!!!', 'success')
    elif request.method == 'GET':
        form.title.data = _post.title
        form.content.data = _post.content
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')


@posts.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    _post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    _db.session.delete(_post)
    _db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home_page'))
