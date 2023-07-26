from tkinter import *

class OutputWindow:
    def __init__(self, master, contacts) -> None:
        self.__output_window = Toplevel(master)
        self.__output_window.title("Search Results")

        self.__frame = Frame(self.__output_window, padx=40, pady=20)
        self.__frame.pack()

        self.__label = Label(self.__frame, text="Search Results", font=('Bauhaus 93', 12))
        self.__label.grid(row=0, column=0, columnspan=5)

        self.__contacts_label = Label(self.__frame, padx=10, pady=10)

        contacts.insert(0, "Name;Age;Address;Email Address;Vaccination Status")

        for idx, contact in enumerate(contacts):
            attributes = contact.split(";")

            for index, attribute in enumerate(attributes):

                attribute_label = Label(self.__frame, text=attribute)
                attribute_label.grid(row=idx+1, column=index)