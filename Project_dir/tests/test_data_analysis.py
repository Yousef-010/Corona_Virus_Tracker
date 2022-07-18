import pytest
from Project_dir.api.data_analysis import *
import requests
import json
import jsonpath

URL = 'https://api.covid19api.com/summary'

response = requests.get(URL)

json_response = json.loads(response.text)

Countries=jsonpath.jsonpath(json_response,"Countries")


TotalConfirmed=[]
TotalDeaths=[]
survivors=[]
countries_name=[]
middle_east=[]
western_europe=[]
fatality_ratio=[]

middle_east_regions = ['Algeria', 'United Arab Emirates', 'Amman', 'Egypt', 'Palestine', 'the two seas', 'Diameter',
                       'Kuwait', 'Lebanon', 'Libya', 'Mauritania', 'Morocco', 'Saudi Arab', 'Sudan', 'Tunisia',
                       'Turkey', 'Syria', 'To whom', 'Iraq', 'Iran', 'Israel', 'Jordan', 'Yemen']
western_europe_regions = ['Cyprus', 'Albania', 'Bulgaria', 'Estonia', 'Poland', 'Bosnia and Herzegovina', 'Cech',
                          'Croatia', 'Latvia', 'Lithuania', 'Romania', 'Macedonia', 'Serbia and Montenegro', 'Slovakia',
                          'Slovenia', 'Hungary', 'iranda', 'Andorra', 'Austria', 'Belgium', 'Iceland', 'Denmark',
                          'Germany', 'France', 'Finland', 'Holland', 'Luxembourg', 'Ligtenstein', 'Malta', 'Monaco',
                          'Norway', 'Portugal', 'Sweden', 'Switzerland', 'Spain', 'Greece', 'Italia', 'Britain']

for i in range(195):

    x=Countries[0][i]["TotalConfirmed"]
    y=Countries[0][i]["TotalDeaths"]



    if Countries[0][i]["Country"] in middle_east_regions:
        middle_east+=[x]
    elif Countries[0][i]["Country"] in western_europe_regions:
        western_europe+=[x]


    TotalConfirmed+=[x]
    TotalDeaths+=[y]

    survivors+=[x-y]
    fatality_ratio+=[round(y/x*100,2)]



sum_middle_east_regions=sum(middle_east)

sun_western_europe_regions=sum(western_europe)




max_TotalConfirmed=max(TotalConfirmed)

max_TotalDeaths=max(TotalDeaths)

min_TotalConfirmed=min(TotalConfirmed)

min_TotalDeaths=min(TotalDeaths)

sum_TotalConfirmed=sum(TotalConfirmed)

sum_TotalDeaths=sum(TotalDeaths)

sum_survivors=sum(survivors)

avr_TotalConfirmed=sum_TotalConfirmed/195

avr_TotalDeaths=sum_TotalDeaths/195

avr_survivors=sum_survivors/195

bad_country=[]

god_country=[]

country_can_visit = []

for i in range(195):
    if Countries[0][i]["TotalConfirmed"]-Countries[0][i]["TotalDeaths"]>avr_survivors:
        god_country+=[Countries[0][i]["Country"]]
    elif Countries[0][i]["TotalConfirmed"]-Countries[0][i]["TotalDeaths"]<avr_survivors:
        bad_country+=[Countries[0][i]["Country"]]

for i in range(195):
    if Countries[0][i]['NewConfirmed'] > 0:
        country_can_visit += [  Countries[0][i]["Country"]]





def test_find_max_deaths():
    actual = find_max_deaths()
    expected = max_TotalDeaths
    assert actual == expected


def test_find_min_deaths():
    actual = find_min_deaths()
    expected = min_TotalDeaths
    assert actual == expected


def test_find_max_confirmed():
    actual = find_max_confirmed()
    expected =max_TotalConfirmed
    assert actual == expected


def test_find_min_confirmed():
    actual = find_min_confirmed()
    expected = min_TotalConfirmed
    assert actual == expected


def test_find_global_death():
    actual = find_global_death()
    expected = sum_TotalDeaths
    assert actual == expected


def test_find_global_confirmed():
    actual = find_global_confirmed()
    expected = sum_TotalConfirmed
    assert actual == expected


def test_find_global_avg_death():
    actual = find_global_avg_death()
    expected = avr_TotalDeaths
    assert actual == expected


def test_find_global_avg_confirmed():
    actual = find_global_avg_confirmed()
    expected = avr_TotalConfirmed
    assert actual == expected


def test_total_survival_for_each_country():
    actual = total_survival_for_each_country()
    expected = survivors
    assert actual == expected


# def test_total_infected_middle_east():
#     actual = total_infected_middle_east()
#     expected = sum_middle_east_regions
#     assert actual == expected


# def test_total_infected_western_europe():
#     actual = total_infected_western_europe()
#     expected = sun_western_europe_regions
#     assert actual == expected


def test_fatality_ratio_of_death_for_each_country():
    actual = fatality_ratio_of_death_for_each_country()
    expected=fatality_ratio
    assert actual == expected


def test_get_report_based_on_avg_of_survivors():
    actual = get_report_based_on_avg_of_survivors()[0]
    expected =god_country
    assert actual == expected



def test_get_report_based_on_avg_of_survivors2():
    actual = get_report_based_on_avg_of_survivors()[1]
    expected =bad_country
    assert actual == expected



def test_transportation_to_country():
    actual = transportation_to_country()
    expected=country_can_visit
    assert actual == expected


