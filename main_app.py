# Ken Leam G. Gamboa
# BSCPE 1-5
# Creating a COVID-19 Contact Tracing App

from tkinter import *
from tkinter import ttk
# Create a UI class that asks for user's contact info
class GUI:
    def __init__(self):
        self.__main_window = Tk()
        self.__frame = Frame(self.__main_window, padx=10, pady=10)
        self.__frame.grid(column=0, row=0)
        self.__main_window.columnconfigure(0, weight=1)
        self.__main_window.rowconfigure(0, weight=1)

        TITLE = Label(self.__frame, text="COVID-19 Contact Tracing App", font= ('Bauhaus 93', 23))
        TITLE.grid(row=0, column=0, columnspan=2, pady=10)

        self.__entries = []

        # Ask for user's name
        name = user_entry(self.__frame, 'Name: ')
        self.__entries.append(name)
        # Ask for user's age
        age = user_entry(self.__frame, 'Age: ')
        self.__entries.append(age)
        # Ask for user's address
        address = user_entry(self.__frame, 'Address: ')
        self.__entries.append(address)
        # Ask for user's email address
        email_address = user_entry(self.__frame, 'Email: ')
        self.__entries.append(email_address)
        # Ask for user's vaccination status
        vaccination_label = Label(self.__frame, text="Vaccination Status: ", font= ('OCR A Extended', 12))
        vaccination_label.grid(row=self.__frame.grid_size()[1], column=0, pady=10)
        vaccination_status = ttk.Combobox(self.__frame, values=["None", "1st Dose", "2nd Dose", "1st Booster Shot", "Second Booster Shot"], width = 37)
        vaccination_status.grid(row=self.__frame.grid_size()[1] - 1, column=1, pady=10)
        self.__entries.append(vaccination_status)
        
        self.__main_window.mainloop()
        
def user_entry(master, user_name):
    entry_label = Label(master, text=user_name, font= ('OCR A Extended', 12))
    entry = Entry(master, width = 40)
    entry_label.grid(row=master.grid_size()[1], column=0)
    entry.grid(row=master.grid_size()[1] - 1, column=1)

    return entry
        
# Create a UI class that searches for user's inputted info
GUI()