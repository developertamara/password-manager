from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_symbols + password_numbers + password_letters
    random.shuffle(password_list)

    password = ''.join(password_list)
    password_textbox.insert(0, password)
    pyperclip.copy(password) #Copy password to the clipboard.

    # print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_data = website_textbox.get()
    email_data = email_textbox.get()
    password_data = password_textbox.get()

    if website_data == "":
        messagebox.showerror(message="Website field cannot be blank.")
        return

    if email_data == "":
        messagebox.showwarning(message="Email field cannot be blank.")
        return

    if password_data == "":
        messagebox.showwarning(title="Oops", message="Password field cannot be blank.")
        return

    is_ok = messagebox.askokcancel(title=website_data,
                                   message=f"These are the details entered: \n"
                                                       f"Website: {website_data} \n"
                                                       f"Email: {email_data} \n"
                                                       f"Password: {password_data} \n"
                                                       f"Is it OK to save?")

    if is_ok:
        with open("data.txt", "a") as password_file:
            password_file.write(f"{website_data} | {email_data} | {password_data} \n")
        clear_entries()

def clear_entries():
    website_textbox.delete(0, END)
    password_textbox.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
key_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=key_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_textbox = Entry(width=35)
website_textbox.focus()
website_textbox.grid(column=1, row=1, columnspan=2)

email_label = Label(text="Email/Username:", anchor="e")
email_label.grid(column=0, row=2)

email_textbox = Entry(width=35)
email_textbox.insert(0, "tamarangr@gmail.com")
email_textbox.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:", anchor="e")
password_label.grid(column=0, row=3)

password_textbox = Entry(width=21)
password_textbox.grid(column=1, row=3)

gen_password_button = Button(text="Generate Password", command=generate_password)
gen_password_button.grid(column=2, row=3)

add_password_button = Button(text="Add", width=36, command=save_password)
add_password_button.grid(column=1, row=4, columnspan=2)
window.mainloop()