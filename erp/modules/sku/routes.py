# from erp.modules import modules
import os
from erp.modules.sku.forms import SkuForm
from erp import db
from erp.models.store import Sku_inf
from datetime import datetime
from erp.modules.sku.utils import save_image
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, current_app
from flask_login import current_user, login_required
from flask import Blueprint


modules = Blueprint('modules', __name__)


@modules.route('/modules/sku/add', methods=['GET', 'POST'])
@login_required
def add_sku():
    form = SkuForm()
    if request.method == 'GET':
      return render_template('modules/sku/add_sku.html', form=form)
    if request.method == 'POST':
      if form.validate_on_submit():
          sku = Sku_inf(sku_id = form.sku_id.data,
                        product = form.product.data,
                        name = form.name.data,
                        affilation = form.affilation.data,
                        comment = form.comment.data,
                        image = save_image(form.image.data, image_name=form.sku_id.data),
                        dtm = datetime.utcnow()
                        )
          db.session.add(sku)
          db.session.commit()
          flash('sku has been added!', category = 'success')
          return redirect(url_for('main.home'))
      else:
        flash("sku hasn't been added!", category = 'danger')
        return render_template('modules/sku/add_sku.html', form=form)

# @posts.route('/post/<int:post_id>')
# def post(post_id):
#     # post = Post.query.get(post_id)
#     post = Post.query.get_or_404(post_id)
#     return render_template('post.html', title = post.title, post = post)

# @posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
# @login_required
# def update_post(post_id):
#     post = Post.query.get_or_404(post_id)
#     if post.author.id != current_user.id:
#         abort(403) 
#     form = PostForm()
#     if form.validate_on_submit():
#         post.title = form.title.data
#         post.content = form.content.data
#         db.session.commit()
#         flash('Your post has been updated!', category = 'success')
#         return redirect(url_for('posts.post', post_id = post.id))
#     elif request.method == 'GET':
#         form.title.data = post.title
#         form.content.data = post.content
#     return render_template('create_post.html', titile='update post', form=form
#                         , legend = 'Update post')


# @posts.route('/post/<int:post_id>/delete', methods=['POST'])
# @login_required
# def delete_post(post_id):
#     post = Post.query.get_or_404(post_id)
#     if post.author.id != current_user.id:
#         abort(403)
#     db.session.delete(post)
#     db.session.commit()
#     flash('Your post has been deleted!', category = 'success')
#     return redirect(url_for('main.home'))