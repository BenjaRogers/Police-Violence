import pandas
from geopy.geocoders import ArcGIS
import folium

map = folium.Map(location=[35.7796, - 78.6382], zoom_start=100)

fg = folium.FeatureGroup(name="My Map")

df = pandas.read_csv('updated_shootings.csv')

lon = list(df['Longitude'])
lat = list(df['Latitude'])

for lt, ln in zip(lat, lon):
    if lt != 'Latitude' and ln != 'Longitude':
        map.add_child(folium.Marker(location=[lt, ln], icon = folium.Icon(color = 'black')))
map.add_child(fg)

map.save('map1.html')
