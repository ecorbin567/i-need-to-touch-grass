"""
Uses the Google Maps API to get the latitude and longitude of a given address.
Code from https://blog.apify.com/google-maps-api-python/
Google Maps API for Python docs:
https://googlemaps.github.io/google-maps-services-python/docs/index.html#googlemaps.Client.places_photo
"""

import requests


def get_lati_longi(api_key, address):
    url = 'https://maps.googleapis.com/maps/api/geocode/json'

    params = {

        "address": address,

        "key": api_key

    }

    response = requests.get(url, params=params)

    if response.status_code == 200:

        data = response.json()

        if data["status"] == "OK":

            location = data["results"][0]["geometry"]["location"]

            lat = location["lat"]

            lng = location["lng"]

            return lat, lng

        else:

            print(f"Error: {data['error_message']}")

            return 0, 0

    else:

        print("Failed to make the request.")

        return 0, 0