import os
import secrets
from PIL import Image
from flask import current_app


def save_image(form_image, image_name='hex_auto_generated', need_to_resize=True):

    image_fn, f_ext = os.path.splitext(form_image.filename)
    if image_name == 'hex_auto_generated':
        random_hex = secrets.token_hex(8)
        image_fn = random_hex + f_ext
    else:
        image_fn = str(image_name) + f_ext
    if not os.path.exists(os.path.join(current_app.root_path, 'static/sku_images')):
        os.mkdir(os.path.join(current_app.root_path, 'static/sku_images'))
    image_path = os.path.join(current_app.root_path, 'static/sku_images', image_fn)
    print('image_path:', image_path)
    
    # we need to resize image (if we want to)
    if need_to_resize:
        output_size = (500, 500)
        form_image_ = Image.open(form_image)
        form_image_.thumbnail(output_size)
        form_image = form_image_
    form_image.save(image_path)
    return image_fn