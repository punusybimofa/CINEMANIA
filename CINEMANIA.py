import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from tabulate import tabulate

# Connect to your MySQL database
mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cinemania"
        )

cursor = mydb.cursor()

class CINEMANIA:
    def __init__(self, master):

        self.master = master
        master.title("CINEMANIA")
        master.geometry('700x400')
        self.master.configure(bg='grey1')  

        # Connect to your MySQL database
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cinemania"
        )

        self.cursor = self.mydb.cursor()

        # GUI for the main menu
        master_frame = tk.Frame(master)
        master_frame.pack()

        master_label = tk.Label(master_frame, text="Welcome to CINEMANIA!", font=('Times New Roman', 25, 'bold'), bg='red3', fg='grey2') 
        master_label.pack(ipadx=470, ipady=12)

        # Create buttons for each GUI
        movie_btn = self.create_button("MOVIE", ('Arial', 15), 'red4', 'black', 10, 'groove', self.movie_details_window)
        movie_btn.pack(pady=25)

        customer_btn = self.create_button("CUSTOMER", ('Arial', 15), 'red4', 'black', 10, 'groove', self.customer_details_window)
        customer_btn.pack(pady=25)

        payment_btn = self.create_button("PAYMENT", ('Arial', 15), 'red4', 'black', 10, 'groove', self.payment_details_window)
        payment_btn.pack(pady=25)


    def create_button(self, text, font, bg, fg, bd, relief, command=None):
        return tk.Button(self.master, text=text, font=font, bg=bg, fg=fg, bd=bd, relief=relief, command=command)

    def movie_details_window(self):
        window = tk.Toplevel(self.master)
        window.title("Movie Details")

        # Create movie data
        data = [["Spider Man 3", "Action & Adventure", "2D", "10AM - 12PM", "RM15"],
            ["Spider Man 3", "Action & Adventure", "Deluxe", "2PM - 4PM", "RM20"],
            ["Spider Man 3", "Action & Adventure", "IMAX", "6PM - 8PM", "RM25"],
            ["Spider Man 3", "Action & Adventure", "Family Session", "8PM - 10PM", "RM30"],
            ["Baymax: The Movie", "Action & Comedy", "2D", "10AM - 12PM", "RM15"],
            ["Baymax: The Movie", "Action & Comedy", "Deluxe", "2PM - 4PM", "RM20"],
            ["Baymax: The Movie", "Action & Comedy", "IMAX", "6PM - 8PM", "RM25"],
            ["Baymax: The Movie", "Action & Comedy", "Family Session", "8PM - 10PM", "RM30"],
            ["Boboiboy The Movie", "Action & Comedy", "2D", "10AM - 12PM", "RM15"],
            ["Boboiboy The Movie", "Action & Comedy", "Deluxe", "2PM - 4PM", "RM20"],
            ["Boboiboy The Movie", "Action & Comedy", "IMAX", "6PM - 8PM", "RM25"],
            ["Boboiboy The Movie", "Action & Comedy", "Family Session", "8PM - 10PM", "RM30"],
            ["The Nun", "Horror", "2D", "10AM - 12PM", "RM15"],
            ["The Nun", "Horror", "Deluxe", "2PM - 4PM", "RM20"],
            ["The Nun", "Horror", "IMAX", "6PM - 8PM", "RM25"],
            ["The Nun", "Horror", "Family Session", "8PM - 1OPM", "RM30"],
            ["Titanic", "Romance", "2D", "10AM - 12PM", "RM15"],
            ["Titanic", "Romance", "Deluxe", "2pm - 4PM", "RM20"],
            ["Titanic", "Romance", "IMAX", "6PM - 8PM", "RM25"],
            ["Titanic", "Romance", "Family Session", "8PM - 10PM", "RM30"]]

        # Define header names
        col_names = ["Movie", "Genre", "Hall", "Showtime", "Price"]

        # Display table
        dataframe = tk.Frame(window, bd=8, bg='grey1', relief='groove')
        dataframe.grid(row=0, column=0, ipadx=20)
        data_Label = tk.Label(dataframe, text='Movie Table', font='Cambria 15 bold', bg='red3', relief='raise')
        data_Label.grid(row=0, column=0, padx=10)

        movie_table = tk.Label(dataframe, text=tabulate(data, headers=col_names), justify='left', font='Courier 10 bold', bg='white', relief='sunken')
        movie_table.grid(row=1, column=0, padx=50, pady=20)

        # User information
        detailsframe = tk.Frame(window, bd=8, bg='grey1',relief='groove')
        detailsframe.grid(row=2, column=0)
        title_Label = tk.Label(detailsframe, text='Title', bg='red1', relief='ridge')
        title_Label.grid(row=0, column=0, padx=10, pady=10)
        title = ttk.Combobox(detailsframe,
                             values=['Spider Man 3  (Action & Adventure)', 'Baymax: The Movie (Action & Comedy)',
                                     'Boboiboy The Movie (Action & Comedy)', 'The Nun (Horror)', 'Titanic (Romance)'])
        title.grid(row=1, column=0, padx=50, ipadx=55)

        hall_Label = tk.Label(detailsframe, text='Hall', bg='red1', relief='ridge')
        hall_Label.grid(row=0, column=1, padx=5, pady=3)
        hall = ttk.Combobox(detailsframe, values=["2D (classic) = RM15", "Deluxe =RM20", "IMAX (Grand Theatre)= RM25",
                                                  "Family Session=RM30"])
        hall.grid(row=1, column=1, padx=5, ipadx=30)

        showtime_Label = tk.Label(detailsframe, text='Showtime', bg='red1', relief ='ridge')
        showtime_Label.grid(row=2, column=0, padx=20, pady=20)
        showtime = ttk.Combobox(detailsframe, values=['10AM - 12PM', '2PM - 4PM', '6PM - 8PM', '8PM - 10PM'])
        showtime.grid(row=3, column=0, ipadx=55)

        seat_Label = tk.Label(detailsframe, text='Seat No.',bg='red1', relief='ridge')
        seat_Label.grid(row=2, column=1, padx=10, pady=10)
        seat_frame = tk.Frame(detailsframe, bd=8)
        seat_frame.grid(row=3, column=1, rowspan=5)
        seat = tk.Listbox(seat_frame, selectmode='multiple', font='Courier 10', bg='white')
        seat.pack(side='left')
        seat_scrollbar = tk.Scrollbar(seat_frame,bg='red1',command=seat.yview)
        seat_scrollbar.pack(side='right', fill='y')
        seat.insert(1, "1A", "2A", "3A", "4A", "5A", "6A", "7A", "8A", "9A", "10A", "1B", "2B", "3B", "4B", "5B", "6B", "7B",
                    "8B", "9B", "10B",
                    "1C", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "1D", "2D", "3D", "4D", "5D", "6D", "7D", "8D",
                    "9D", "10D",
                    "1E", "2E", "3E", "4E", "5E", "6E", "7E", "8E", "9E", "10E", "1F", "2F", "3F", "4F", "5F", "6F", "7F", "8F",
                    "9F", "10F")

        # Create a cursor object to interact with the database
        self.cursor = self.mydb.cursor()

        def enter_data():
            try:
                # Get the selected indices from the Listbox
                selected_indices = seat.curselection()

                # Check if any seat is selected
                if not selected_indices:
                    messagebox.showerror("Error", "Please select at least one seat.")
                    return

                # Get the selected seats using the indices
                selected_seats = [seat.get(index) for index in selected_indices]

                # Inserting data into a table
                sql = "INSERT INTO movie_info (Title, Hall, Showtime, Seat) VALUES (%s, %s, %s, %s)"
                val = (title.get(), hall.get(), showtime.get(), ', '.join(selected_seats))
                
                cursor.execute(sql, val)
                mydb.commit()
                print("Data inserted successfully!")

                # Get selected movie information
                selected_movie = title.get().split('(')[0].strip()
                selected_hall = hall.get().split('=')[0].strip()
                selected_showtime = showtime.get()

                # Show a messagebox with information about successful insertion
                messagebox.showinfo("Success", f"Data inserted successfully!\n\n"
                                        f"Movie: {selected_movie}\n"
                                        f"Hall: {selected_hall}\n"
                                        f"Showtime: {selected_showtime}\n"
                                        f"Seats: {', '.join(selected_seats)}")

            except mysql.connector.Error as err:
                print(f"Error: {err}")
                self.mydb.rollback()
                
                # Optional: Display an error message to the user
                messagebox.showerror("Error", f"Error inserting data: {err}")

            finally:
                self.cursor.close()

        def update_database():
            try:
                new_movie = title.get()
                new_hall = hall.get()
                new_showtime = showtime.get()

                # Get the selected indices from the Listbox
                selected_indices = seat.curselection()

                # Check if any seat is selected
                if not selected_indices:
                    messagebox.showerror("Error", "Please select at least one seat.")
                    return

                # Get the selected seats using the indices
                selected_seats = [seat.get(index) for index in selected_indices]

                # Updating data in the table including selected seats
                sql = "UPDATE movie_info SET Title=%s, Hall=%s, Seat=%s WHERE Showtime=%s"
                val = (new_movie, new_hall, ', '.join(selected_seats), new_showtime)

                cursor.execute(sql, val)
                mydb.commit()
                print("Data updated successfully!")

                # Optional: Display a message to the user indicating a successful update
                messagebox.showinfo("Success", "Data updated successfully!")

            except mysql.connector.Error as err:
                print(f"Error: {err}")
                self.mydb.rollback()
                # Optional: Display an error message to the user
                messagebox.showerror("Error", f"Error updating data: {err}")

            finally:
                self.cursor.close()

        def delete_data():
            try:
                # Get the selected indices from the Listbox
                selected_indices = seat.curselection()

                # Check if any seat is selected
                if not selected_indices:
                    messagebox.showerror("Error", "Please select at least one seat.")
                    return

                # Get the selected seats using the indices
                selected_seats = [seat.get(index) for index in selected_indices]

                # Deleting data from the table based on Seat
                sql = "DELETE FROM movie_info WHERE Title=%s AND Hall=%s AND Showtime=%s AND Seat =%s"
                val = (title.get(), hall.get(), showtime.get(), ', '.join(selected_seats))
                
                cursor.execute(sql, val)
                mydb.commit()
                print("Data deleted successfully!")

                # Optional: Display a message to the user indicating a successful deletion
                messagebox.showinfo("Success", "Data deleted successfully!")

            except mysql.connector.Error as err:
                print(f"Error: {err}")
                self.mydb.rollback()
                
                # Optional: Display an error message to the user
                messagebox.showerror("Error", f"Error deleting data: {err}")

            finally:    
                # Close the cursor and the database connection
                self.cursor.close()
                self.mydb.close()

        # Create button to enter data into the table
        enter_button = tk.Button(detailsframe, text="ENTER", bg='red1',relief='raise', command=enter_data)
        enter_button.grid(row=0, column=2, rowspan=3, padx=40, ipady=15, ipadx=30)

        # Create button to update data in the table
        update_button = tk.Button(detailsframe, text="UPDATE", bg='red1', relief='raise',command=update_database)
        update_button.grid(row=2, column=2, rowspan=3, padx=40, ipady=15, ipadx=25)

        # Create button to delete data from the table
        delete_button = tk.Button(detailsframe, text="DELETE", bg='red1' , relief='raise', command=delete_data)
        delete_button.grid(row=4, column=2, rowspan=3, padx=40, ipady=15, ipadx=27)



################################################################### CUSTOMER ###################################################################
    
    def customer_details_window(self):
        customer_window = tk.Toplevel(self.master)
        customer_window.title("Customer Details")
        customer_window.configure(bg='grey1')

        # Create and place widgets
        label_name = tk.Label (customer_window, text= "Name:", bg='red1', relief='ridge')
        label_name.grid (row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_name = tk.Entry(customer_window)
        self.entry_name.grid (row=0, column=1, padx=10, pady=5, ipadx=30)

        label_email = tk.Label (customer_window, text="E-mail:", bg='red1', relief='ridge')
        label_email.grid (row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_email = tk.Entry (customer_window)
        self.entry_email.grid (row=1, column=1, padx=10, pady=5, ipadx=30)

        label_phone = tk.Label (customer_window, text="Phone Number:", bg='red1', relief='ridge')
        label_phone.grid (row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_phone = tk.Entry (customer_window)
        self.entry_phone.grid(row=2, column=1, padx=10, pady=5, ipadx=30)

        save_button = tk.Button (customer_window, text="SAVE", bg='red1', relief='raise', command=self.save_customer)
        save_button.grid (row=4, column=1, columnspan=1, pady=10, padx=40, ipady=8, ipadx=20)

        #Create button to update data in the table
        update_button = tk.Button(customer_window, text="UPDATE",bg='red1', relief='raise', command=self.update_database_customer)
        update_button.grid(row=5, column=1, columnspan=5, pady=5, padx=40, ipady=8, ipadx=13)

        # Create button to delete data from the table
        delete_button = tk.Button(customer_window, text="DELETE",bg='red1',relief='raise',command=self.delete_data_customer)
        delete_button.grid(row=6, column=1, columnspan=2, pady= 6, padx=40, ipady=8, ipadx=15)

    def save_customer(self):

        customer_name = self.entry_name.get()
        email = self.entry_email.get()
        phone_number = self.entry_phone.get()

        # Display a message box with the collected information
        message=f"Name: {customer_name}\nE-mail: {email}\nPhone Number: {phone_number}"
        messagebox.showinfo ("Customer Information", message)

        sql = "INSERT INTO customer_details (cus_name, cus_email, cus_phone_number) VALUES (%s, %s, %s)"
        val = (customer_name, email, phone_number)

        try:
            cursor.execute(sql, val)
            mydb.commit()
            print('Data inserted successfully!')
        except mysql.connector.Error as err:
            print(f'Error:{err}')
            self.mydb.rollback()
        
        finally:
            self.cursor.close()
            self.mydb.close()

    def update_database_customer(self):
        try:
            new_name = self.entry_name.get()
            new_email = self.entry_email.get()
            new_phone = self.entry_phone.get()

            # Updating data in the table for a specific customer based on their name
            sql = "UPDATE customer_details SET cus_name=%s, cus_email=%s WHERE cus_phone_number=%s"
            val = (new_name, new_email, new_phone)

            cursor.execute(sql, val)
            mydb.commit()
            print("Data updated successfully!")

            # Optional: Display a message to the user indicating a successful update
            messagebox.showinfo("Success", "Data updated successfully!")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.mydb.rollback()
            # Optional: Display an error message to the user
            messagebox.showerror("Error", f"Error updating data: {err}")

        finally:    
            self.cursor.close()
        

    def delete_data_customer(self):

        try:
            # Fetch the current values from entry widgets
            name = self.entry_name.get()
            email = self.entry_email.get()
            phone = self.entry_phone.get()

            # Deleting data from the table based on Seat
            sql = "DELETE FROM customer_details WHERE cus_name=%s AND cus_email=%s AND cus_phone_number=%s"
            val = (name, email, phone)
            
            cursor.execute(sql, val)
            mydb.commit()
            print("Data deleted successfully!")

            # Optional: Display a message to the user indicating a successful deletion
            messagebox.showinfo("Success", "Data deleted successfully!")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.mydb.rollback()
            # Optional: Display an error message to the user
            messagebox.showerror("Error", f"Error deleting data: {err}")

        finally:
            self.cursor.close()
            self.mydb.close()
        
#################################################################  payment  #######################################################################
            
    def payment_details_window(self):
        payment_window = tk.Toplevel(self.master)
        payment_window.title("Payment Details")
        payment_window.configure(bg='grey1')
        # Payment Frame
        payment_details_frame = tk.LabelFrame(payment_window, text="Payment", bg='gray25', fg='white')
        payment_details_frame.grid(row=1, column=0, padx=30, pady=20,columnspan=3)

        method_of_payment_label = tk.Label(payment_details_frame, text="Method of Payment", bg='red1', relief='ridge')
        self.method_of_payment_combobox = ttk.Combobox(payment_details_frame, values=["Master Card", "VISA", "Apple pay"])
        method_of_payment_label.grid(row=0, column=0)
        self.method_of_payment_combobox.grid(row=1, column=0)

        card_num_label = tk.Label(payment_details_frame, text="Card Number",bg='red1', relief='ridge')
        card_num_label.grid(row=0, column=1)
        expired_date_label = tk.Label(payment_details_frame, text="Expired Date", bg='red1', relief='ridge')
        expired_date_label.grid(row=0, column=2)
        sec_code_label = tk.Label(payment_details_frame, text="CVV/CVC", bg='red1', relief='ridge')
        sec_code_label.grid(row=0, column=3)

        self.card_num_entry = tk.Entry(payment_details_frame)
        self.expired_date_entry = tk.Entry(payment_details_frame)
        self.sec_code_entry = tk.Entry(payment_details_frame)
        self.card_num_entry.grid(row=1, column=1)
        self.expired_date_entry.grid(row=1, column=2)
        self.sec_code_entry.grid(row=1, column=3)

        for widget in payment_details_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        # Movie Ticket Cost Calculation Frame
        frame = tk.Frame(payment_window)
        frame.grid(row=0, column=0,columnspan=3)
        frame.configure(bg='gray25')

        hall_label = tk.Label(frame, text="Select Movie Hall:", bg='red1', relief='ridge')
        self.hall_combobox = ttk.Combobox(frame, values=["2D", "Deluxe", "IMAX", "Family Session"])
        hall_label.grid(row=0, column=0, padx=10, pady=5)
        self.hall_combobox.grid(row=1, column=0, padx=10, pady=5)

        num_tickets_label = tk.Label(frame, text="Number of Tickets:", bg='red1', relief='ridge')
        self.num_tickets_entry = tk.Entry(frame)
        num_tickets_label.grid(row=0, column=1, padx=10, pady=5)
        self.num_tickets_entry.grid(row=1, column=1, padx=10, pady=5)

        calculate_button = tk.Button(frame, text="Calculate", bg='red1', relief='ridge', command=self.calculate_cost)
        calculate_button.grid(row=1, column=2, pady=10, ipadx=20)

        self.result_label = tk.Label(frame, text="", bg='white')
        self.result_label.grid(row=5, column=0, pady=5)

        # Submission and Control Buttons
        submit_button = tk.Button(payment_window, text="SUBMIT", bg='red1', relief='raise', command=self.enter_data_payment)
        submit_button.grid(row=2, column=0, pady=5,padx=2, ipadx=30)

        update_button = tk.Button(payment_window, text="UPDATE", bg='red1', relief='raise', command=self.update_database_payment)
        update_button.grid(row=2, column=1, pady=5,padx=2, ipadx=30) 

        delete_button = tk.Button(payment_window, text="DELETE", bg='red1', relief='raise' ,command=self.delete_data_payment)
        delete_button.grid(row=2, column=2, pady=5, padx=2, ipadx=30)

    def calculate_cost(self):
        selected_hall = self.hall_combobox.get()
        num_tickets = int(self.num_tickets_entry.get())

        hall_prices = {
            "2D": 15,
            "Deluxe": 20,
            "IMAX": 25,
            "Family Session": 30
        }

        if selected_hall in hall_prices:
            ticket_price = hall_prices[selected_hall]
            total_cost = num_tickets * ticket_price
            self.result_label.config(text=f"Total Cost: RM {total_cost}")
        else:
            self.result_label.config(text="Invalid Hall Selection")

    def enter_data_payment(self):
        method_of_payment = self.method_of_payment_combobox.get()
        card_number = self.card_num_entry.get()
        expired_date = self.expired_date_entry.get()
        cvv_cvc = self.sec_code_entry.get()

        selected_hall = self.hall_combobox.get()
        num_tickets = int(self.num_tickets_entry.get())

        hall_prices = {
            "2D": 15,
            "Deluxe": 20,
            "IMAX": 25,
            "Family Session": 30
        }

        if selected_hall in hall_prices:
            ticket_price = hall_prices[selected_hall]
            total_cost = num_tickets * ticket_price

            # Create a popup window with the collected information and total cost
            popup = tk.Toplevel(self.master)
            popup.title("Payment Details")

            # Calculate the right side position of the popup window
            right_position = self.master.winfo_x() + self.master.winfo_width()

            # Set the geometry of the popup window to appear on the right side
            popup.geometry(f"+{right_position}+{self.master.winfo_y()}")

            message = f"Method of Payment: {method_of_payment}\nCard Number: {card_number}\nExpired Date: {expired_date}\nSecurity Code: {cvv_cvc}\nCost: RM {total_cost}"
            label = tk.Label(popup, text=message, padx=10, pady=10)
            label.pack()

            # Optionally, you can add OK button to close the popup
            ok_button = tk.Button(popup, text="OK", command=popup.destroy)
            ok_button.pack()

        try:

            sql = "INSERT INTO payment_info (Method_of_Payment, card_number, expired_date, CVV_CVC, total_cost) VALUES (%s, %s, %s, %s, %s)"
            val = (method_of_payment, card_number, expired_date, cvv_cvc, total_cost)
            
            cursor.execute(sql, val)
            mydb.commit()
            print("Data inserted successfully")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.mydb.rollback()

        else:
            self.result_label.config(text="Invalid Hall Selection")

        finally:
            self.cursor.close()    

    def update_database_payment(self):
        try:
            new_method = self.method_of_payment_combobox.get()
            new_card_num = self.card_num_entry.get()
            new_expired_date = self.expired_date_entry.get()
            new_code = self.sec_code_entry.get()

            # Updating data in the table for a specific customer based on their name
            sql = "UPDATE payment_info SET Method_of_Payment=%s, card_number=%s, expired_date=%s WHERE CVV_CVC=%s"
            val = (new_method, new_card_num, new_expired_date, new_code )

            cursor.execute(sql, val)
            mydb.commit()
            print("Data updated successfully!")

            # Optional: Display a message to the user indicating a successful update
            messagebox.showinfo("Success", "Data updated successfully!")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.mydb.rollback()
            # Optional: Display an error message to the user
            messagebox.showerror("Error", f"Error updating data: {err}")

        finally:
            self.cursor.close()

    def delete_data_payment(self):
        try:
            # Deleting data from the table based on Seat
            sql = "DELETE FROM payment_info WHERE Method_of_Payment=%s AND card_number=%s AND expired_date=%s AND CVV_CVC=%s"
            val = (self.method_of_payment_combobox.get(), self.card_num_entry.get(), self.expired_date_entry.get(), self.sec_code_entry.get())
            

            cursor.execute(sql, val)
            mydb.commit()
            print("Data deleted successfully!")

            # Optional: Display a message to the user indicating a successful deletion
            messagebox.showinfo("Success", "Data deleted successfully!")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.mydb.rollback()
            # Optional: Display an error message to the user
            messagebox.showerror("Error", f"Error deleting data: {err}")
        
        finally:
            self.cursor.close()
            self.mydb.close()
        

    

# Create an instance of the CINEMANIA class
def main(): 
    root = tk.Tk()
    app = CINEMANIA(root)
    root.mainloop()

if __name__ == "__main__":
    main()

cursor.close()
mydb.close()
