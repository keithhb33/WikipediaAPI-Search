import tkinter as tk
from tkinter import *
import wikipediaapi
import webbrowser
import sys
import os

root = tk.Tk()
wiki_wiki = wikipediaapi.Wikipedia('en')

def restart(args=None):
    os.execl(sys.executable, sys.executable, *sys.argv)

def search(args=None):
    open_search = "http://wikipedia.org/wiki/" + search_entry.get()
    page_py = wiki_wiki.page(search_entry.get())
    page_not_found = Label(root, text="", font=("Courier", 15))
    page_not_found.pack()
    if page_py.exists():
        webbrowser.open_new(open_search)
        search_another = Button(root, text="Restart Program")
    elif not page_py.exists():
        page_not_found.config(text="Page Not Found")
        search_another = Button(root, text="Restart Program to Search Again")
    search_another.bind('<Button-1>', restart)
    search_another.pack()


search_label = Label(root, text="Search Wikipedia.org", font=("Times New Roman", 25))
search_label.pack()

white = Label(root, text="")
white.pack()

search_entry = Entry(root, width=20, justify='center', font=("Courier", 15))
search_entry.focus()
search_entry.bind('<Return>', search)
search_entry.pack()

line_break = Label(root, text="")
line_break.pack()

search_button = Button(root, text="Search")
search_button.bind('<Button-1>', search)
search_button.pack()

root.geometry('300x200')
root.mainloop()
