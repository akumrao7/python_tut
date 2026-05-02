import tkinter as tk

import tkinter.font as tfont
from tkinter import ttk

#Tk
window = tk.Tk()
window.title("My application")
window.minsize(400, 300)

custom_font=tfont.Font(family='Times New Roman', size=15, weight='bold') # slant='italic',

label = ttk.Label(text="Hello World!!\nHave a nice day", font=custom_font, padding=15)
label.pack()
# label.config(font=("Courier New", 25))
label.config(text="My new App")

# Buttons

# counter=0
def function_button():
    # global counter
    # counter+=1
    input_text=user_input.get()
    label.config(text=input_text)


# Taking user input using Entry
user_input = ttk.Entry(width=30)
user_input.pack()

button = ttk.Button(text="Click", command=function_button)
button.pack()


quit_function = ttk.Button(text="Quit", command=window.destroy)
quit_function.pack(pady=10)

sep=ttk.Separator(orient="horizontal")
sep.pack(fill="x")

text=tk.Text(height=5, width=30)
text.pack(pady=10)
text.focus()

text.insert("1.0", "Enter Your Comments")

def text_function():
    text_data = text.get("1.0", "end")
    print(text_data)

text_button = ttk.Button(text="Get text", command=text_function)
text_button.pack()


# text["state"] = "disabled"
#
# def enable_text():
#     text["state"] = "normal"
#
# enable_button = ttk.Button(text="Enable text bos", command=enable_text)
# enable_button.pack()

# check_options=tk.IntVar()
check_options=tk.StringVar()

def check_option_task():
    print(check_options.get())

check_button = ttk.Checkbutton(text="Agree with the terms and conditions?", variable=check_options, command=check_option_task, onvalue="Yes", offvalue="No")
check_button.pack()


# RadioButton

radio_value=tk.StringVar()
def get_radio_value():
    print(radio_value.get())
option_1=ttk.Radiobutton(text="Male", variable=radio_value, value='male', command=get_radio_value)
option_2=ttk.Radiobutton(text="Female", variable=radio_value, value='female', command=get_radio_value)
option_1.pack()
option_2.pack()

# Combobox
selected_country=tk.StringVar()
countries=ttk.Combobox(textvariable=selected_country, values=("US", "UK", "India", "China"))
countries["state"]= "readonly"
countries.pack()

def display_country(event):
    msg=f"Selected country is {selected_country.get()}"
    country_label=tk.Label(text=msg)
    country_label.pack()
    # print(f"Selected countries is {selected_country.get()}")

countries.bind("<<ComboboxSelected>>", display_country)

# List Box

food_items=('Pizza', "Roti", "Rice", "Dall", "Baati")
fav_food= tk.StringVar(value=food_items)

food_lists= tk.Listbox(listvariable=fav_food, height=5,  selectmode="extended")
food_lists.pack()

def get_fav_food(event):
    food_indices=food_lists.curselection()
    for i in food_indices:
        print(food_lists.get(i))

food_lists.bind("<<ListboxSelect>>", get_fav_food)

# Spinbox
counter=tk.IntVar(value=1)
def get_spin_box_value():
    print(f"Current spin box value {spin_box.get()}")

spin_box=ttk.Spinbox(values=tuple(range(5,105,5)), textvariable=counter, wrap=True, command=get_spin_box_value) #from_=0, to=20
spin_box.pack()

print(f"Initial spin box value {spin_box.get()}")

window.mainloop()