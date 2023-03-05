from tkinter import Button, Entry
from canvas import root, frame
from helpers import clean_screen, get_password_hash
from products_page import display_products
from json import loads, dump


def render_entry():
    register_btn = Button(root,
                          text="Register",
                          bg="green",
                          fg="white",
                          font=("Helvetica", 14),
                          borderwidth=0,
                          width=20,
                          height=3,
                          command=register
                          )

    login_btn = Button(root,
                       text="Log in",
                       bg="blue",
                       fg="white",
                       font=("Helvetica", 14),
                       borderwidth=0,
                       width=20,
                       height=3,
                       command=login
                       )

    frame.create_window(350, 260, window=register_btn)
    frame.create_window(350, 350, window=login_btn)


def register():
    clean_screen()

    frame.create_text(100, 50, text="First name:")
    frame.create_text(100, 100, text="Last name:")
    frame.create_text(100, 150, text="Username:")
    frame.create_text(100, 200, text="Password:")

    frame.create_window(200, 50, window=first_name_box)
    frame.create_window(200, 100, window=last_name_box)
    frame.create_window(200, 150, window=username_box)
    frame.create_window(200, 200, window=password_box)

    registration_btn = Button(
        root,
        text="Register",
        bg='green',
        fg='white',
        borderwidth=0,
        command=registration
    )

    frame.create_window(300, 250, window=registration_btn)


def registration():
    user_info = {
        "first_name": first_name_box.get(),
        "last_name": last_name_box.get(),
        "username": username_box.get(),
        "password": get_password_hash(password_box.get())
    }

    if validation(**user_info):
        with open("db/users_information.txt", 'a') as users_file:
            dump(user_info, users_file)
            users_file.write('\n')
            display_products()


def validation(**kwargs):
    for el in kwargs.values():
        if not el.strip():
            frame.create_text(300, 300, text="Please fill all fields!", fill='red', tag='error')
            return False

    frame.delete('error')

    info_data = get_user_data()

    for record in info_data:
        if record["username"] == kwargs["username"]:
            frame.create_text(300, 300, text="This username is taken!", fill='red', tag='error')
            return False

    frame.delete('error')

    return True


def get_user_data():
    info_data = []

    with open("db/users_information.txt", 'r') as users_file:
        for line in users_file:
            info_data.append(loads(line))

    return info_data


def login():
    clean_screen()

    frame.create_text(100, 50, text="Username:")
    frame.create_text(100, 100, text="Password:")

    frame.create_window(200, 50, window=username_box)
    frame.create_window(200, 100, window=password_box)

    frame.create_window(300, 250, window=logging_btn)


def logging():
    if login_check():
        display_products()
    else:
        frame.create_text(160, 200, text="Invalid username or password!", fill='red')


def login_check():
    info_data = get_user_data()
    user_name = username_box.get()
    user_pass = get_password_hash(password_box.get())

    for i in range(len(info_data)):
        username = info_data[i]["username"]
        password = info_data[i]["password"]

        if user_name == username and user_pass == password:
            return True

    return False


def login_fulfilled(event):
    info = {
        "username": username_box.get(),
        "password": password_box.get()
    }

    for el in info.values():
        if not el.strip():
            logging_btn["state"] = "disabled"
            break
    else:
        logging_btn["state"] = "normal"


first_name_box = Entry(root, bd=0)
last_name_box = Entry(root, bd=0)
username_box = Entry(root, bd=0)
password_box = Entry(root, bd=0, show='*')

logging_btn = Button(root,
                         text='Log in',
                         bg='blue',
                         fg='white',
                         borderwidth=0,
                         command=logging
    )

logging_btn["state"] = "disabled"

root.bind('<KeyRelease>', login_fulfilled)