import pandas
import matplotlib.pyplot
"""based on https://www.census.gov/quickfacts/fact/table/US/RHI225218#RHI225218
    population estimates july1 2019"""
TOTAL_POPULATION = 328239525
WHITE_PERCENT = .765
BLACK_PERCENT = .134
WHITE_POP = TOTAL_POPULATION * WHITE_PERCENT
BLACK_POP = TOTAL_POPULATION * BLACK_PERCENT
url2 = 'https://simplemaps.com/data/us-cities'
mapinfo = pandas.read_csv(url2)
"""Turning csv data into pandas dataframe"""
def get_all_info():
    url = 'https://raw.githubusercontent.com/washingtonpost/data-police-shootings/master/fatal-police-shootings-data.csv'
    info = pandas.read_csv(url)
    return info

state_info = dict(get_all_info().groupby('state').size())

"""Returns all white information"""
def get_white_info(info):
    winfo = info.loc[info['race'] == 'W']
    return winfo
#print(get_white_info(get_all_info()))
def total_white_deaths(white_deaths):
    total_white = len(white_deaths)
    return total_white
"""Returns all black information"""
def get_black_info(info):
    binfo = info.loc[info['race'] == 'B']
    return binfo
"""Returns total number of black killings"""
def total_black_deaths(black_deaths):
    total_black = len(black_deaths)
    return total_black
"""Returns proportion of black to all-other race killings"""
def black_killings_to_other(black_deaths, all_deaths):
    total_black = len(black_deaths)
    total_all = len(all_deaths)
    proportion = float(total_black/total_all)
    return proportion
#print(black_killings_to_other(get_black_info(get_all_info()), get_all_info()))4
#0.2345447733233421

def black_unarmed_killings(black_deaths):
    black_unarmed = black_deaths.loc[black_deaths['armed'] == 'unarmed']
    return len(black_unarmed)

def print_total_black_unarmed_killings():
    print(black_unarmed_killings(get_black_info(get_all_info())))


def white_unarmed_killings(white_deaths):
    white_unarmed = white_deaths.loc[white_deaths['armed'] == 'unarmed']
    return len(white_unarmed)

def print_total_unarmed_killings():
    print("The total number of white unarmed killings is: " + str(white_unarmed_killings(get_white_info(get_all_info()))))
    print("The total number of black unarmed killings is: " + str(black_unarmed_killings(get_black_info(get_all_info()))))


def proportion_black_unarmed(total_black_killings, total_black_killings_unarmed):
    proportion_unarmed_black = total_black_killings_unarmed / total_black_killings
    return proportion_unarmed_black
def print_proportion_black_unarmed():
    print(proportion_black_unarmed(total_black_deaths(get_black_info(get_all_info())), (black_unarmed_killings(get_black_info(get_all_info())))))

def proportion_white_unarmed(total_white_killings, total_white_killings_unarmed):
    proportion_unarmed_white = total_white_killings_unarmed / total_white_killings
    return proportion_unarmed_white

def print_proportion_white_unarmed():
    print(proportion_white_unarmed(total_white_deaths(get_white_info(get_all_info())), (white_unarmed_killings(get_white_info(get_all_info())))))

def chance_of_being_killed_white(white_killings):
    chance_of_being_killed_white = white_killings / WHITE_POP
    return chance_of_being_killed_white
def print_chance_of_being_killed_white():
    print(chance_of_being_killed_white(total_white_deaths(get_white_info(get_all_info()))))

def chance_of_being_killed_black(black_killings):
    chance_of_being_killed_black = black_killings / BLACK_POP
    return chance_of_being_killed_black

def print_chance_of_being_killed_black():
    print(chance_of_being_killed_black(total_black_deaths(get_black_info(get_all_info()))))


def chance_of_being_killed_black_unarmed(total_black_killings_unarmed):
    chance_of_being_killed_black_unarmed = total_black_killings_unarmed / BLACK_POP
    return chance_of_being_killed_black_unarmed

def chance_of_being_killed_white_unarmed(total_white_killings_unarmed):
    chance_of_being_killed_white_unarmed = total_white_killings_unarmed / WHITE_POP
    return chance_of_being_killed_white_unarmed

def print_chance_of_being_killed_black_unarmed():
    print(chance_of_being_killed_black_unarmed(black_unarmed_killings(get_black_info(get_all_info()))))

def print_chance_of_being_killed_white_unarmed():
    print(chance_of_being_killed_white_unarmed(white_unarmed_killings(get_white_info(get_all_info()))))

print_chance_of_being_killed_white()
print_chance_of_being_killed_black()
print("If youre white youre this much as likely to be killed by police "  + str(chance_of_being_killed_white(total_white_deaths(get_white_info(get_all_info())))/chance_of_being_killed_black(total_black_deaths(get_black_info(get_all_info())))))
print("If youre black youre this much more likely to be killed by police " + str(chance_of_being_killed_black(total_black_deaths(get_black_info(get_all_info())))/chance_of_being_killed_white(total_white_deaths(get_white_info(get_all_info())))))

print_chance_of_being_killed_white_unarmed()
print_chance_of_being_killed_black_unarmed()
print("If youre black youre this much more likely to be killed by police without a weapon " + str(chance_of_being_killed_black_unarmed(black_unarmed_killings(get_black_info(get_all_info())))/chance_of_being_killed_white_unarmed(white_unarmed_killings(get_white_info(get_all_info())))))

#state_info = dict(get_all_info().groupby(['state', 'race']).size())
state_info = dict(get_all_info().groupby(['state']).size())
values = state_info.values()
keys = state_info.keys()
"""
keys = state_info.keys()
values = state_info.values()
barchart = matplotlib.pyplot.bar(keys, values)
matplotlib.pyplot.show("out.png")

"""
print(state_info)
print(keys)

