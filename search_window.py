from tkinter import *
# Create a UI class that searches for user's inputted info:
class SearchInterface:
    def __init__(self, parent):
        self.__parent = parent
        self.__new_window = Toplevel(self.__parent)
        self.__new_frame = Frame(self.__new_window, padx=10, pady=10)
        self.__new_frame.pack()
        self.__search_window()
        
        self.__new_window.mainloop()

    def __search_window(self):
        # Create another window for search entry
        window_label = Label(self.__new_frame, text="Search the info that you want to acquire.", font=('OCR A Extended', 9))
        window_label.pack()
        self.__search_entry = Entry(self.__new_frame)
        self.__search_entry.pack()

        # Create a search button
        search_button = Button(self.__new_frame, text="Search", font=('Franklin Gothic Heavy', 12), width= 10, command=self.__search_entry_by_category)
        search_button.pack(padx=10, pady=10)

    def __search_entry_by_category(self):
        # Retrieve the inputted entries from text file
        with open("log_file.txt", "r") as contacts_file:
            contacts = contacts_file.readlines()
            
            valid_contacts = []
            for contact in contacts:
                contact_info = contact.split(";")
                # Print the retrieved info
                print(contact_info)
                entry = self.__search_entry.get()
                # Print the entry
                print(entry)

    