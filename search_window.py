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
        window_label = Label(self.__new_frame, text="Search the info that you want to acquire.", font=('OCR A Extended', 9))
        window_label.pack()
        self.__search_entry = Entry(self.__new_frame)
        self.__search_entry.pack()

        search_button = Button(self.__new_frame, text="Search", font=('Franklin Gothic Heavy', 12), width= 10)
        search_button.pack(padx=10, pady=10)
    