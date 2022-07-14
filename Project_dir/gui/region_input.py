import tkinter
from logging import root
from tkinter import *

# from home import root

bkg1 = '#787A91'
clr1 = '#EEEEEE'
clr2 = '#141E61'


def show_country_region():
    pass


def region_input():
    country_region_window = Tk()
    country_region_window.title('Country/Region Input')
    country_region_window.iconbitmap('./Assets/gm_logo.ico')
    country_region_window.configure(bg=bkg1)
    country_region_window.minsize(width=900, height=600)

    def region_input_instructions():
        region_input_instruction = """
        Kindly choose a country or a region 
        to view from the dropdown list,
        then click 'Next'
        """
        r_c_instruction_label = Label(country_region_window,
                                      text=region_input_instruction,
                                      pady=25,
                                      padx=0,
                                      justify='center',
                                      border=10,
                                      background=clr1,
                                      foreground=clr2,
                                      borderwidth=2,
                                      font=('Times New Roman bold', 25))

        r_c_instruction_label.pack(pady=25)

    region_input_instructions()

    country_region_window.mainloop()
