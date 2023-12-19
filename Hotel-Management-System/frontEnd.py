
def open_room_selection_window():
    # Function to open the room selection window
    room_selection_window = Toplevel()
    room_selection_window.title("Select a Room")
    room_selection_window.geometry("300x200")
    Label(room_selection_window, text="Select a Room to Book").pack(pady=10)

    Button(room_selection_window, text="Room 1", command=lambda: book_room("Room 1")).pack()
    Button(room_selection_window, text="Room 2", command=lambda: book_room("Room 2")).pack()
    Button(room_selection_window, text="Room 3", command=lambda: book_room("Room 3")).pack()
    Button(room_selection_window, text="Room 4", command=lambda: book_room("Room 4")).pack()
    Button(room_selection_window, text="Room 5", command=lambda: book_room("Room 5")).pack()

def book_room(room):
    # Function to handle room booking and display confirmation
    booking_confirmation_window = Toplevel()
    booking_confirmation_window.title("Booking Confirmation")
    booking_confirmation_window.geometry("300x200")

    customer_name = name_var.get()
    customer_from_date = from_date_entry.get()
    
    booking_message = f"You have booked {room} for\nName: {customer_name}\nDate: {customer_from_date}"
    Label(booking_confirmation_window, text=booking_message).pack(pady=10)

from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from customer import Customer
import sqlite3

conn = sqlite3.connect('guest_data_base.db')


def submit_info():
    
    c = conn.cursor()
    
    # Fetching values from entry fields
    customer_name = name_var.get()
    customer_country = country_var.get()
    customer_passport = passport_var.get()
    customer_gender = gender_var.get()
    customer_from_date = from_date_entry.get()
    customer_to_date = to_date_entry.get()

    # Validation check for empty fields
    if not (customer_name and customer_country and customer_passport and customer_gender and customer_from_date and customer_to_date):
        messagebox.showwarning("Warning", "All fields are required!")
        return

    open_room_selection_window()
    try:    
        customer_name = name_var.get()
        customer_country = country_var.get()
        customer_passport = passport_var.get()
        customer_gender = gender_var.get()
        customer_from_date = from_date_entry.get()
        customer_to_date = to_date_entry.get()

        customer = Customer(customer_name, customer_country, customer_passport, customer_gender, customer_from_date, customer_to_date)
        print(customer)

        c.execute("INSERT INTO guests (firstname, country, passport, gender, from_date, to_date) VALUES (?, ?, ?, ?, ?, ?)",
                  (customer_name, customer_country, customer_passport, customer_gender, customer_from_date, customer_to_date))

        conn.commit()
    except Exception as e:
        print("Error occurred:", e)
        conn.rollback()
    finally:   
        conn.close()

def delete_reservation():
    name_to_delete = delete_name_var.get()
    if name_to_delete:
        c = conn.cursor()
        c.execute("DELETE FROM guests WHERE firstname = ?", (name_to_delete,))
        conn.commit()
        messagebox.showinfo("Info", "Your reservation was successfully deleted")
    else:
        messagebox.showwarning("Warning", "Please enter a name")


window = Tk()
window.title("Python Hotel")
window.geometry("800x600")
window.resizable(False, False)

frame = Frame(window, bg="lightblue")
frame.pack(expand=True, fill="both")
frame.pack_propagate(False)

headline = Label(frame, text="Welcome to Tkinter Hotel!", font=("Times New Roman", 24), bg="lightblue")
headline.pack(pady=20)

user_name_label = Label(window, text="To book a room, please enter your information:", font=("Times New Roman", 20), bg="lightblue").place(x=40, y=200)

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
gender_options = ["Male", "Female"]
gender_var.set(gender_options[0])  # Default option
gender_dropdown = OptionMenu(window, gender_var, *gender_options)
gender_dropdown.place(x=250, y=360)

from_date_var = StringVar()
to_date_var = StringVar()

from_to_label = Label(window, text="From - To:", font=("Times New Roman", 16), bg="lightblue")
from_to_label.place(x=40, y=400)

from_date_entry = DateEntry(window, textvariable=from_date_var, width=15, background='darkblue', foreground='white', borderwidth=2)
from_date_entry.place(x=250, y=400)

to_date_entry = DateEntry(window, textvariable=to_date_var, width=15, background='darkblue', foreground='white', borderwidth=2)
to_date_entry.place(x=450, y=400)

submit_button = Button(window, text="Submit", command=submit_info)
submit_button.place(x=700, y=440)

Label(window, text="To delete a reservation enter your name:").pack()
delete_name_var = StringVar()
delete_name_entry = Entry(window, textvariable=delete_name_var)
delete_name_entry.pack()
Button(window, text="Delete Reservation", command=delete_reservation).pack()

def on_closing():
    conn.close()
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()

def open_room_selection_window():
    # Function to open the room selection window
    room_selection_window = Toplevel()
    room_selection_window.title("Select a Room")
    room_selection_window.geometry("300x200")
    Label(room_selection_window, text="Select a Room to Book").pack(pady=10)

    Button(room_selection_window, text="Room 1", command=lambda: book_room("Room 1")).pack()
    Button(room_selection_window, text="Room 2", command=lambda: book_room("Room 2")).pack()
    Button(room_selection_window, text="Room 3", command=lambda: book_room("Room 3")).pack()

def book_room(room):
    # Function to handle room booking and display confirmation
    booking_confirmation_window = Toplevel()
    booking_confirmation_window.title("Booking Confirmation")
    booking_confirmation_window.geometry("300x200")

    customer_name = name_var.get()
    customer_from_date = from_date_entry.get()
    
    booking_message = f"You have booked {room} for\nName: {customer_name}\nDate: {customer_from_date}"
    Label(booking_confirmation_window, text=booking_message).pack(pady=10)


