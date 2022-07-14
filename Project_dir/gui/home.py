# import tkinter as tk
from tkinter import *
# from pill import imageTK, image
import region_input

bkg1 = '#787A91'
clr1 = '#EEEEEE'
clr2 = '#141E61'
# bgimg = PhotoImage(file='Project_dir/gui/Assets/img.ico')


def home_window():
    root = Tk()
    root.title('COVID Live Tracker')
    root.iconbitmap('./Assets/gm_logo.ico')
    root.configure(bg=bkg1)
    root.minsize(width=900, height=600)

    def welcome_msg():
        # home.geometry('700x500')
        welcome = Label(root, text="""Welcome To COVID Live Tracker
        Your COVID Related Stats Viewer, Analyzer and Downloader 
         To Proceed, Please Click 'Next'""",
                        pady=25,
                        padx=0,
                        border=10,
                        background=clr1,
                        foreground=clr2,
                        borderwidth=2,
                        font=('Times New Roman bold', 30))

        welcome.pack(pady=25)

    def user_name_input():
        user_name = Entry(root, width=25,
                          font=('Andalus', 20),
                          bg=clr2,
                          bd=2.5,
                          foreground=clr1,
                          justify='center',
                          borderwidth=5)

        user_name.pack(pady=25)
        user_name.insert(0, 'Please Enter Your Name')
        name = str(user_name.get())
        return 'Hello ' + name.capitalize()

    def user_profession():
        prof = StringVar(root)
        prof.set('Please Enter Your Profession')
        user_prof = Entry(root, textvariable=prof,
                          width=25,
                          font=('Andalus', 20),
                          bg=clr2,
                          bd=2.5,
                          foreground=clr1,
                          justify='center',
                          borderwidth=5)

        user_prof.pack(pady=25)
        # user_prof.insert(0, 'Please Enter Your Profession')
        profession = user_prof.get()
        return profession

    def home_next():
        root.destroy()
        region_input.region_input()

    def next_button():
        next_btn = Button(root,
                          text='Next',
                          command=home_next,
                          bg=clr2,
                          height=2,
                          width=15,
                          foreground=clr1,
                          font=('serif bold', 15),
                          justify='center')

        next_btn.pack(pady=50)
        # next_btn.pack(side='right', padx=100, pady=50)

    """
    1. Replace text (on-click)
    """

    welcome_msg()
    user_profession()
    user_name_input()

    next_button()

    root.mainloop()


"""
2. Set Root and Frame
3. Change Background
"""

if __name__ == '__main__':
    home_window()