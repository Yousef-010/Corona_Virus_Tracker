from tkinter import *
from visualizing_page import display_page5
from region_input import region_input

bkg1 = '#787A91'
clr1 = '#EEEEEE'
clr2 = '#141E61'
ft = 'serif bold'
reg_page = Tk()


def visualize_botton():
    vis_btn = Button(reg_page,
                     text='Next',
                     bg=clr2,
                     height=2,
                     width=15,
                     foreground=clr1,
                     font=(ft, 15),
                     justify='center',
                     command=display_page5()
                     )
    vis_btn.pack(pady=50)


def back_botton():
    back_btn = Button(reg_page,
                      text='Back',
                      bg=clr2,
                      height=2,
                      width=15,
                      foreground=clr1,
                      font=(ft, 15),
                      justify='center',
                      command=region_input()
                      )
    back_btn.pack()


def display_page4():
    reg_page.title('COVID Live Tracker')
    reg_page.minsize(width=900, height=600)
    visualize_botton()
    back_botton()
    reg_page.mainloop()


if __name__ == '__main__':
    display_page4()
