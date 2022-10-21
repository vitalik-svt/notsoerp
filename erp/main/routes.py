from flask import Blueprint
from flask import render_template, request
from flask_login import login_required

main = Blueprint('main', __name__)


@main.route('/erp')
@main.route('/erp/home')
@login_required
def home():
    # page = request.args.get('page', 1, type=int)
    # posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    # return render_template('home.html', posts=posts, title = 'notsoerp')
    return render_template('about.html', title = 'about')


@main.route('/erp/about')
def about():
    return render_template('about.html', title = 'about')


@main.route('/erp/modules')
def modules():
    return render_template('modules/modules.html', title = 'modules')


