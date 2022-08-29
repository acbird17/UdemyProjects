from tkinter import *
from tkinter import messagebox
import string
import secrets
import random
import json
# import pyperclip
# pyperclip.cop(password)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    length = random.randint(12, 15)
    window.clipboard_clear()
    password_input.delete(0, END)
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    print(password)
    password_input.insert(0, password)
    window.clipboard_append(password)

# ---------------------------- SAVE PASSWORD ------------------------------- 
def save_password():
    website = website_input.get().title()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
# ---------------------------- SEARCH ------------------------------- #
def search():
    website = website_input.get().title()

    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found!")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title=website, message=f"No data for {website} found.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
bg_image = PhotoImage(file="./logo.png")
canvas.create_image(100,100, image=bg_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)
website_label.focus()

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)

website_input = Entry(width=26)
website_input.grid(column=1, row=1)

email_input = Entry(width=45)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "acbird.ab@gmail.com")

password_input = Entry(width=26)
password_input.config(text="")
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", bg="white", width=15, command=generate_pass)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=38, bg="white", command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=13, bg="white", command=search)
search_button.grid(column=2, row=1)


window.mainloop()