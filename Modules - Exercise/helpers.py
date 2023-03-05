from PIL import Image, ImageTk

from hashlib import sha256

from canvas import frame


def clean_screen():
    frame.delete('all')


def resize_images(img_path):
    image = Image.open(img_path)
    resized_image = image.resize((75, 125))

    image = ImageTk.PhotoImage(resized_image)

    return image


def get_password_hash(password):
    hash_object = sha256(password.encode())

    return str(hash_object.hexdigest())

