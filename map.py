import folium
from geopy.geocoders import Nominatim

film_studio_cities = ['Los Angeles', 'Rome', 'Wellington', 'Saint-Denis', 'Mumbai', 'Ouarzazate', 'Berlin']
film_studio = ['Hollywood', 'Cinecitta', 'Weta', 'La Cité du Cinéma', 'Bollywood', ' Atlas', 'Filmpark Babelsberg']
locations = list()
lst = list()
titles = list()
name = str()
city = str()
map = folium.Map()
year = input('Enter the year: ')
films = folium.FeatureGroup(name='Location')
studio = folium.FeatureGroup(name='Famous studio')
with open('C:\\Users\\Home\\Downloads\\locations.list') as text:
    for line in text:
        if (year in line) and ('(' in line):
            lst = line.strip().split()
            if (len(lst) == 5) and (year in lst[1]):
                titles.append(lst[0])
                del (lst[:2])
                name = list(lst[0])
                if name.pop() == ',':
                    for j in range(len(name)):
                        city += name[j]
                    if city not in locations:
                        locations.append(city)
                    city = str()
                    name = str()
                    if len(locations) == 25:
                        break

geolocator = Nominatim(user_agent="Map")
for i in range(len(locations)):
    location = geolocator.geocode(locations[i])
    if location == None:
        continue
    else:
        films.add_child(folium.Marker(location=[location.latitude, location.longitude],
                                      popup=titles[i],
                                      icon=folium.Icon()))

for j in range(len(film_studio)):
    location = location = geolocator.geocode(film_studio_cities[j])
    if location == None:
        continue
    else:
        studio.add_child(folium.CircleMarker(location=[location.latitude, location.longitude],
                                             radius=10,
                                             popup=film_studio[j],
                                             fill_color='green',
                                             color='red',
                                             fill_opacity=0.5))
map.add_child(films)
map.add_child(studio)
map.save('films.html')
