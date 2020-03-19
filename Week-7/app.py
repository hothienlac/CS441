from ipywidgets.embed import embed_minimal_html
import gmaps
import requests
import pandas as pd
import urllib.parse
import json
from ast import literal_eval as make_tuple
gmaps.configure(api_key='AIzaSyCZ0PPD0mymbJqX4ESYnuASb-wHXcC3zos')









emp = pd.read_csv('./em.csv')
emp = emp[emp['lng'] != '0']
emp = emp.to_dict(orient='records')

emp_locations = [make_tuple(e['lng']) for e in emp]


info_box_template = """
<dl>
<dt>ID</dt><dd>{employee_id}</dd>
<dt>Address</dt><dd>{lat}</dd>
</dl>
"""

emp_info = [info_box_template.format(**e) for e in emp]

san_francisco_coordinates = (37.773972, -122.431297)
fig = gmaps.figure(center=san_francisco_coordinates, zoom_level=12)

emp_layer = gmaps.symbol_layer(emp_locations, info_box_content=emp_info,
                        stroke_opacity=0.2, fill_opacity= 0.2,
                        fill_color='red', stroke_color='red', scale=2)

fig.add_layer(emp_layer)


bus = pd.read_csv('./intersections.csv')

bus = bus.to_dict(orient='records')
bus_locations = [(e['lat'], e['lng']) for e in bus]


info_box_template = """
<dl>
<dt>Station</dt><dd>{Street_Two}</dd>
</dl>
"""

bus_info = [info_box_template.format(**b) for b in bus]

bus_layer = gmaps.symbol_layer(bus_locations, info_box_content=bus_info,
                        stroke_opacity=0.5, fill_opacity= 0.5,
                        fill_color='blue', stroke_color='blue', scale=2)

fig.add_layer(bus_layer)

embed_minimal_html('map.html', views=[fig])
