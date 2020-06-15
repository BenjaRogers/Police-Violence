import pandas
from geopy.geocoders import ArcGIS
import folium
from folium.plugins import FloatImage
from collections import Counter
from folium.plugins import MarkerCluster
import random

"""
Data created and extended to include Latitude and Longitude coordinates from 
'https://raw.githubusercontent.com/washingtonpost/data-police-shootings/master/fatal-police-shootings-data.csv'
"""
df = pandas.read_csv('updated_shootings_6-13-20.csv')
map = folium.Map(location=[39.8283, - 96.5795], zoom_start=4, width='75%')
legend_file = 'Map_legend.png'
"""
Create all Feature Groups:
1 for each year
1 for each racial class
1 for armed vs unarmed
"""
fg20 = folium.FeatureGroup(name="2020")
fg19 = folium.FeatureGroup(name="2019")
fg18 = folium.FeatureGroup(name="2018")
fg17 = folium.FeatureGroup(name="2017")
fg16 = folium.FeatureGroup(name="2016")
fg15 = folium.FeatureGroup(name="2015")
"""
Future implementation
cannot figure out how to make feature groups inclusive of one another.
"""
"""
fgW = folium.FeatureGroup(name="White, non-Hispanic")
fgB = folium.FeatureGroup(name="Black, non-Hispanic")
fgA = folium.FeatureGroup(name="Asian")
fgN = folium.FeatureGroup(name="Native American")
fgH = folium.FeatureGroup(name="Hispanic")
fgO = folium.FeatureGroup(name="Other")
fgNA = folium.FeatureGroup(name='Unknown')
"""
"""
Assign lists to individual variables
"""
lon = list(df['Longitude'])
lat = list(df['Latitude'])
year = list(df['date'])
name = list(df['name'])
race = list(df['race'])
armed = list(df['armed'])
manner_of_death = list(df['manner_of_death'])
threat_level = list(df['threat_level'])
fleeing = list(df['flee'])
body_camera = list(df['body_camera'])

"""
Create different colored icons based on whether the person was armed according to 
washington post 
"""
def fill_color_selector(race):
    if race == 'W':
        return 'red'
    if race == 'B':
        return 'blue'
    if race == 'A':
        return 'green'
    if race == 'N':
        return 'purple'
    if race == 'H':
        return 'orange'
    if race == 'O':
        return 'pink'

def color_icon(armed):
    if armed == 'unarmed':
        return 'grey'
    else:
        return 'black'
cluster = folium.plugins.MarkerCluster(name="People")
"""
HTML code to give popup the ability to google persons name when clicked.
"""

html = """
Name: <br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Date: %s <br>
Race: %s <br>
Armed: %s <br>
Threat Level: %s <br>
Fleeing: %s <br>
Body Camera: %s <br>
Manner of Death: %s <br>

"""

def offset_location_lat(lat):
    lt = float(lat) + (random.randint(-5, 5)/300)
    return lt

def offset_location_lon(lon):
    ln = float(lon) + (random.randint(-5, 5) / 300)
    return ln

"""Create Icons for appropriate Feature Group based on year """
for lt, ln, dt, arm, nm, rc, tl, flee, bc, mod in zip(lat, lon, year, armed, name, race, threat_level, fleeing, body_camera, manner_of_death):
    if lt != 'Latitude' and ln != 'Longitude':
        if '2020' in dt:
            iframe = folium.IFrame(html=html % (nm, nm, dt, rc, arm, tl, flee, bc, mod), width=200, height=100)
            fg20.add_child(folium.CircleMarker(location=[offset_location_lat(lt),offset_location_lon(ln)], popup=folium.Popup(iframe),
                                               radius=5, fill_color=fill_color_selector(rc), fill_opacity=.8,color=color_icon(arm), opacity=1).add_to(cluster))
        if '2019' in dt:
            iframe = folium.IFrame(html=html % (nm, nm, dt, rc, arm, tl, flee, bc, mod), width=200, height=100)
            fg19.add_child(folium.CircleMarker(location=[offset_location_lat(lt),offset_location_lon(ln)], popup=folium.Popup(iframe),
                                               radius=5, fill_color=fill_color_selector(rc), fill_opacity=.8,color=color_icon(arm), opacity=1).add_to(cluster))
        if '2018' in dt:
            iframe = folium.IFrame(html=html % (nm, nm, dt, rc, arm, tl, flee, bc, mod), width=200, height=100)
            fg18.add_child(folium.CircleMarker(location=[offset_location_lat(lt),offset_location_lon(ln)], popup=folium.Popup(iframe),
                                               radius=5, fill_color=fill_color_selector(rc), fill_opacity=.8,color=color_icon(arm), opacity=1).add_to(cluster))
        if '2017' in dt:
            iframe = folium.IFrame(html=html % (nm, nm, dt, rc, arm, tl, flee, bc, mod), width=200, height=100)
            fg17.add_child(folium.CircleMarker(location=[offset_location_lat(lt),offset_location_lon(ln)], popup=folium.Popup(iframe),
                                               radius=5, fill_color=fill_color_selector(rc), fill_opacity=.8,color=color_icon(arm), opacity=1).add_to(cluster))
        if '2016' in dt:
            iframe = folium.IFrame(html=html % (nm, nm, dt, rc, arm, tl, flee, bc, mod), width=200, height=100)
            fg16.add_child(folium.CircleMarker(location=[offset_location_lat(lt),offset_location_lon(ln)], popup=folium.Popup(iframe),
                                               radius=5, fill_color=fill_color_selector(rc), fill_opacity=.8,color=color_icon(arm), opacity=1).add_to(cluster))
        if '2015' in dt:
            iframe = folium.IFrame(html=html % (nm, nm, dt, rc, arm, tl, flee, bc, mod), width=200, height=100)
            fg15.add_child(folium.CircleMarker(location=[offset_location_lat(lt),offset_location_lon(ln)], popup=folium.Popup(iframe),
                                               radius=5, fill_color=fill_color_selector(rc), fill_opacity=.8,color=color_icon(arm), opacity=1).add_to(cluster))
"""
Add all icons from the following feature groups to map
"""
map.add_child(fg20)
map.add_child(fg19)
map.add_child(fg18)
map.add_child(fg17)
map.add_child(fg16)
map.add_child(fg15)
FloatImage(legend_file, bottom= 0, left=0).add_to(map)
cluster.add_to(map)
map.add_child(folium.LayerControl())

map.save('map2.html')

