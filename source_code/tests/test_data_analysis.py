import pytest
from source_code.api.data_analysis import *


def test_find_max_deaths():
    actual = find_max_deaths()
    expected = 1021838
    assert actual == expected


def test_find_min_deaths():
    actual = find_min_deaths()
    expected = 0
    assert actual == expected


def test_find_max_confirmed():
    actual = find_max_confirmed()
    expected = 88946276
    assert actual == expected


def test_find_min_confirmed():
    actual = find_min_confirmed()
    expected = 1
    assert actual == expected


def test_find_global_death():
    actual = find_global_death()
    expected = 6354573
    assert actual == expected


def test_find_global_confirmed():
    actual = find_global_confirmed()
    expected = 556684901
    assert actual == expected


def test_find_global_avg_death():
    actual = find_global_avg_death()
    expected = 32587.553846153845
    assert actual == expected


def test_find_global_avg_confirmed():
    actual = find_global_avg_confirmed()
    expected = 2854794.3641025643
    assert actual == expected


def test_total_survival_for_each_country():
    actual = total_survival_for_each_country()
    expected = [175544, 285875, 259428, 44518, 99420, 11, 8543, 9297026, 415142, 8595544, 4559249, 783671, 35477, 640475, 1961819, 85973, 986919, 4288092, 64828, 27053, 59919, 926685, 364172, 321401, 32330453, 178042, 1143357, 20657, 43022, 133318, 118137, 3368000, 61260, 14599, 7234, 4036218, 1489608, 6058646, 8049, 24035, 90361, 896409, 1144129, 1097961, 529431, 3903458, 83359, 3236844, 15501, 14784, 615118, 886643, 490920, 176806, 16321, 9724, 582535, 483005, 65536, 1153544, 32602409, 47852, 11644, 1645455, 29165961, 165759, 3812666, 18327, 936622, 36913, 8229, 67146, 31143, 29, 419760, 1886127, 198542, 43144331, 5959541, 7113566, 2365427, 1607095, 4461014, 19497930, 140980, 9775505, 1688592, 1380638, 330385, 3223, -5, 18577429, 645660, 198252, 209629, 836256, 1115932, 33338, 7208, 495859, 18141, 1156927, 271420, 307392, 64695, 84148, 4564917, 183184, 30455, 108730, 47, 60417, 232074, 5975456, 38, 509612, 13516, 927534, 241607, 1226668, 226555, 594326, 165185, 968638, 8231341, 1466396, 14478, 8785, 255730, 1448100, 387013, 1513317, 5302, 656926, 930407, 44090, 654793, 3477499, 3660773, 5908030, 5242095, 389375, 228882, 2880377, 17824948, 130272, 6287, 26952, 9013, 15105, 18770, 6005, 791646, 84558, 2028946, 44909, 7593, 1539341, 2538925, 1045913, 21391, 25539, 3896095, 17595, 12923867, 647789, 57840, 79542, 71810, 2504260, 3847908, 52807, 4124649, 17661, 35333, 4520017, 22839, 37361, 12370, 164396, 1058207, 15081387, 164813, 5209832, 963751, 22907048, 87924438, 957997, 240177, 11676, 522825, 10713164, 9683, 323094, 250416]
    assert actual == expected


def test_total_infected_middle_east():
    actual = total_infected_middle_east()
    expected = 30224899
    assert actual == expected


def test_total_infected_western_europe():
    actual = total_infected_western_europe()
    expected = 126630608
    assert actual == expected


def test_fatality_ratio_of_death_for_each_country():
    actual = fatality_ratio_of_death_for_each_country()
    expected = [4.22, 1.21, 2.58, 0.34, 1.88, 0.0, 1.65, 1.37, 2.04, 0.12, 0.44, 1.22, 2.26, 0.23, 1.47, 0.55, 0.72, 0.74, 1.04, 0.6, 0.04, 2.32, 4.16, 0.85, 2.04, 0.13, 3.16, 1.84, 0.09, 2.24, 1.61, 1.1, 0.66, 0.77, 2.6, 1.44, 0.97, 2.26, 1.95, 1.58, 1.5, 0.94, 1.39, 0.77, 0.2, 1.02, 0.96, 0.2, 1.2, 0.46, 0.71, 3.88, 4.79, 2.3, 1.11, 1.05, 0.45, 1.54, 1.31, 0.43, 0.46, 0.63, 3.04, 1.01, 0.48, 0.87, 0.79, 1.26, 1.96, 1.19, 2.04, 1.85, 2.62, 0.0, 2.53, 2.41, 0.09, 1.2, 2.56, 1.95, 1.06, 0.47, 0.25, 0.86, 2.19, 0.32, 0.83, 1.36, 1.69, 0.4, 600.0, 0.13, 0.39, 1.49, 0.36, 0.7, 0.93, 2.06, 3.92, 1.28, 0.47, 0.79, 0.4, 2.95, 2.12, 3.05, 0.78, 0.17, 2.36, 0.7, 0.0, 1.61, 0.43, 5.18, 0.0, 2.22, 0.44, 0.23, 1.12, 1.3, 0.97, 3.17, 2.4, 1.22, 0.27, 0.11, 1.65, 3.42, 1.21, 0.24, 1.18, 1.97, 0.11, 0.85, 0.89, 1.48, 2.83, 5.79, 1.63, 1.93, 0.46, 0.17, 1.36, 2.23, 2.05, 1.11, 0.71, 1.41, 1.25, 0.19, 0.61, 1.22, 1.15, 2.27, 0.79, 0.37, 1.62, 0.09, 0.79, 0.63, 0.71, 5.06, 2.55, 0.78, 0.84, 2.49, 7.89, 1.7, 1.94, 0.76, 0.36, 5.63, 0.19, 0.7, 2.32, 0.68, 0.58, 0.73, 0.1, 2.39, 2.65, 0.65, 2.15, 2.2, 0.24, 0.79, 1.15, 0.76, 0.68, 0.12, 1.09, 0.4, 18.16, 1.23, 2.17]
    assert actual == expected


def test_get_report_based_on_avg_of_survivors():
    actual1 = get_report_based_on_avg_of_survivors()[0]
    expected1 = ['Argentina', 'Australia', 'Austria', 'Belgium', 'Brazil', 'Canada', 'Chile', 'Colombia', 'Czech Republic', 'Denmark', 'France', 'Germany', 'Greece', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Israel', 'Italy', 'Japan', 'Korea (South)', 'Malaysia', 'Mexico', 'Netherlands', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Romania', 'Russian Federation', 'South Africa', 'Spain', 'Switzerland', 'Taiwan, Republic of China', 'Thailand', 'Turkey', 'Ukraine', 'United Kingdom', 'United States of America', 'Viet Nam']
    assert actual1 == expected1


def test_transportation_to_country():
    actual = transportation_to_country()
    expected = ['Australia', 'Brazil', 'Canada', 'Chile', 'China', 'Germany', 'India', 'Italy', 'Japan', 'Malaysia', 'Mexico', 'Netherlands', 'Pakistan', 'Peru', 'Russian Federation', 'Spain', 'United Kingdom', 'United States of America']

    assert actual == expected


