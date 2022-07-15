import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='white', color_codes=True)
from Project_dir.api.data_analysis import *
from tkinter import *
from region_input import region_input
from tkinter import ttk
import pandasql as psql
import mysql.connector




bkg1 = '#787A91'
clr1 = '#EEEEEE'
clr2 = '#141E61'
ft = 'serif bold'
country_page = Tk()


def region_data():
    country_page.title('COVID Live Tracker')
    country_page.minsize(width=900, height=600)

    def display():
        pass

    def Visualize_data():
        pass


    def dload_data():
        return 'Hi Shatha'

    def visualize_button():
        vis_btn = Button(country_page,
                         text='Visualize Data',
                         bg=clr2,
                         height=2,
                         width=15,
                         foreground=clr1,
                         font=(ft, 15),
                         justify='center'
                         )
        vis_btn.pack()

    def back_button():
        back_btn = Button(country_page,
                          text='Back',
                          bg=clr2,
                          height=2,
                          width=15,
                          foreground=clr1,
                          font=(ft, 15),
                          justify='center',
                          command=region_input
                          )
        back_btn.pack(pady=25)

    def download_button():
        dl_btn = Button(country_page, text='Download',
                        bg=clr2,
                        height=2,
                        width=15,
                        foreground=clr1,
                        font=(ft, 15),
                        justify='center',
                        command=dload_data
                        )
        dl_btn.pack()

    visualize_button()
    back_button()
    download_button()
    country_page.mainloop()


if __name__ == '__main__':
    region_data()



