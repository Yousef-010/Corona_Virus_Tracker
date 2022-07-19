import pytest
import pandas as pd
data_set = pd.read_csv('topics.csv')


def test_total_count_of_country_names():
    number_of_country_names = data_set['Name'].values
    actual = len(number_of_country_names)
    expected = 195
    assert actual == expected


def test_find_max_deaths():
    actual = data_set['TotalDeaths'].max()
    expected = 1023736
    assert actual == expected


def test_find_min_deaths():
    actual = data_set['TotalDeaths'].min()
    expected = 0
    assert actual == expected


def test_find_max_confirmed():
    actual = data_set['TotalConfirmed'].max()
    expected = 89453076
    assert actual == expected


def test_find_min_confirmed():
    actual = data_set['TotalConfirmed'].min()
    expected = 1
    assert actual == expected


def test_find_global_death():
    actual = data_set['TotalDeaths'].sum()
    expected = 6363126
    assert actual == expected


def test_find_global_confirmed():
    actual = data_set['TotalConfirmed'].sum()
    expected = 560298445
    assert actual == expected


def test_find_global_avg_death():
    actual = data_set['TotalDeaths'].mean()
    expected = 32631.415384615386
    assert actual == expected


def test_find_global_avg_confirmed():
    actual = data_set['TotalConfirmed'].mean()
    expected = 2873325.358974359
    assert actual == expected


def test_total_infected_middle_east():
    middle_east_infected = 0
    middle_east_view = data_set.loc[data_set['Region'] == 'Middle_East']
    for i in middle_east_view['TotalConfirmed']:
        middle_east_infected += i
    actual = middle_east_infected
    expected = 30435539
    assert actual == expected


def test_total_infected_western_europe():
    western_europe_infected = 0
    western_europe_view = data_set.loc[data_set['Region'] == 'Western_Europe']
    for i in western_europe_view['TotalConfirmed']:
        western_europe_infected += i
    actual = western_europe_infected
    expected = 127393355
    assert actual == expected


def test_get_report_based_on_avg_of_survivors():
    average_survivors = int(data_set['survivors'].mean())
    good_countries = []
    for i in data_set[data_set['survivors'] > average_survivors].Name:
        good_countries.append(i)
    actual = good_countries
    expected = ['Argentina', 'Australia', 'Austria', 'Belgium', 'Brazil', 'Canada', 'Chile', 'Colombia', 'Czech Republic', 'Denmark', 'France', 'Germany', 'Greece', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Israel', 'Italy', 'Japan', 'Korea (South)', 'Malaysia', 'Mexico', 'Netherlands', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Romania', 'Russian Federation', 'South Africa', 'Spain', 'Switzerland', 'Taiwan, Republic of China', 'Thailand', 'Turkey', 'Ukraine', 'United Kingdom', 'United States of America', 'Viet Nam']
    assert actual == expected


def test_get_report_based_on_avg_of_survivors2():
    average_survivors = int(data_set['survivors'].mean())
    bad_countries = []
    for i in data_set[data_set['survivors'] < average_survivors].Name:
        bad_countries.append(i)
    actual = bad_countries[:10]
    expected = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antarctica', 'Antigua and Barbuda', 'Armenia', 'Azerbaijan','Bahamas']
    assert actual == expected


def test_transportation_to_country():
    country_can_visit = []
    for i in data_set[data_set['NewConfirmed'] > 0].Name:
        country_can_visit.append(i)
    actual = country_can_visit[50:]
    expected = ['Mozambique', 'Myanmar', 'Nepal', 'Netherlands', 'New Zealand', 'Nigeria', 'Norway', 'Pakistan', 'Peru', 'Philippines', 'Poland', 'Qatar', 'Republic of Kosovo', 'Romania', 'Russian Federation', 'Rwanda', 'San Marino', 'Saudi Arabia', 'Senegal', 'Serbia', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'South Africa', 'Spain', 'Sri Lanka', 'Swaziland', 'Sweden', 'Taiwan, Republic of China', 'Thailand', 'Togo', 'Trinidad and Tobago', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States of America', 'Uzbekistan', 'Venezuela (Bolivarian Republic)', 'Viet Nam', 'Yemen']
    assert actual == expected

# ##############################################################


def test_total_NewConfirmed():
    actual = data_set['NewConfirmed'].sum()
    expected = 1791655
    assert actual == expected


def test_total_NewDeaths():
    actual = data_set['NewDeaths'].sum()
    expected = 5209
    assert actual == expected


def test_name_of_max_survivals_country():
    maxi = data_set['survivors'].max()
    row = data_set[data_set['survivors'] == maxi]
    actual = row.values[0][0]
    expected = 'United States of America'
    assert actual == expected


def test_name_of_min_survivals_country():
    maxi = data_set['survivors'].min()
    row = data_set[data_set['survivors'] == maxi]
    actual = row.values[0][0]
    expected = 'Korea (North)'
    assert actual == expected


def test_total_count_of_middle_east_regions():
    middle_east_view = data_set.loc[data_set['Region'] == 'Middle_East']
    actual = len(middle_east_view['Region'].values)
    expected = 15
    assert actual == expected


def test_total_count_of_western_europe_regions():
    middle_east_view = data_set.loc[data_set['Region'] == 'Western_Europe']
    actual = len(middle_east_view['Region'].values)
    expected = 30
    assert actual == expected


def test_total_count_of_other_regions():
    middle_east_view = data_set.loc[data_set['Region'] == 'Other']
    actual = len(middle_east_view['Region'].values)
    expected = 150
    assert actual == expected


def test_name_of_max_Fatality_ratio_country():
    maxi = data_set['Fatality_ratio'].max()
    row = data_set[data_set['Fatality_ratio'] == maxi]
    actual = row.values[0][0]
    expected = 'Korea (North)'
    assert actual == expected


def test_name_of_min_Fatality_ratio_country():
    maxi = data_set['Fatality_ratio'].min()
    row = data_set[data_set['Fatality_ratio'] == maxi]
    actual = row.values[0][0]
    expected = 'Antarctica'
    assert actual == expected



