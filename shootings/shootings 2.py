import pandas
from geopy.geocoders import ArcGIS
import folium

map = folium.Map(location=[35.7796, - 78.6382], zoom_start=100)
nom = ArcGIS(timeout=300)

fg = folium.FeatureGroup(name="My Map")

info = pandas.read_csv('fatal-police-shootings-data.csv')

info['Address'] = info['city'] + ', ' + info['state'] + ', ' + 'USA'
brevinfo = info[:50]

brevinfo['Coordinates'] = brevinfo['Address'].apply(nom.geocode)
brevinfo["Latitude"] = brevinfo["Coordinates"].apply(lambda x: x.latitude if x != None else None)
brevinfo["Longitude"] = brevinfo["Coordinates"].apply(lambda x: x.longitude if x != None else None)
lon = list(brevinfo['Longitude'])
lat = list(brevinfo['Latitude'])
pandas.DataFrame.to_csv(brevinfo)
for lt, ln in zip(lat, lon):
    map.add_child(folium.Marker(location=[lt, ln], icon = folium.Icon(color = 'black')))
map.add_child(fg)

map.save('map.html')