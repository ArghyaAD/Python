from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generate():
    entry_password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list1 = [random.choice(letters) for _ in range(nr_letters)]
    password_list2 = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list3 = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_list1 + password_list2 + password_list3

    random.shuffle(password_list)
    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    password = entry_password.get()
    email = entry_email.get()
    new_data = {website:
        {
            "email": email,
            "password": password
        }}
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="ERROR", message="please fill all areas to proceed!!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"email:{email}\npassword:{password}\nready to save?")
        if is_ok:
            try:
                with open("password.json", mode="r") as data:
                    file_data = json.load(data)
                    file_data.update(new_data)
            except:
                with open("password.json", mode="w") as data:
                    json.dump(new_data, data, indent=4)
                    entry_website.delete(0, END)
                    entry_password.delete(0, END)
            else:
                with open("password.json", mode="w") as data:
                    json.dump(file_data, data, indent=4)
                    entry_website.delete(0, END)
                    entry_password.delete(0, END)


# ------------------------SEARCH DETAILS-------------------------#

def search():
    try:
        with open("password.json", mode="r") as data:
            details = json.load(data)
            if len(entry_website.get()) > 0:
                try:
                    to_search = entry_website.get()
                    email = details[to_search]["email"]
                    password = details[to_search]["password"]
                    messagebox.showinfo(title=to_search, message=f"email:{email}\npassword:{password}")
                except:
                    messagebox.showinfo(title="oops", message="no such info")
            else:
                messagebox.showinfo(title="ERROR", message="Please fill to proceed")
    except:
        pass


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:")
label_website.grid(row=1, column=0)

label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0)

label_password = Label(text="Password:")
label_password.grid(row=3, column=0)

entry_website = Entry(width=21)
entry_website.focus()
entry_website.grid(row=1, column=1)

entry_email = Entry(width=39)
entry_email.insert(0, "jishuadhikary2015@gmail.com")
entry_email.grid(row=2, column=1, columnspan=2)

entry_password = Entry(width=21)
entry_password.grid(row=3, column=1)

button_password = Button(text="Generate Password", width=14, command=password_generate)
button_password.grid(row=3, column=2)

button_add = Button(text="Add", width=34, command=save)
button_add.grid(row=4, column=1, columnspan=2)

button_search = Button(text="search", width=15, command=search)
button_search.grid(row=1, column=2)
window.mainloop()
