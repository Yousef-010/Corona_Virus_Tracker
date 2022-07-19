from source_code.api.api import *


def convert_data_to_data_frame():
    topics_dict = fill_data_into_object()[0]
    topics_df = pd.DataFrame(topics_dict)
    return topics_df


def fill_data_into_csv_file():
    topics_df = convert_data_to_data_frame()
    topics_df.to_csv('topics.csv', index=None)
    return topics_df


def read_csv_data():
    fill_data_into_csv_file()
    data_set = pd.read_csv('topics.csv')
    return data_set


def find_max_deaths():
    data_set = read_csv_data()
    maximum_total_deaths = data_set['TotalDeaths'].max()
    return maximum_total_deaths


def find_min_deaths():
    data_set = read_csv_data()
    minimum_total_deaths = data_set['TotalDeaths'].min()
    return minimum_total_deaths


def find_max_confirmed():
    data_set = read_csv_data()
    maximum_total_confirmed_deaths = data_set['TotalConfirmed'].max()
    return maximum_total_confirmed_deaths


def find_min_confirmed():
    data_set = read_csv_data()
    minimum_total_confirmed_deaths = data_set['TotalConfirmed'].min()
    return minimum_total_confirmed_deaths


def find_global_death():
    data_set = read_csv_data()
    global_deaths = data_set['TotalDeaths'].sum()
    return global_deaths


def find_global_confirmed():
    data_set = read_csv_data()
    global_confirmed = data_set['TotalConfirmed'].sum()
    return global_confirmed


def find_global_avg_death():
    data_set = read_csv_data()
    average_global_deaths = data_set['TotalDeaths'].mean()
    return average_global_deaths


def find_global_avg_confirmed():
    data_set = read_csv_data()
    average_global_confirmed = data_set['TotalConfirmed'].mean()
    return average_global_confirmed


def get_max_deaths_report():
    data_set = read_csv_data()
    country_details = data_set.query('TotalDeaths == 1021306 ')
    return country_details


def get_max_confirmed_report():
    data_set = read_csv_data()
    country_details = data_set.query('TotalConfirmed == 88754821 ')
    return country_details


def total_survival_for_each_country():
    data_set = read_csv_data()
    total_survival = data_set['TotalConfirmed'] - data_set['TotalDeaths']
    return list(total_survival)


def total_infected_middle_east():
    data_set = read_csv_data()
    middle_east_infected = 0
    middle_east_view = data_set.loc[data_set['Region'] == 'Middle_East']
    for i in middle_east_view['TotalConfirmed']:
        middle_east_infected += i
    return middle_east_infected


def total_infected_western_europe():
    data_set = read_csv_data()
    western_europe_infected = 0
    western_europe_view = data_set.loc[data_set['Region'] == 'Western_Europe']
    for i in western_europe_view['TotalConfirmed']:
        western_europe_infected += i
    return western_europe_infected


def fatality_ratio_of_death_for_each_country():
    data_set = read_csv_data()
    fatality_ratio = round((data_set['TotalDeaths'] / data_set["TotalConfirmed"]*100), 2)
    return list(fatality_ratio)


def get_report_based_on_avg_of_survivors():
    data_set = read_csv_data()
    average_survivors = int(data_set['survivors'].mean())
    report = ''
    good_countries = []
    bad_countries = []
    for i in data_set[data_set['survivors'] > average_survivors].Name:
        good_countries.append(i)
    for i in data_set[data_set['survivors'] < average_survivors].Name:
        bad_countries.append(i)
    return good_countries, bad_countries


def transportation_to_country():
    data_set = read_csv_data()
    country_can_visit = []
    for i in data_set[data_set['NewConfirmed'] > 0].Name:
        country_can_visit.append(i)
    return country_can_visit



