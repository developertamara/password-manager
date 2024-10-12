from tkinter import *
from tkinter import messagebox
import random
from types import NoneType

import pyperclip
import json

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
    pyperclip.copy(password) # Copy password to the clipboard.

    # print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_data = website_textbox.get()
    email_data = email_textbox.get()
    password_data = password_textbox.get()
    new_data = {
        website_data: {
            "email": email_data,
            "password": password_data
        }
    }

    if website_data == "" or email_data == "" or password_data == "":
        messagebox.showerror(message="Please make sure you haven't left any fields empty.")
        return
    else:
        # Write to the json file.
        # with open("data.json", "w", encoding="utf-8") as data_file:
        #     json.dump(new_data, data_file, indent=4)

        # Read the json file.
        # with open("data.json", "r", encoding="utf-8") as data_file:
        #     data = json.load(data_file)
        #     print(data)

        # Update data in a json file.
        try:
            with open("data.json", "r", encoding="utf-8") as data_file:
                data = json.load(data_file) # Reading the old data.
        except FileNotFoundError:
            with open("data.json", "w", encoding="utf-8") as data_file:
                # data.update(new_data) # Updating the old data with new data.
                json.dump(new_data, data_file, indent=4) # Saving the updated data.
        else:
            data.update(new_data)  # Updating the old data with new data.
            with open("data.json", "w", encoding="utf-8") as data_file:
                json.dump(data, data_file, indent=4) # Saving the updated data.
        finally:
            clear_entries()

def clear_entries():
    website_textbox.delete(0, END)
    password_textbox.delete(0, END)

def find_password():
   try:
       # Check if the input is empty
       if website_textbox.get() == "":
           messagebox.showinfo(message="Enter a website to perform the search.")
           return

       with open("data.json", "r", encoding="utf-8") as data_file:
            data = json.load(data_file)  # Reading the old data.
            search_value = website_textbox.get().lower()

       lowercased_data = {key.lower(): value for key, value in data.items()}
       search_result = lowercased_data.get(search_value)

       if search_result is None:
           messagebox.showinfo(message="No password found for this website.")
           return
       if search_result is None:
           messagebox.showinfo(message="No password found for this website.")
           return

       password_return = search_result['password']
       messagebox.showinfo(message=f"Password for {search_value}:\n {password_return}")

   except FileNotFoundError:
       messagebox.showerror(title="Error", message="No data file found.")
   except TypeError as e:
       messagebox.showerror(title="Error", message=f"Error: {e}. This usually means the data structure has a NoneType.")
   except Exception as e:
       messagebox.showerror(title="Error", message=f"An unexpected error occurred: {e}.")


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

website_textbox = Entry(width=20)
website_textbox.focus()
website_textbox.grid(column=1, row=1, columnspan=1)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)

email_label = Label(text="Email/Username:", anchor="w")
email_label.grid(column=0, row=2)

email_textbox = Entry(width=38)
email_textbox.insert(0, "default@gmail.com")
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