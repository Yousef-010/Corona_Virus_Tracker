import tkinter
import home
import pandas as pd
import country_output
import region_output
from tkinter import *
import Project_dir.api.data_analysis as da

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
        # hello = home.home_window().user_name_input()
        region_input_instruction = """Kindly choose a country or a region 
        to view from the dropdown list,
        then click 'Next'"""
        r_c_instruction_label = Label(country_region_window,
                                      text=region_input_instruction,
                                      pady=25,
                                      padx=25,
                                      justify='center',
                                      border=10,
                                      background=clr1,
                                      foreground=clr2,
                                      borderwidth=2,
                                      font=('Times New Roman bold', 25))

        r_c_instruction_label.pack(pady=25)

    def country_region_back():
        country_region_window.destroy()
        home.home_window()

    def country_region_next_button():
        next_btn = Button(country_region_window,
                          text='Next',
                          command=country_region_next,
                          bg=clr2,
                          height=2,
                          width=15,
                          foreground=clr1,
                          font=('serif bold', 15),
                          justify='center')

        next_btn.pack(side='right', pady=50)

    def country_region_back_button():
        back_btn = Button(country_region_window,
                          text='Back',
                          command=country_region_back,
                          bg=clr2,
                          height=2,
                          width=15,
                          foreground=clr1,
                          font=('serif bold', 15),
                          justify='center')

        back_btn.pack(side='left', pady=150)
        # next_btn.pack(side='right', padx=100, pady=50)
    g_c, b_c = da.get_report_based_on_avg_of_survivors()
    countries = g_c + b_c

    def country_list():
        clicked_country = StringVar()
        clicked_country.set('Choose a Country')
        country_choice = clicked_country.get()
        country_drop_list = OptionMenu(country_region_window, clicked_country, *countries)
        country_drop_list.pack(pady=25, padx=25)
        return country_choice

    regions = [
        'Middle East',
        'Europe'
    ]

    def region_list():
        clicked_region = StringVar()
        clicked_region.set('Choose a Region')
        region_choice = clicked_region.get()
        reg_drop_list = OptionMenu(country_region_window, clicked_region, *regions)
        reg_drop_list.pack(pady=25, padx=25)
        return region_choice

    def country_region_next():
        country_choice = country_list()
        region_choice = region_list()
        if country_choice:
            country_region_window.destroy()
            country_output.country_data()
        elif region_choice:
            country_region_window.destroy()
            region_output.region_data()
        else:
            return 'ERROR MSG'

    region_input_instructions()
    region_list()
    country_list()
    country_region_next_button()
    country_region_back_button()

    country_region_window.mainloop()


# if __name__ == '__main__':
#     region_input()
