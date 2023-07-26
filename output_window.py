from tkinter import *

class OutputWindow:
    def __init__(self, master, contacts) -> None:
        self.__output_window = Toplevel(master)
        self.__output_window.title("Search Results")

        self.__frame = Frame(self.__output_window, padx=40, pady=20)
        self.__frame.pack()

        self.__label = Label(self.__frame, text="Search Results", font=('Bauhaus 93', 12))
        self.__label.pack()
        