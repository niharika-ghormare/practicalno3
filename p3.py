import tkinter as *
import mysql.connector

def book_flight():
    # Get the selected values from the dropdowns
    selected_ticket = ticket_var.get()
    selected_flight = flight_var.get()
    selected_date = date_var.get()
    selected_destination = destination_var.get()
    selected_seat = seat_var.get()
    selected_time = time_var.get()
    selected_passenger = passenger_var.get()

    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ABCD1234",
        database="flight"
    )
    cursor = connection.cursor()

    # Insert the ticket into the database
    sql = "INSERT INTO flight.ticket (t_no,flight_no,DATE,Destination,seat_no,TIME,passenger_id) VALUES (%d, %d, %s,%s,%s,%s,%d)"
    values = (selected_ticket,selected_flight ,selected_date,selected_destination,selected_seat,selected_time,selected_passenger)
    cursor.execute(sql, values)
    connection.commit()

    # Close the database connection
    cursor.close()
    connection.close()

    # Display a confirmation message
    confirmation_label.config(text="Booking successful!")

# Create the main window
window = Tk()
root.geometry("600x300")
window.title("Flight Booking System")

# Create and pack the labels
tid = Label(window, text="Ticket no:",font=("bold",12))
tid.place(x=20,y=30)

fno = tk.Label(window, text="Flight no:",font=("bold",12))
fno.place(x=20,y=60)

date = tk.Label(window, text="Date ",font=("bold",12))
dat

from_label = tk.Label(window, text="Destimation",font=("bold",12))
from_label.pack()

from_label = tk.Label(window, text="Seat no",font=("bold",12))
from_label.pack()

from_label = tk.Label(window, text="Time",font=("bold",12))
from_label.pack()

from_label = tk.Label(window, text="Passenger ID",font=("bold",12))
from_label.pack()

# Create and pack the book button
book_button = tk.Button(window, text="Book Flight", command=book_flight)
book_button.pack()

# Create and pack the confirmation label
confirmation_label = tk.Label(window, text="")
confirmation_label.pack()

# Run the main window loop
window.mainloop()

