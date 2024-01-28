"""
Uses the Google Maps API to generate a list of places and some information about them based on user input.
Google Maps API for Python docs:
https://googlemaps.github.io/google-maps-services-python/docs/index.html#googlemaps.Client.places_photo
"""
import googlemaps
from datetime import datetime
import pandas as pd
from latitude_longitude_test import get_lati_longi
from driving_distance_test import get_dist_dur
from typing import Any

api_key = 'AIzaSyCr1A8C-25fFAWtGudA3xfIzbswAEGTWWQ'

gmaps = googlemaps.Client(key=api_key)


def get_places(address: str, keyword: str, km: int) -> Any:
    """
    :param address: the starting address of the user
    :param keyword: what kind of nature the user is looking for
    :param km: how many km away the user is willing to go
    :return: a list of places containing the place name, latitude, longitude, and address of the place,
                distance in km and duration in minutes, average rating, and photo reference ID
    """
    location = get_lati_longi(api_key, address)
    place_list = gmaps.places(query=keyword, location=location, radius=km * 1000, language="English", type=keyword)
    place_results = place_list['results']
    places = []
    if len(place_results) == 0:
        print("No places found, sorry! Try a different search term.")
    else:
        for place in place_results:
            if 'name' in place:
                name = place['name']
            else:
                name = "N/A"
            if 'location' in place['geometry']:
                lat = place['geometry']['location']['lat']
                lng = place['geometry']['location']['lng']
            else:
                lat, lng = "N/A", "N/A"
            if 'formatted_address' in place:
                place_address = place['formatted_address']
                place_distance = get_dist_dur(api_key, address, place_address)[0]
                place_duration = get_dist_dur(api_key, address, place_address)[1]
            else:
                place_address, place_distance, place_duration = "N/A", "N/A", "N/A"
            if 'rating' in place:
                rating = place['rating']
            else:
                rating = "N/A"
            if 'photos' in place:
                photo_reference = place['photos'][0]['photo_reference']
            else:
                photo_reference = "N/A"
            places.append((name,
                           lat, lng, place_address,
                           place_distance, place_duration,
                           rating,
                           photo_reference))
    return places


def get_directions(address: str, end_address: str, mode: str) -> Any:
    """
    :param address: the starting address of the user
    :param end_address: the address of the place
    :param mode: preferred mode of transportation
    :return: Google Maps directions to the place
    """
    now = datetime.now()
    directions_result = gmaps.directions(address,
                                         end_address,
                                         mode,
                                         departure_time=now)
    return directions_result


def get_picture(photo_reference: str, photo_name: str) -> None:
    """
    Saves a photo of the given place.
    :param photo_reference: A unique photo identifier given by get_places
    :param photo_name: The name of the place
    :return: None
    """
    f = open(photo_name+'.png', 'wb')
    for chunk in gmaps.places_photo(photo_reference, max_width=400, max_height = 400):
        if chunk:
            f.write(chunk)
    f.close()


def places_to_dataframe(places: list[Any]) -> pd.DataFrame:
    """
    :param places: Output of get_places
    :return: A pandas dataframe containing the data in get_places that the user would want to see
    """
    df = pd.DataFrame(places)
    df = df.drop([1, 2, 7], axis=1)
    df.columns = ["Name of place", "Address", "km away", "Minutes away", "Rating out of 5"]
    return df


def sort_dataframe(df: pd.DataFrame, parameter: str) -> pd.DataFrame:
    """
    :param df: Output of places_to_dataframe
    :param parameter: Column to sort the dataframe by (number columns only)
    :return: Dataframe sorted by given parameter
    """
    return df.sort_values(by=parameter)
