import pandas
import time

from geopy.geocoders import ArcGIS
url = 'https://raw.githubusercontent.com/washingtonpost/data-police-shootings/master/fatal-police-shootings-data.csv'
#establish geofinder object
nom = ArcGIS(timeout=300)
#csv file to pull data from
info = pandas.read_csv(url)
# create an address that can be used by ARCGIS to create longitudinal and latitudinal coordinates
info['Address'] = info['city'] + ', ' + info['state'] + ', ' + 'USA'
total_length = len(info)
def make_file(data):
    data.to_csv('updated_shootings_6-13-20.csv', mode='a')
query_start = 0
query_end = query_start + 50
while query_start < total_length + 1:
    brevinfo = info[query_start:query_end]
    brevinfo['Coordinates'] = brevinfo['Address'].apply(nom.geocode)
    brevinfo["Latitude"] = brevinfo["Coordinates"].apply(lambda x: x.latitude if x != None else None)
    brevinfo["Longitude"] = brevinfo["Coordinates"].apply(lambda x: x.longitude if x != None else None)
    print(brevinfo)
    make_file(brevinfo)
    query_start += 50
    query_end += 50
    time.sleep(1)
