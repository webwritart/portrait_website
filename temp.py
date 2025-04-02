from PIL import Image
import os

image_folder = 'static/images/artworks/originals'

for image_path in os.listdir(image_folder):
    import_path = 'static/images/artworks/originals/'
    export_path = 'static/images/artworks/thumbnails/'
    image = Image.open(import_path + image_path)
    width, height = image.size
    print(width, height)

    w_h_ratio = round(width/height, 3)
    print(w_h_ratio)

    new_height = 500
    new_width = round(new_height * w_h_ratio)
    print(new_width)

    image.thumbnail((new_width, new_height), Image.Resampling.LANCZOS)
    image.save(export_path + image_path)

