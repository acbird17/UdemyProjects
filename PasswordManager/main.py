from tkinter import *
from tkinter import messagebox
import string
import secrets
import random
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
# random.choice(rand_chars) for char in range(length)

# ---------------------------- SAVE PASSWORD ------------------------------- 
def save_password():
    website = str(website_input.get())
    email = str(email_input.get())
    password = password_input.get()
    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Error", message="Looks like you left a field blank.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        
        if is_ok:
            with open("pwfile.txt", "a") as pwfile:
                pwfile.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)
    

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

website_input = Entry(width=45)
website_input.grid(column=1, row=1, columnspan=2)

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


window.mainloop()