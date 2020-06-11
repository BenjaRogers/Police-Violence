import pandas
from geopy.geocoders import ArcGIS
import folium

map = folium.Map(location=[35.7796, - 78.6382], zoom_start=5)
fg = folium.FeatureGroup(name="My Map")
df = pandas.read_csv('updated_shootings.csv')

lon = list(df['Longitude'])
lat = list(df['Latitude'])
name = list(df['name'])
date = list(df['date'])
armed = list(df['armed'])
html = """
Name: <br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Date: %s
"""
def color_icon(armed):
    if armed == 'unarmed':
        return 'green'
    else:
        return 'red'


for lt, ln, nm, dt,arm in zip(lat, lon, name, date, armed):
    if lt != 'Latitude' and ln != 'Longitude':
        iframe = folium.IFrame(html=html % (nm, nm ,dt), width=200, height=100)
        fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe),
                                   icon =folium.Icon(color='green')))
map.add_child(fg)

map.save('map1.html')
