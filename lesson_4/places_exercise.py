'''
# HEY
# Google places API exercise

# Places in vicinity

1. Build a function that given a string, returns all places that contain the
string

>>> find_places('IAL')
[('IAL', 12.5, 41.95)]


2. Build a function that given a place, returns a list of places nearby

>> > nearby_places({})
[{'name': 'ciao'}]

3. Get place name from command line argument

> >> import subprocess
> >> subprocess.check_output(['places_exercise.py', 'IAL'])
ciao
'''

import urllib.request
import urllib.parse
import json
import pprint


def find_places(place_name):
    KEY = 'AIzaSyBnTJ0P-nXBgUEut5z_EZYQVwudWl4lP1E'
    qs = urllib.parse.urlencode({'query': place_name, 'key': KEY, 'sensor': 'false'})
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?' + qs
    resp = urllib.request.urlopen(url).read()
    data = json.loads(resp.decode())
    pprint.pprint(data)
    return [res['geometry']['location'] for res in data['results']]


def nearby_place(lat, lng):
    pass
