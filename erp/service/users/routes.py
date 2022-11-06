from flask import Blueprint
from flask import render_template, url_for, flash, redirect, request, current_app
from erp import db, bcrypt
from erp.service.users.forms import (LoginForm)
from erp.models.service import User
from flask_login import login_user, logout_user, current_user, login_required

 
users = Blueprint('users', __name__)


# @users.route('/erp/register', methods=['GET', 'POST'])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('main.home')) 
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
#         user = User(username=form.username.data
#                     , email=form.email.data
#                     , password = hashed_password)
#         db.session.add(user)
#         db.session.commit()
#         flash(f'{form.username.data} account created! You can log in now.', category='success')
#         return redirect(url_for('users.login'))
#     return render_template('service/register.html', titile='register', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home')) 
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            requested_page = request.args.get('next')
            return redirect(requested_page) if requested_page else redirect(url_for('main.home'))
        else:
            flash(f'Login unsuccessful! Please check your username and/or password', category='danger')
    return render_template('login/login.html', titile='login', form=form)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))


# @users.route('/erp/account', methods=['GET', 'POST'])
# @login_required
# def account():
#     form = UpdateAccountForm()
#     if form.validate_on_submit():
#         if form.image.data:
#             image_file = save_picture(form.image.data)
#             # also i want to drop old picture (if it's not default) before changing the name in db
#             old_picture_path = os.path.join(current_app.root_path, 'static/profile_pics', current_user.image)
#             if os.path.isfile(old_picture_path) and ('default' not in current_user.image):
#                 os.remove(old_picture_path)
#             # and then change name to new file in db
#             current_user.image = image_file
#         current_user.username = form.username.data
#         current_user.email = form.email.data 
#         db.session.commit()
#         flash('your account has been updated!', category = 'success')
#         return redirect(url_for('users.account'))
#     elif request.method == 'GET':
#         form.username.data = current_user.username
#         form.email.data = current_user.email
#     image_file = url_for('static', filename=f'profile_pics/{current_user.image}')
#     return render_template('service/account.html', titile='account', image_file=image_file, form=form)


# @users.route('/user/<string:username>')
# def user_posts(username):
#     page = request.args.get('page', 1, type=int)
#     user = User.query.filter_by(username=username).first_or_404()
#     posts = Post.query\
#             .filter_by(author=user)\
#             .order_by(Post.date_posted.desc())\
#             .paginate(page=page, per_page=5)
#     return render_template('user_post.html', posts=posts, user=user)


# @users.route('/erp/reset_password', methods=['GET', 'POST'])
# def reset_request():
#     if current_user.is_authenticated:
#         return redirect(url_for('main.home')) 
#     form = RequestResetForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         send_reset_email(user)
#         flash('email for reseting pssword has been sent', category='info')
#         return redirect(url_for('users.login'))
#     return render_template('service/reset_request.html', title='reset password', form=form)
 

# @users.route('/erp/reset_password/<token>', methods=['GET', 'POST'])
# def reset_token(token):
#     if current_user.is_authenticated:
#         return redirect(url_for('main.home')) 
#     user = User.verify_reset_token(token)
#     if user is None:
#         flash('That is an invalid or expired token', category='warning')
#         return redirect(url_for('users.reset_request'))
#     form = ResetPasswordForm()
#     if form.validate_on_submit():
#         hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
#         user.password = hashed_password
#         db.session.commit()
#         flash(f'Your password has been updated', category='success')
#         return redirect(url_for('users.login'))
#     return render_template('service/reset_token.html', title='reset password', form=form)