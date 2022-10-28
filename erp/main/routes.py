from flask import Blueprint
from flask import render_template, request
from flask_login import login_required

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/erp')
@main.route('/erp/home')
@login_required
def home():
    return render_template('about.html', title = 'about')

@main.route('/erp/about')
def about():
    return render_template('about.html', title = 'about')

@main.route('/erp/modules')
def modules():
    return render_template('modules/modules.html', title = 'modules')


