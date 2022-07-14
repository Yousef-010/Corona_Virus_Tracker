from tkinter import *
from tkinter import ttk
from pandastable import Table, TableModel
# from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox,filedialog


import pandas as pd
from Project_dir.api.data_analysis import *

bkg1 = '#787A91'
clr1 = '#EEEEEE'
clr2 = '#141E61'

root = Tk()
root.title('COVID Live Tracker')
root.configure(bg=bkg1)
root.minsize(width=900, height=600)

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


def home_next():
    country_region_window = Tk()
    country_region_window.title('Country/Region Input')
    country_region_window.configure(bg=bkg1)
    country_region_window.minsize(width=900, height=600)

    region_input_instruction = 'HI ' + user_name.get() + """
    Kindly choose a country or a region 
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
                 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica',
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
        'Middle East',
        'Europe'
    ]

    clicked_region = StringVar(country_region_window)
    reg_drop_list = OptionMenu(country_region_window, clicked_region, *regions)
    clicked_region.set('Choose a Region')
    # region_choice = clicked_region.get()
    reg_drop_list.pack(pady=25, padx=25)

    def country_region_next():
        ################ start country_region_window  #################

        if clicked_country.get() != 'Choose a Country':
            country_region_window.destroy()
            ###############  start country page ###############
            bkg1 = '#787A91'
            clr1 = '#EEEEEE'
            clr2 = '#141E61'
            ft = 'serif bold'
            country_page = Tk()
            country_page.title('Country_page')
            country_page.minsize(width=900, height=600)

            ###### country Table

            def dload_data():
                data_set = pd.read_csv('topics.csv')
                path = filedialog.askdirectory()
                selected_country = data_set[data_set.Name == clicked_country.get()]
                selected_df = {'Name': selected_country['Name'],
                               'TotalConfirmed': selected_country['TotalConfirmed'],
                               'TotalDeaths': selected_country['TotalDeaths'],
                               'NewConfirmed': selected_country['NewConfirmed'],
                               'NewDeaths': selected_country['NewDeaths'],
                               'survivors': selected_country['survivors'],
                               'Fatality_ratio': selected_country['Fatality_ratio'],
                               'Region': selected_country['Region'],
                               'Date': selected_country['Date'],
                }
                selected_df = pd.DataFrame(selected_df)
                selected_df.to_csv(f'{path}.csv')
                messagebox.showinfo(f'{clicked_country.get()} data downloaded _______')

            def back_function():
                country_page.destroy()

            def visualize_data():
                import matplotlib.pyplot as plt
                import seaborn as sns

                sns.set(style='white', color_codes=True)
                data_set = pd.read_csv('topics.csv')
                TC = data_set[data_set.Name == clicked_country.get()].iloc[0]['TotalConfirmed']
                TD = data_set[data_set.Name == clicked_country.get()].iloc[0]['survivors']
                TS = data_set[data_set.Name == clicked_country.get()].iloc[0]['Fatality_ratio']

                labels = 'TotalConfirmed', 'survivors', 'Fatality_ratio'
                sizes = [TC, TD, TS*10000]
                explode = (0, 0, 0)
                fig1, ax1 = plt.subplots()
                ax1.pie(sizes, explode=explode, labels=labels,autopct='%1.0f%%',
                        shadow=True, startangle=90)
                ax1.axis('equal')
                plt.show()

            vis_btn = Button(country_page,
                             text='Visualize Data',
                             bg=clr2,
                             height=2,
                             width=15,
                             foreground=clr1,
                             font=(ft, 15),
                             justify='center',
                             command=visualize_data
                             )
            vis_btn.pack(side='right', pady=50)

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
            back_btn.pack(side='left')

            dl_btn = Button(country_page, text='Download',
                            bg=clr2,
                            height=2,
                            width=15,
                            foreground=clr1,
                            font=(ft, 15),
                            justify='center',
                            command=dload_data
                            )
            dl_btn.pack(padx=200 ,side='left')

            country_page.mainloop()
            ################ end country page #################

        elif clicked_region.get() != 'Choose a Region':
            country_region_window.destroy()
            ################ start region page #################

            bkg1 = '#787A91'
            clr1 = '#EEEEEE'
            clr2 = '#141E61'
            ft = 'serif bold'

            region_page = Tk()
            region_page.title('Region_page')
            region_page.minsize(width=900, height=600)

            def display():
                pass

            def back_function():
                region_page.destroy()

            def Visualize_data():
                pass

            def dload_data():
                pass

            vis_btn = Button(region_page,
                             text='Visualize Data',
                             bg=clr2,
                             height=2,
                             width=15,
                             foreground=clr1,
                             font=(ft, 15),
                             justify='center',
                             command=Visualize_data
                             )
            vis_btn.pack(side='right')

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
            back_btn.pack(side='left')

            dl_btn = Button(region_page, text='Download',
                            bg=clr2,
                            height=2,
                            width=15,
                            foreground=clr1,
                            font=(ft, 15),
                            justify='center',
                            command=dload_data
                            )
            dl_btn.pack(side='left', padx=200)

            region_page.mainloop()

            ################ end region page #################

        else:
            messagebox.showinfo('ERROR MSG')

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

    root.destroy()

    country_region_window.mainloop()
    ################ end country_region_window  #################


user_name = Entry(root, width=25,
                  font=('Andalus', 20),
                  bg=clr2,
                  bd=2.5,
                  foreground=clr1,
                  justify='center',
                  borderwidth=5
                  )

user_name.pack(pady=25)
user_name.insert(0, 'Please Enter Your Name')

next_btn = Button(root,
                  text='Next',
                  command=home_next,
                  bg=clr2,
                  height=2,
                  width=15,
                  foreground=clr1,
                  font=('serif bold', 15),
                  justify='center'
                  )

next_btn.pack(pady=50)

if __name__ == '__main__':
    root.mainloop()
