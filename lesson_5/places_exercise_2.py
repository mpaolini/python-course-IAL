'''
1. Website for places

Build a function that given a string, returns all websites found

Factor out all common code for place search and place details.

>> websites = find_place_websites('IAL')
>> websites[0]
'http://www.ial.lazio.it/'


2. reviews for places

Find average rating for all place reviews. None if no reviews found.

(use common utilities functions written for point 1.)

>>> find_place_reviews('Rosticceria')
3.75

3. modify the above functions to visit *all* the pages in the search result
'''

import requests

KEY = 'AIzaSyDv4yY43goypjC6BXZYCcaaXySvbsFAxTA'


def search_place(place_name):
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    params = {
        'query': place_name,
        'key': KEY
    }
    resp = requests.get(url, params=params)
    data = resp.json()
    return data


def get_details(place_id):
    resp2 = requests.get(
        'https://maps.googleapis.com/maps/api/place/details/json',
        params={'key': KEY,
                'placeid': place_id}
    )
    detail = resp2.json()
    return detail


def find_place_websites(place_name):
    data = search_place(place_name)
    websites = []
    for place in data['results']:
        detail = get_details(place['place_id'])
        if 'website' in detail['result']:
            websites.append(detail['result']['website'])
    return websites


def find_place_reviews(place_name):
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    params = {
        'query': place_name,
        'key': KEY
    }
    resp = requests.get(url, params=params)
    data = resp.json()
    reviews = []
    for place in data['results']:
        resp2 = requests.get(
            'https://maps.googleapis.com/maps/api/place/details/json',
            params={'key': KEY,
                    'placeid': place['place_id']}
        )
        detail = resp2.json()
        try:
            reviews.append(detail['result']['rating'])
        except KeyError:
            pass
    if len(reviews) == 0:
        return None
    return sum(reviews) / len(reviews)
