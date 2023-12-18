from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from customer import Customer

def submit_info():
    customer_name = name_var.get()
    customer_country = country_var.get()
    customer_passport = passport_var.get()
    customer_gender = gender_var.get()
    customer_from_date = from_date_var.get()
    customer_to_date = to_date_var.get()

    customer = Customer(customer_name, customer_country, customer_passport, customer_gender, customer_from_date, customer_to_date)
    print(customer)
    show_accommodation_frame()

def show_accommodation_frame():
    accommodation_frame = Frame(window, bg="lightblue")
    headline_accommodation = Label(accommodation_frame, text="Select Accommodation Type:", font=("Times New Roman", 20), bg="lightblue")
    headline_accommodation.pack(pady=20)

    # Accommodation dropdown
    accommodation_label = Label(accommodation_frame, text="Accommodation:", font=("Times New Roman", 16), bg="lightblue")
    accommodation_label.pack()

    accommodation_options = get_accommodation_options(gender_var.get())
    accommodation_var.set(accommodation_options[0])  # Default option
    OptionMenu(accommodation_frame, accommodation_var, *accommodation_options).pack(pady=10)

    submit_button = Button(accommodation_frame, text="Book Now", command=show_success_message, bg="green", fg="white", font=("Times New Roman", 14))
    submit_button.pack(pady=20)

    accommodation_frame.pack_forget()
    accommodation_frame.pack()

def show_success_message():
    message = f"Booking successful!\nName: {name_var.get()}\nAccommodation: {accommodation_var.get()}"
    messagebox.showinfo("Success", message)

def get_accommodation_options(selected_gender):
    # Define the initial accommodation options with maximum places
    accommodation_options = {
        "male": {" male dorm ": 4},
        "female": {"female dorm ": 4},
        "blank": {"2 double room": 2, "5 single room": 5}
    }

    selected_gender = selected_gender.lower()
    if selected_gender not in accommodation_options:
        selected_gender = "blank"  # Default to blank if an invalid gender is specified

    options = accommodation_options[selected_gender]

    # Filter out options with no available places
    available_options = [option for option, places_left in options.items() if places_left > 0]

    return available_options

window = Tk()
window.title("Junkie House")
window.geometry("800x600")
window.resizable(False, False)
window.configure(bg="lightblue")

frame = Frame(window, bg="lightblue")
frame.pack(expand=True, fill="both")
frame.pack_propagate(False)

headline = Label(frame, text="Welcome to Junkie House!", font=("Times New Roman", 24), bg="lightblue")
headline.pack(pady=20)

user_name_label = Label(window, text="To book a room, please enter your information:", font=("Times New Roman", 20), bg="lightblue")
user_name_label.place(x=40, y=200)

# Entry fields
name_var = StringVar()
name_label = Label(window, text="Name:", font=("Times New Roman", 16), bg="lightblue")
name_label.place(x=40, y=240)
name_entry = Entry(window, textvariable=name_var, width=30)
name_entry.place(x=250, y=240)

country_var = StringVar()
country_label = Label(window, text="Country:", font=("Times New Roman", 16), bg="lightblue")
country_label.place(x=40, y=280)
country_entry = Entry(window, textvariable=country_var, width=30)
country_entry.place(x=250, y=280)

passport_var = StringVar()
passport_label = Label(window, text="Passport:", font=("Times New Roman", 16), bg="lightblue")
passport_label.place(x=40, y=320)
passport_entry = Entry(window, textvariable=passport_var, width=30)
passport_entry.place(x=250, y=320)

gender_var = StringVar()
gender_label = Label(window, text="Gender:", font=("Times New Roman", 16), bg="lightblue")
gender_label.place(x=40, y=360)
gender_options = ["", "Male", "Female"]  # Updated options with a blank value
gender_var.set(gender_options[0])  # Default option
gender_dropdown = OptionMenu(window, gender_var, *gender_options)
gender_dropdown.place(x=250, y=360)

from_date_var = StringVar()
to_date_var = StringVar()

from_to_label = Label(window, text="From - To:", font=("Times New Roman", 16), bg="lightblue")
from_to_label.place(x=40, y=400)

from_date_entry = DateEntry(window, textvariable=from_date_var, width=15, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd-mm-yyyy')
from_date_entry.place(x=250, y=400)

to_date_entry = DateEntry(window, textvariable=to_date_var, width=15, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd-mm-yyyy')
to_date_entry.place(x=450, y=400)

accommodation_var = StringVar()

submit_button = Button(window, text="Submit", command=submit_info, bg="blue", fg="white", font=("Times New Roman", 16))
submit_button.place(x=700, y=440)

window.mainloop()
