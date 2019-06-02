from tkinter import Button
from tkinter import END
from tkinter import Entry
from tkinter import Label
from tkinter import Listbox
from tkinter import Scrollbar
from tkinter import StringVar
from tkinter import Tk

from backend import Database

database = Database("books.db")

class Window(object):
    def __init__(self, window):
        self.window = window
        self.windows.wm_title("BookStore")

        l1 = Label(window, text="Title")
        l1.grid(row=0, column=0)

        l2 = Label(window, text="Author")
        l2.grid(row=0, column=2)

        l3 = Label(window, text="Year")
        l3.grid(row=1, column=0)

        l4 = Label(window, text="ISBN")
        l4.grid(row=1, column=2)

        title_text = StringVar()
        e1 = Entry(window, textvariable=title_text)
        e1.grid(row=0, column=1)

        author_text = StringVar()
        e2 = Entry(window, textvariable=author_text)
        e2.grid(row=0, column=3)

        year_text = StringVar()
        e3 = Entry(window, textvariable=year_text)
        e3.grid(row=1, column=1)

        isbn_text = StringVar()
        e4 = Entry(window, textvariable=isbn_text)
        e4.grid(row=1, column=3)

        list1 = Listbox(window, height=6, width=35)
        list1.grid(row=2, column=0, rowspan=6, columnspan=2)

        list1.bind('<<ListboxSelect>>', get_selected_row)

        sb1 = Scrollbar(window)
        sb1.grid(row=2, column=2, rowspan=6)

        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)

        b1 = Button(window, text="View all", width=12, command=view_command)
        b1.grid(row=2, column=3)

        b2 = Button(window, text="Search entry", width=12, command=search_command)
        b2.grid(row=3, column=3)

        b3 = Button(window, text="Add Entry", width=12, command=add_command)
        b3.grid(row=4, column=3)

        b4 = Button(window, text="Update Selected", width=12, command=update_command)
        b4.grid(row=5, column=3)

        b5 = Button(window, text="Delete Selected", width=12, command=delete_command)
        b5.grid(row=6, column=3)

        b6 = Button(window, text="Close", width=12, command=window.destroy)
        b6.grid(row=7, column=3)


    def get_selected_row(self, event):
        try:
            global selected_tuple
            index = self.list1.curselection()[0]
            self.selected_tuple = list1.get(index)
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)
            self.e1.insert(END, self.selected_tuple[1])
            self.e2.insert(END, self.selected_tuple[2])
            self.e3.insert(END, self.selected_tuple[3])
            self.e4.insert(END, self.selected_tuple[4])
        except:
            pass

            
    def view_command():
        self.list1.delete(0, END)
        for row in database.view():
            self.list1.insert(END, row)


    def search_command():
        self.list1.delete(0, END)
        for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
            self.list1.insert(END, row)


    def add_command():
        database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))


    def delete_command():
        database.delete(self.selected_tuple[0])


    def update_command():
        database.update(self.selected_tuple[0], self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())

window = Tk()
Windows(window)
window.mainloop()
