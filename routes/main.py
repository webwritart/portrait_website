from flask import Blueprint, render_template, request
import os


main = Blueprint('main', __name__, static_folder='static', template_folder='templates')


@main.route('/')
def home():
    thumbnails = []
    thumbnails_path = 'static/images/artworks/thumbnails/'
    thumbnail_names = os.listdir(thumbnails_path)
    for thumbnail in thumbnail_names:
        thumbnails.append(thumbnails_path + thumbnail)
    return render_template('index.html', thumbnails=thumbnails)


@main.route('/full_size_image', methods=['GET', 'POST'])
def full_size_image():
    original_image_path = "static/images/artworks/originals/"
    img_url = request.args.get('image_url')
    img_name = img_url.split("/")[-1:][0]
    original_image_url = original_image_path + img_name
    return render_template('full_size_image_template.html', img_url=original_image_url)
