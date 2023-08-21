import tkinter as tk


class login_menu:
    def __init__(self):
        window = tk.Tk()
        hello = tk.Label(text='Welcome to the Health Tracker!',
                         foreground='orange',
                         background='black')
        hello.pack()
        window.mainloop()
