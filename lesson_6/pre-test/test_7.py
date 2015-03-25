import json
import urllib.request


def unique_names():
    data = urllib.request.urlopen('http://private-bb81a-ialpython.apiary-mock.com/people')
    data = json.loads(data.read().decode())
    names = list(set(data.values()))
    return names
