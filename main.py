from tkinter import *
from  tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I','J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbol + password_number
    shuffle(password_list)

    password = "".join(password_list) # is used to join a string with a string or empty string

    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")

    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading the data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Reading the data from the json file
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating the json file with the new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving the new data with the data in the json file
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, 'end')
            password_input.delete(0, 'end')

# ---------------------------- Find PASSWORD ------------------------------- #

def find_password():
    search_button.config(bg="Blue")
    website = website_input.get()
    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave website field empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading the data
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No data file found")
        else:
            if website not in data:
                messagebox.showinfo(title="Oop", message=f"No details for the {website}")
            else:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
    search_button.config(bg="White")


# ---------------------------- UI SETUP ------------------------------- #

#window
window = Tk()
window.title("Password Manager")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

#canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image= logo_img)
canvas.grid(column= 1, row = 0,)


#website Label
website_label = Label(text="Website:")
website_label.grid(column= 0, row =1)

#website input/entry
website_input = Entry(width=32)
website_input.focus()
website_input.grid(row = 1, column=1, padx=2.5, pady=2.5)

#username label
username_label = Label(text="Email/Username:")
username_label.grid(column= 0, row = 2)

#username Input/entry
username_input = Entry(width=52)
username_input.insert(0, "rohit@gmail.com")
username_input.grid(row = 2, column=1, columnspan=2, padx=2.5, pady=2.5)

#password label
password_label = Label(text="Password:")
password_label.grid(column= 0, row = 3)

#password input/entry
password_input = Entry(width=32)
password_input.grid(column= 1, row = 3, padx=2.5, pady=2.5)

#password generate button
password_gen_button = Button(text="Generate Password", command=generate_password)
password_gen_button.grid(column= 2, row = 3, padx=2.5, pady=2.5)

#password Add Button
add_button = Button(text="Add", width=44, command= save_password)
add_button.grid(column= 1, row = 4, columnspan=2)


#Search Button
search_button = Button(text="Search", width=15, command= find_password)
search_button.grid(column= 2, row = 1, columnspan=2)


# To stay app window open until closing it
window.mainloop()
