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


def region_data():
    region_page = Tk()
    region_page.title('Region_page')
    region_page.minsize(width=900, height=600)

    def display():
        pass

    def back_function():
        region_page.destroy()
        region_input.region_input()

    def Visualize_data():
        print('visualize Button for region_page')

    def dload_data():
        print('download Button for region_page')

    def visualize_button():
        vis_btn = Button(region_page,
                         text='Visualize Data',
                         bg=clr2,
                         height=2,
                         width=15,
                         foreground=clr1,
                         font=(ft, 15),
                         justify='center',
                         command = Visualize_data
                         )
        vis_btn.pack()

    def back_button():
        back_btn = Button(region_page,
                          text='Back',
                          bg=clr2,
                          height=2,
                          width=15,
                          foreground=clr1,
                          font=(ft, 15),
                          justify='center',
                          command=back_function
                          )
        back_btn.pack(pady=25)

    def download_button():
        dl_btn = Button(region_page, text='Download',
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
    region_page.mainloop()


# if __name__ == '__main__':
#     region_data()


