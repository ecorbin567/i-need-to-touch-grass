"""
Uses the Google Maps API to get the distance and duration that it takes to get from one location to another.
Code from https://blog.apify.com/google-maps-api-python/
Google Maps API for Python docs:
https://googlemaps.github.io/google-maps-services-python/docs/index.html#googlemaps.Client.places_photo
"""

import requests


def get_dist_dur(api_key, start, end):

    base_url = "https://maps.googleapis.com/maps/api/distancematrix/json"

    params = {

        "origins": start,

        "destinations": end,

        "key": api_key

    }



    response = requests.get(base_url, params=params)



    if response.status_code == 200:

        data = response.json()

        if data["status"] == "OK":

            distance = data["rows"][0]["elements"][0]["distance"]["text"]

            duration = data["rows"][0]["elements"][0]["duration"]["text"]

            return distance, duration

        else:

            print("Request failed.")

            return None, None

    else:

        print("Failed to make the request.")

        return None, None