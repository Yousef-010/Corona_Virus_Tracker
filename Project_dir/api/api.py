import requests
import json
import pandas as pd

URL = 'https://api.covid19api.com/summary'


def get_data_from_api(URL):
    response = requests.get(URL)
    data = response.text
    return data


def convert_data_to_json():
    data = get_data_from_api(URL)
    data_json = json.loads(data)
    data_arr = data_json['Countries']
    return data_arr


def fill_data_into_arrays():
    data_arr = convert_data_to_json()
    country_names = []
    country_total_confirmed = []
    country_total_deaths = []
    country_date = []
    middle_east_regions = ['Algeria', 'United Arab Emirates', 'Amman', 'Egypt', 'Palestine', 'the two seas', 'Diameter', 'Kuwait', 'Lebanon', 'Libya', 'Mauritania', 'Morocco', 'Saudi Arab', 'Sudan', 'Tunisia', 'Turkey', 'Syria', 'To whom', 'Iraq', 'Iran', 'Israel', 'Jordan', 'Yemen']
    western_europe_regions = ['Cyprus', 'Albania', 'Bulgaria', 'Estonia', 'Poland', 'Bosnia and Herzegovina', 'Cech', 'Croatia', 'Latvia', 'Lithuania', 'Romania', 'Macedonia', 'Serbia and Montenegro', 'Slovakia', 'Slovenia', 'Hungary', 'iranda', 'Andorra', 'Austria', 'Belgium', 'Iceland', 'Denmark', 'Germany', 'France', 'Finland', 'Holland', 'Luxembourg', 'Ligtenstein', 'Malta', 'Monaco', 'Norway', 'Portugal', 'Sweden', 'Switzerland', 'Spain', 'Greece', 'Italia', 'Britain']
    region = []
    total_survival = []
    fatality_ratio = []
    new_confirmed_arr = []
    new_deaths_arr = []

    for cases in data_arr:
        name = cases['Country']
        total_confirmed = cases['TotalConfirmed']
        total_deaths = cases['TotalDeaths']
        date = cases['Date']
        new_confirmed = cases['NewConfirmed']
        new_deaths = cases['NewDeaths']

        if name in middle_east_regions:
            region.append('Middle_East')
        elif name in western_europe_regions:
            region.append('Western_Europe')
        else:
            region.append('Other')

        country_names.append(name)
        country_total_confirmed.append(total_confirmed)
        country_total_deaths.append(total_deaths)
        country_date.append(date)
        total_survival.append(cases['TotalConfirmed'] - cases['TotalDeaths'])
        fatality_ratio.append(round((cases['TotalDeaths'] / cases["TotalConfirmed"] * 100), 2))
        new_confirmed_arr.append(new_confirmed)
        new_deaths_arr.append(new_deaths)
    return country_names, country_total_confirmed, country_total_deaths, new_confirmed_arr, new_deaths_arr, total_survival, fatality_ratio, region, country_date


def fill_data_into_object():
    topics_dict = {
        'Name': fill_data_into_arrays()[0],
        'TotalConfirmed': fill_data_into_arrays()[1],
        'TotalDeaths': fill_data_into_arrays()[2],
        'NewConfirmed': fill_data_into_arrays()[3],
        'NewDeaths': fill_data_into_arrays()[4],
        'survivors': fill_data_into_arrays()[5],
        'Fatality_ratio': fill_data_into_arrays()[6],
        'Region': fill_data_into_arrays()[7],
        'Date': fill_data_into_arrays()[8]

    }

    text_str = json.dumps(topics_dict, sort_keys=False, indent=4)
    return topics_dict, text_str

