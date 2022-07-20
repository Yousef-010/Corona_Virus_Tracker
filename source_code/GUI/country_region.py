import os
import pyttsx3

from datetime import datetime
from tkinter import *
from tkinter import messagebox, filedialog
from tkinter import ttk

import matplotlib.pyplot as plt
import seaborn as sns

from source_code.api.data_analysis import *
import main

# *************** Global Style Variables ****************
bkg1 = '#1d2b2c'  # Background color
clr1 = '#0b3b40'  # Label Box color
clr2 = '#9fe3de'  # Font color
clr3 = '#74d1b6'
buttons = '#0b3b40'  # Buttons Background color
ft = 'Times'  # Primary Font type
ft2 = 'courier'  # Secondary Font type
ftt = ('Times', 17),
tble_clr = '#041315'  # Table Background color
data_set = pd.read_csv('topics.csv')

# *************** Render ****************
country_region_window = Tk()
country_region_window.title('Country/Region Input')
country_region_window.configure(bg=clr3)
country_region_window.minsize(width=1000, height=600)

if main.user_name.get() == 'Please Enter Your Name':
    region_input_instruction = "Hello Sir/Ma'am\nKindly Choose a Country or a Region \nto View From The " \
                               "Dropdown List, Then Click Next"
else:
    region_input_instruction = 'Hello ' + main.user_name.get().capitalize() + "\nKindly Choose a Country or a " \
                                                                              "Region \nto View From The " \
                                                                              "Dropdown List, Then Click Next"

r_c_instruction_label = Label(country_region_window,
                              text=region_input_instruction,
                              pady=50,
                              padx=25,
                              justify='center',
                              border=10,
                              background=clr3,
                              foreground=clr1,
                              borderwidth=2,
                              font=('andalus', 30))

r_c_instruction_label.pack(pady=25)


# Should return to root (home window)
def country_region_back():
    country_region_window.destroy()
    os.system('python main.py')


countries = data_set['Name'].values

clicked_country = StringVar(country_region_window)
clicked_country.set('Choose a Country')
country_drop_list = OptionMenu(country_region_window, clicked_country, *countries)
country_drop_list.configure(bg=buttons, fg=clr3, font=('Times', 17))
country_drop_list.pack(pady=15, padx=25)

regions = [
    'Middle_East',
    'Western_Europe',
    'Other'
]

clicked_region = StringVar(country_region_window)
reg_drop_list = OptionMenu(country_region_window, clicked_region, *regions)
reg_drop_list.configure(bg=buttons, fg=clr3, font=('Times', 17))
clicked_region.set('Choose a Region')

reg_drop_list.pack(pady=25, padx=25)


def country_region_next():
    # --------------- start country_region_window ---------------
    if clicked_country.get() == 'Israel':
        messagebox.showinfo(title="OOPS!", message="You must mean Palestine")
        country_region_window.destroy()

    if clicked_country.get() != 'Choose a Country':
        country_region_window.destroy()
        # --------------- start country page ---------------

        country_page = Tk()
        country_page.title('Country_page')
        country_page.configure(bg=bkg1)
        country_page.minsize(width=800, height=400)

        # --------------- country Table ---------------

        def dload_data():
            path = filedialog.askdirectory()
            selected_country = data_set[data_set.Name == clicked_country.get()]

            selected_df = pd.DataFrame(selected_country)
            selected_df.to_csv(f'{path}.csv')
            messagebox.showinfo(title=f'{clicked_country.get()} Download',
                                message='Your Data Has been downloaded successfully')

        def back_to_country_region_from_country_function():
            country_page.destroy()
            os.system('python country_region.py')

        def visualize_data():
            TC = data_set[data_set.Name == clicked_country.get()].iloc[0]['TotalDeaths']
            TD = data_set[data_set.Name == clicked_country.get()].iloc[0]['survivors']

            labels = 'TotalDeaths', 'survivors'
            sizes = [TC, TD]
            explode = (0, 0)
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.0f%%',
                    shadow=True, startangle=90)
            ax1.axis('equal')
            plt.show()

        def display_data():
            data_set = pd.read_csv('topics.csv')
            data_set = data_set[data_set.Name == clicked_country.get()]

            # ************** Start Styling Table **************
            style = ttk.Style()
            style.theme_use('clam')
            style.configure("Treeview",
                            background=buttons,
                            foreground=clr2,
                            rowheight=30,
                            fieldbackground=buttons)
            # ************** End Styling Table **************
            tree = ttk.Treeview(country_page, padding=5, height=3, selectmode='browse')
            scrollbar = Scrollbar(country_page, orient="horizontal", width=20)
            tree.config(xscrollcommand=scrollbar.set)
            scrollbar.config(command=tree.xview)

            tree["column"] = list(data_set.columns)
            tree["show"] = "headings"
            for col in tree["column"]:
                tree.heading(col, text=col)

            df_rows = data_set.to_numpy().tolist()
            for row in df_rows:
                tree.insert("", "end", values=row)

            tree.pack()
            scrollbar.pack(fill='both')

        display_data()

        def display_report():
            selected_country = data_set[data_set.Name == clicked_country.get()]
            name = selected_country['Name'].values[0]
            total_cases = selected_country['TotalConfirmed'].values[0]
            total_deaths = selected_country['TotalDeaths'].values[0]
            new_confirmed = selected_country['NewConfirmed'].values[0]
            new_deaths = selected_country['NewDeaths'].values[0]

            if selected_country['NewConfirmed'].values[0] > 0:
                bad_country_msg = f"Today is {datetime.now().strftime('%A, ' + '%Y-%m-%d')}. As of" \
                                  f" {datetime.now().strftime('%H:%M%p')}:\nFor your own safety, try to " \
                                  f"avoid visiting {name} as {new_confirmed} new cases of COVID 19 infections" \
                                  f" have been confirmed with {new_deaths} new deaths, raising the total " \
                                  f"number of infections to {total_cases} cases, and total death toll " \
                                  f"to {total_deaths} since the pandemic broke out"

                def read_bad_country_report():
                    box = messagebox.askquestion(title=f'{clicked_country.get()}  Report',
                                                 message=bad_country_msg + '\n\nRead Report?')
                    if box == 'yes':
                        txt_to_speech = pyttsx3.init()
                        txt_to_speech.setProperty("rate", 135)

                        txt_to_speech.say(bad_country_msg)
                        txt_to_speech.runAndWait()

                read_bad_country_report()

            else:
                good_country_message = f'Today is  {datetime.now().strftime("%A, " + "%Y-%m-%d")}. As ' \
                                       f'of {datetime.now().strftime("%H:%M%p")}: \nThere' \
                                       f' are no new confirmed cases of COVID infection' \
                                       f' in {name} \nEnjoy your time there'

                def read_good_country_report():
                    box = messagebox.askquestion(title=f'{clicked_country.get()}  Report',
                                                 message=good_country_message + " ^^" + '\n\nRead Report?')

                    if box == 'yes':
                        txt_to_speech = pyttsx3.init()
                        txt_to_speech.setProperty("rate", 135)

                        txt_to_speech.say(good_country_message)
                        txt_to_speech.runAndWait()

                read_good_country_report()

        rep_btn = Button(country_page,
                         text='Show Report',
                         bg=buttons,
                         height=2,
                         width=15,
                         foreground=clr2,
                         font=(ft, 15),
                         justify='center',
                         command=display_report
                         )
        rep_btn.pack(side='right', padx=50)

        vis_btn = Button(country_page,
                         text='Visualize Data',
                         bg=buttons,
                         height=2,
                         width=15,
                         foreground=clr2,
                         font=(ft, 15),
                         justify='center',
                         command=visualize_data
                         )
        vis_btn.pack(side='right', pady=50)

        back_country_button = Button(country_page,
                                     text='Back',
                                     bg=buttons,
                                     height=2,
                                     width=15,
                                     foreground=clr2,
                                     font=(ft, 15),
                                     justify='center',
                                     command=back_to_country_region_from_country_function
                                     )
        back_country_button.pack(side='left')

        dl_btn = Button(country_page, text='Download',
                        bg=buttons,
                        height=2,
                        width=15,
                        foreground=clr2,
                        font=(ft, 15),
                        justify='center',
                        command=dload_data
                        )
        dl_btn.pack(padx=50, side='right')
        country_page.mainloop()

        # --------------- end country page ---------------

    elif clicked_region.get() != 'Choose a Region':
        country_region_window.destroy()
        # --------------- start region page ---------------

        region_page = Tk()
        region_page.title('Region_page')
        region_page.configure(bg=bkg1)
        region_page.minsize(width=900, height=600)

        def display_region_data():
            data_set = pd.read_csv('topics.csv')
            selected_region = clicked_region.get()
            data_set = data_set[data_set.Region == selected_region]

            # ************** Start Styling Table **************
            style = ttk.Style()
            style.theme_use('clam')
            style.configure("Treeview",
                            background=buttons,
                            foreground=clr2,
                            rowheight=30,
                            fieldbackground=buttons)

            # ************** End Styling Table **************
            tree = ttk.Treeview(region_page, padding=5, height=14, selectmode='browse')
            scrollbar = Scrollbar(region_page, orient="horizontal", width=20)
            tree.config(xscrollcommand=scrollbar.set)
            scrollbar.config(command=tree.xview)

            tree["column"] = list(data_set.columns)
            tree["show"] = "headings"
            for col in tree["column"]:
                tree.heading(col, text=col)

            df_rows = data_set.to_numpy().tolist()
            for row in df_rows:
                tree.insert("", "end", values=row)

            tree.pack()
            scrollbar.pack(fill='both')

        display_region_data()

        def back_to_country_region_from_region_function():
            region_page.destroy()
            os.system('python country_region.py')

        def visualize_region_data():
            data_set = pd.read_csv('topics.csv')
            selected_region = clicked_region.get()
            data_set = data_set[data_set.Region == selected_region].head(19).sort_values('Fatality_ratio',
                                                                                         ascending=False)

            sns.barplot(data=data_set, x='Fatality_ratio', y='Name', ci=None)
            plt.xticks(rotation=90)
            plt.show()

        def dload_region_data():
            data_set = pd.read_csv('topics.csv')
            selected_region = clicked_region.get()
            data_set = data_set[data_set.Region == selected_region]
            path = filedialog.askdirectory()

            selected_r_df = pd.DataFrame(data_set)
            selected_r_df.to_csv(f'{path}.csv')
            messagebox.showinfo(title=f'{selected_region} Download',
                                message='Your Data Has been downloaded successfully')

        def display_region_report():
            data_set = pd.read_csv('topics.csv')
            selected_region = clicked_region.get()
            data_set = data_set[data_set.Region == selected_region]
            minimum = data_set['Fatality_ratio'].min()
            maximum = data_set['Fatality_ratio'].max()
            avg = round((data_set['TotalDeaths'].mean()), 2)
            survivors = round(((data_set['survivors'] / data_set['TotalConfirmed'] * 100).mean()), 2)
            n_min = data_set[(data_set['Fatality_ratio'] == minimum)]['Name'].values[0]
            n_max = data_set[(data_set['Fatality_ratio'] == maximum)]['Name'].values[0]
            region = selected_region
            region_msg = f"Today is {datetime.now().strftime('%A, ' + '%Y-%m-%d')}. As" \
                         f" of {datetime.now().strftime('%H:%M%p')}: \nWith a fatality rate of {minimum}% ," \
                         f" {n_min} is the {region.replace('_', ' ')}'s safest travel destination.\nOn the " \
                         f"other hand, avoid traveling to {n_max} for your own safety, as the fatality " \
                         f"rate stands at {maximum}% right now. \nThe average of death cases in " \
                         f"{region.replace('_', ' ')} region is {avg}\n with a survival rate of {survivors}% "


            def read_good_country_report():
                box = messagebox.askquestion(title=f'{selected_region.replace("_", " ")} Report',
                                             message=region_msg + '\n\nRead Report?')

                if box == 'yes':
                    txt_to_speech = pyttsx3.init()
                    txt_to_speech.setProperty("rate", 135)

                    txt_to_speech.say(region_msg)
                    txt_to_speech.runAndWait()

            read_good_country_report()

        rep_btn = Button(region_page,
                         text='Show Report',
                         bg=buttons,
                         height=2,
                         width=15,
                         foreground=clr2,
                         font=(ft, 15),
                         justify='center',
                         command=display_region_report
                         )
        rep_btn.pack(side='right', padx=50)

        vis_btn = Button(region_page,
                         text='Visualize Data',
                         bg=buttons,
                         height=2,
                         width=15,
                         foreground=clr2,
                         font=(ft, 15),
                         justify='center',
                         command=visualize_region_data
                         )
        vis_btn.pack(side='right')

        back_region_button = Button(region_page,
                                    text='Back',
                                    bg=buttons,
                                    height=2,
                                    width=15,
                                    foreground=clr2,
                                    font=(ft, 15),
                                    justify='center',
                                    command=back_to_country_region_from_region_function
                                    )
        back_region_button.pack(side='left')

        dl_btn = Button(region_page, text='Download',
                        bg=buttons,
                        height=2,
                        width=15,
                        foreground=clr2,
                        font=(ft, 15),
                        justify='center',
                        command=dload_region_data
                        )
        dl_btn.pack(padx=50, side='right')

        region_page.mainloop()

        # --------------- end region page ---------------

    else:
        messagebox.showinfo(title='ERROR', message='Please Select a Country or a Region! ')


next_country_region_window_button = Button(country_region_window,
                                           text='Next',
                                           command=country_region_next,
                                           bg=buttons,
                                           height=2,
                                           width=15,
                                           foreground=clr2,
                                           font=ftt,
                                           justify='center')

next_country_region_window_button.pack(side='right', pady=50, padx=75)

back_country_region_window_button = Button(country_region_window,
                                           text='Back',
                                           command=country_region_back,
                                           bg=buttons,
                                           height=2,
                                           width=15,
                                           foreground=clr2,
                                           font=ftt,
                                           justify='center')

back_country_region_window_button.pack(side='left', pady=50, padx=75)

main.root.destroy()

country_region_window.mainloop()
