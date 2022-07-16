from tkinter import *
from tkinter import ttk
# from pandastable import Table, TableModel
# from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox, filedialog
from datetime import datetime
# import pandas as pd
from Project_dir.api.data_analysis import *
from PIL import Image, ImageTk

# *************** Global Style Variables ****************
bkg1 = '#1d2b2c'  # Background color
clr1 = '#0b3b40'  # Label Box color
clr2 = '#9fe3de'  # Font color
buttons = '#0b3b40'  # Buttons Background color
ft = 'Times'  # Font type
tc = '#041315'  # Table Background color

root = Tk()
root.title('COVID Live Tracker')
root.configure(bg=bkg1)
root.minsize(width=900, height=700)

bg_img = ImageTk.PhotoImage(file="CV_4.jpg")
# can = Canvas(root)
# can.place(relx=0, rely=0, relwidth=1, relheight=1)
# # add image
# can.create_image(0, 0, image=bg_img, anchor="nw")
# can.create_text(450,
#                 200,
#                 text="Welcome To COVID Live Tracker\nYour COVID Related Stats Viewer, Analyzer and Downloader \nTo "
#                      "Proceed, Please Click 'Next'",
#                 font=(ft, 20),
#                 fill=clr2,
#                 justify='center')


# ************** Add image BackGround **************
img_label = Label(root, image=bg_img)
img_label.place(relx=0, rely=0, relwidth=1, relheight=1)

welcome = Label(img_label, text="Welcome To COVID Live Tracker \nYour COVID Related Stats Viewer, Analyzer and "
                                "Downloader\nTo Proceed, Please Click Next",
                pady=25,
                padx=0,
                border=10,
                background=clr1,
                foreground=clr2,
                borderwidth=2,
                font=(ft, 25))

welcome.pack(pady=50)


def home_next():
    country_region_window = Tk()
    country_region_window.title('Country/Region Input')
    country_region_window.configure(bg=bkg1)
    country_region_window.minsize(width=500, height=300)

    region_input_instruction = 'Hi ' + user_name.get() + "\nKindly choose a country or a region \nto view from the " \
                                                         "dropdown list,then click Next "
    r_c_instruction_label = Label(country_region_window,
                                  text=region_input_instruction,
                                  pady=25,
                                  padx=25,
                                  justify='center',
                                  border=10,
                                  background=clr1,
                                  foreground=clr2,
                                  borderwidth=2,
                                  font=(ft, 25))

    r_c_instruction_label.pack(pady=25)

    def country_region_back():
        country_region_window.destroy()

    countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antarctica', 'Antigua and Barbuda',
                 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh',
                 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina',
                 'Botswana', 'Brazil', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia',
                 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia',
                 'Comoros', 'Congo (Brazzaville)', 'Congo (Kinshasa)', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus',
                 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador',
                 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland',
                 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea',
                 'Guinea-Bissau', 'Guyana', 'Haiti', 'Holy See (Vatican City State)', 'Honduras', 'Hungary', 'Iceland',
                 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Palestinian', 'Italy',
                 'Jamaica',
                 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea (North)', 'Korea (South)', 'Kuwait',
                 'Kyrgyzstan', 'Lao PDR', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein',
                 'Lithuania', 'Luxembourg', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives',
                 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico',
                 'Micronesia, Federated States of', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco',
                 'Mozambique', 'Myanmar', 'Namibia', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger',
                 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palestinian Territory', 'Panama',
                 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar',
                 'Republic of Kosovo', 'Romania', 'Russian Federation', 'Rwanda',
                 'Saint Lucia', 'Saint Vincent and Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe',
                 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia',
                 'Solomon Islands', 'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname',
                 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic (Syria)', 'Taiwan, Republic of China',
                 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga',
                 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Uganda', 'Ukraine', 'United Arab Emirates',
                 'United Kingdom', 'United States of America', 'Uruguay', 'Uzbekistan', 'Vanuatu',
                 'Viet Nam', 'Yemen', 'Zambia', 'Zimbabwe']

    clicked_country = StringVar(country_region_window)
    clicked_country.set('Choose a Country')
    country_drop_list = OptionMenu(country_region_window, clicked_country, *countries)
    country_drop_list.pack(pady=25, padx=25)
    # country_choice = clicked_country.get()

    regions = [
        'Middle_East',
        'Western_Europe',
        'Other'
    ]

    clicked_region = StringVar(country_region_window)
    reg_drop_list = OptionMenu(country_region_window, clicked_region, *regions)
    clicked_region.set('Choose a Region')
    # region_choice = clicked_region.get()
    reg_drop_list.pack(pady=25, padx=25)

    def country_region_next():

        # ############### start country_region_window  #################

        if clicked_country.get() != 'Choose a Country':
            country_region_window.destroy()
            # ##############  start country page ###############

            country_page = Tk()
            country_page.title('Country_page')
            country_page.configure(bg=bkg1)
            country_page.minsize(width=800, height=400)

            # ##### country Table

            def dload_data():
                data_set = pd.read_csv('topics.csv')
                path = filedialog.askdirectory()
                selected_country = data_set[data_set.Name == clicked_country.get()]
                # selected_df = {'Name': selected_country['Name'],
                #                'TotalConfirmed': selected_country['TotalConfirmed'],
                #                'TotalDeaths': selected_country['TotalDeaths'],
                #                'NewConfirmed': selected_country['NewConfirmed'],
                #                'NewDeaths': selected_country['NewDeaths'],
                #                'survivors': selected_country['survivors'],
                #                'Fatality_ratio': selected_country['Fatality_ratio'],
                #                'Region': selected_country['Region'],
                #                'Date': selected_country['Date'],
                #                }
                # selected_df = pd.DataFrame(selected_df)
                selected_df = pd.DataFrame(selected_country)
                selected_df.to_csv(f'{path}.csv')
                messagebox.showinfo(title=f'{clicked_country.get()} Download',
                                    message='Your Data Has been downloaded successfully')

            def back_function():
                country_page.destroy()

            def visualize_data():
                import matplotlib.pyplot as plt
                import seaborn as sns

                sns.set(style='white', color_codes=True)
                data_set = pd.read_csv('topics.csv')
                TC = data_set[data_set.Name == clicked_country.get()].iloc[0]['TotalDeaths']
                TD = data_set[data_set.Name == clicked_country.get()].iloc[0]['survivors']
                # TS = data_set[data_set.Name == clicked_country.get()].iloc[0]['Fatality_ratio']

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
                # selected_country = data_set[data_set.Name == clicked_country.get()]
                data_set = data_set[data_set.Name == clicked_country.get()]

                # selected_df = {'Name': selected_country['Name'],
                #                'TotalConfirmed': selected_country['TotalConfirmed'],
                #                'TotalDeaths': selected_country['TotalDeaths'],
                #                'NewConfirmed': selected_country['NewConfirmed'],
                #                'NewDeaths': selected_country['NewDeaths'],
                #                'survivors': selected_country['survivors'],
                #                'Fatality_ratio': selected_country['Fatality_ratio'],
                #                'Region': selected_country['Region'],
                #                'Date': datetime.now().strftime("%Y-%m-%d %H:%M")
                #                }
                # selected_df = pd.DataFrame(selected_df)

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

                # tree["column"] = list(selected_df.columns)
                tree["column"] = list(data_set.columns)
                tree["show"] = "headings"
                tree.column("# 0.5", anchor=CENTER, stretch=NO, width=50)
                tree.column("# 0.5", anchor=CENTER, stretch=NO)
                for col in tree["column"]:
                    tree.heading(col, text=col)

                # df_rows = selected_df.to_numpy().tolist()
                df_rows = data_set.to_numpy().tolist()
                for row in df_rows:
                    tree.insert("", "end", values=row)

                tree.pack()
                scrollbar.pack(fill='both')

            display_data()

            def display_report():
                data_set = pd.read_csv('topics.csv')
                selected_country = data_set[data_set.Name == clicked_country.get()]
                name = selected_country['Name'].values[0]
                F_R_today = round(
                    ((selected_country['NewDeaths'].values[0] / selected_country['NewConfirmed'].values[0]) * 100), 2)
                surviving_ratio = round((((selected_country['NewConfirmed'].values[0] - selected_country['NewDeaths'].values[0]) / (selected_country['NewConfirmed'].values[0])) * 100), 2)
                if selected_country['NewConfirmed'].values[0] > 0:

                    messagebox.showinfo(title=f'{clicked_country.get()}  report',
                                        message=f'Today is {datetime.now().strftime("%Y-%m-%d %H:%M")} \nWe dont recommend to visit {clicked_country.get()} now \nThe possibility of surviving from the virus for today is  {surviving_ratio} % \nThe possibility of your death is {F_R_today} % \nThe health system in {name} not good ')
                else:
                    messagebox.showinfo(title=f'{clicked_country.get()}  report',
                                        message=f'Today is  {datetime.now().strftime("%Y-%m-%d %H:%M")} \nThere is no new cases for today in {name} \nEnjoy spending time there :) ')

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

            back_btn = Button(country_page,
                              text='Back',
                              bg=buttons,
                              height=2,
                              width=15,
                              foreground=clr2,
                              font=(ft, 15),
                              justify='center',
                              command=back_function
                              )
            back_btn.pack(side='left')

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

            # ############### end country page #################

        elif clicked_region.get() != 'Choose a Region':
            country_region_window.destroy()
            # ############### start region page #################

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
                tree.column("# 0.5", anchor=CENTER, stretch=NO, width=50)
                tree.column("# 0.5", anchor=CENTER, stretch=NO)
                for col in tree["column"]:
                    tree.heading(col, text=col)

                df_rows = data_set.to_numpy().tolist()
                for row in df_rows:
                    tree.insert("", "end", values=row)

                tree.pack()
                scrollbar.pack(fill='both')

            display_region_data()

            def back_function():
                region_page.destroy()

            def Visualize_region_data():
                import matplotlib.pyplot as plt
                import seaborn as sns

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

                messagebox.showinfo(title=f'{region}',
                                    message=f"Today date is, {datetime.now().strftime('%Y-%m-%d %H:%M')} \n{n_min} is the safest country to visit in {region} \nwith Fatality_ratio = {minimum}% \nFor your safety avoid visiting {n_max} \nwith Fatality_ratio =  {maximum}%  \nThe average of death cases in {region} = {avg}  \nwith survival rate = {survivors}% "
                                    )

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
                             command=Visualize_region_data
                             )
            vis_btn.pack(side='right')

            back_btn = Button(region_page,
                              text='Back',
                              bg=buttons,
                              height=2,
                              width=15,
                              foreground=clr2,
                              font=(ft, 15),
                              justify='center',
                              command=back_function
                              )
            back_btn.pack(side='left')

            dl_btn = Button(region_page, text='Download',
                            bg=buttons,
                            height=2,
                            width=15,
                            foreground=clr2,
                            font=(ft, 15),
                            justify='center',
                            command=dload_region_data
                            )
            dl_btn.pack(side='left', padx=200)

            region_page.mainloop()

            # ############### end region page #################

        else:
            messagebox.showinfo(title='ERROR', message='Please Select country or region ! ')

    next_btn = Button(country_region_window,
                      text='Next',
                      command=country_region_next,
                      bg=buttons,
                      height=2,
                      width=15,
                      foreground=clr2,
                      font=(ft, 15),
                      justify='center')

    next_btn.pack(side='right', pady=50)

    back_btn = Button(country_region_window,
                      text='Back',
                      command=country_region_back,
                      bg=buttons,
                      height=2,
                      width=15,
                      foreground=clr2,
                      font=(ft, 15),
                      justify='center')

    back_btn.pack(side='left', pady=50)

    root.destroy()

    country_region_window.mainloop()
    # ############### end country_region_window  #################


user_name = Entry(img_label, width=25,
                  font=(ft, 20),
                  bg=clr1,
                  bd=2.5,
                  foreground=clr2,
                  justify='center',
                  borderwidth=5
                  )

user_name.place(x=250, y=450)
user_name.insert(0, 'Please Enter Your Name')

next_btn = Button(img_label,
                  text='Next',
                  command=home_next,
                  bg=buttons,
                  height=2,
                  width=15,
                  foreground=clr2,
                  font=(ft, 15),
                  justify='center'
                  )

next_btn.place(x=350, y=550)
#
# def resizer(e):
#     global bg, re_bg, new_bg
#     bg = Image.open('CV_4.jpg')
#     re_bg = bg.resize((e.width, e.height), Image.ANTIALIAS)
#     new_bg = ImageTk.PhotoImage(re_bg)
#     can.create_image(0, 0, image=new_bg, anchor="nw")
#     can.create_text(450,
#                     200,
#                     text="Welcome To COVID Live Tracker\nYour COVID Related Stats Viewer, \nAnalyzer and Downloader \nTo "
#                          "Proceed, Please Click 'Next'",
#                     font=(ft, 25),
#                     fill=clr2,
#                     justify='center')


if __name__ == '__main__':
    # root.bind('<Configure>', resizer)
    root.mainloop()
