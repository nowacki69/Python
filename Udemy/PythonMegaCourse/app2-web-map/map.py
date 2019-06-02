import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])
type = list(data["TYPE"])


def color_producer(t):
    if t == 'Caldera' or t == 'Calderas':
        return 'red'
    elif t == 'Cinder cone'or t == 'Cinder cones':
        return 'beige'
    elif t == 'Complex volcano':
        return 'purple'
    elif t == 'Fissure vents':
        return 'blue'
    elif t == "Lava domes":
        return 'gray'
    elif t == 'Maar':
        return 'orange'
    elif t == 'Shield volcano' or t == 'Shield volcanoes':
        return 'pink'
    elif t == 'Stratovolcano' or t == 'Stratovolcanoes':
        return 'green'
    elif t == 'Volcanic field':
        return 'darkpurple'
    else:
        return 'white'


html = """<h4>Volcano Information:</h4>
Name: %s
<br>Height: %s m
<br>Type: %s
"""

map = folium.Map([40, -100], zoom_start=5, tiles="Mapbox Bright")
fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, nam, el, typ in zip(lat, lon, name, elev, type):
    iframe = folium.IFrame(html=html % (nam, str(el), typ), width=250, height=120)
    # fgv.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe),
    #                            icon=folium.Icon(color=color_producer(typ))))
    fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(iframe),
                                     fill_color=color_producer(typ), color='grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                            else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map.html")
