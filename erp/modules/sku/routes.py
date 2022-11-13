# from erp.modules import modules
import os
from erp.modules.sku.forms import AddSkuForm
from erp import db
from erp.models.store import Sku_inf, Sku_comp
from datetime import datetime
from erp.modules.sku.utils import save_image
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, current_app
from flask_login import current_user, login_required
from flask import Blueprint
import sys


modules = Blueprint('modules', __name__)


@modules.route('/modules/sku/add', methods=['GET', 'POST'])
@login_required
def add_sku():
    form = AddSkuForm()
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
          sku_comp = []
          for component in form.sku_components:
            _sku_comp = Sku_comp(sku_id = form.sku_id.data,
                                 component_id = component.component_id.data,
                                 quantity = component.quantity.data)
            sku_comp.append(_sku_comp)
            print(sku_comp, file=sys.stderr)
          db.session.add(sku)
          db.session.add_all(sku_comp)
          db.session.commit()
          
          flash('sku has been added!', category = 'success')
          return redirect(url_for('main.home'))
      else:
        flash("sku hasn't been added!", category = 'danger')
        return render_template('modules/sku/add_sku.html', form=form)
