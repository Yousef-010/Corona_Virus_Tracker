import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='white', color_codes=True)
from Project_dir.api.data_analysis import *
from tkinter import *
import region_input
from tkinter import ttk


bkg1 = '#787A91'
clr1 = '#EEEEEE'
clr2 = '#141E61'
ft = 'serif bold'


def country_data():
    country_page = Tk()
    country_page.title('Country_page')
    country_page.minsize(width=900, height=600)

    # def download():
    #     pass

    def dload_data():
        print('Download Button from country_page')

    def back_function():
        country_page.destroy()
        region_input.region_input()

    def visualize_data():
        print('visualize button from country_page')

    def visualize_button():
        vis_btn = Button(country_page,
                         text='Visualize Data',
                         bg=clr2,
                         height=2,
                         width=15,
                         foreground=clr1,
                         font=(ft, 15),
                         justify='center',
                         command= visualize_data
                         )
        vis_btn.pack(pady=50)

    def back_button():
        back_btn = Button(country_page,
                          text='Back',
                          bg=clr2,
                          height=2,
                          width=15,
                          foreground=clr1,
                          font=(ft, 15),
                          justify='center',
                          command=back_function
                          )
        back_btn.pack()

    def download_button():
        dl_btn = Button(country_page, text='Download',
                        bg=clr2,
                        height=2,
                        width=15,
                        foreground=clr1,
                        font=(ft, 15),
                        justify='center',
                        command = dload_data
                        )
        dl_btn.pack()

    visualize_button()
    back_button()
    download_button()
    country_page.mainloop()


# if __name__ == '__main__':
#     country_data()
