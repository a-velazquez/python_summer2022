# TODO: write code to answer the following questions:
# 1) which of these embassies is closest to the White House in meters?
# how far is it, and what is the address?
# 2) if I wanted to hold a morning meeting there, which cafe would you suggest (best rating and closest)?
# 3) if I wanted to hold an upscale evening meeting there, which fancy bar would you suggest?
# for 2 and 3, you will need to enable the google places API
# you may find this page useful to learn about different findinging nearby places https://www.geeksforgeeks.org/python-fetch-nearest-hospital-locations-using-googlemaps-api/


import importlib
import os
import googlemaps
import pandas as pd

imported_items = importlib.import_module("start_google")
gmaps = imported_items.client

whitehouse = "1600 Pennsylvania Avenue, Washington, DC"

wh = gmaps.geocode(whitehouse)
wh_loc = wh[0]["geometry"]["location"]

embassies = [
    [38.917228, -77.0522365],
    [38.9076502, -77.0370427],
    [38.916944, -77.048739],
]


locations = []
for e in embassies:
    temp_loc = {"lat": e[0], "lng": e[1]}
    locations.append(temp_loc)

distances = []
for l in locations:
    distance = gmaps.distance_matrix(wh_loc, l)
    distances.append([l, distance["rows"][0]["elements"][0]["distance"]["text"]])


address_string = ""
for item in gmaps.reverse_geocode(locations[1])[0]["address_components"]:
    address_string += item["short_name"] + " "


cafes = gmaps.places_nearby(locations[1], 1000, "cafe")


cafes["results"][0].keys()


def get_places(keyword, values, asc):
    place_info = {"name": [], "location": [], "rating": [], "distance": [], "price": []}

    places = gmaps.places_nearby(locations[1], 1000, keyword)

    for p in places["results"]:
        place_info["name"].append(p["name"])
        place_info["location"].append(p["geometry"]["location"])
        place_info["rating"].append(p["rating"])
        if "price_level" in p:
            place_info["price"].append(p["price_level"])
        else:
            place_info["price"].append(None)

    for loc in place_info["location"]:
        d_temp = gmaps.distance_matrix(locations[1], loc)
        place_info["distance"].append(
            d_temp["rows"][0]["elements"][0]["distance"]["text"]
        )

    df = pd.DataFrame(place_info)

    values.append("name")

    end = df.sort_values(values[:-1], ascending=asc)[values].head()

    return end


cafe_df = get_places("cafe", ["rating", "distance"], [False, True])

bar_df = get_places("bar", ["rating", "distance", "price"], [False, True, False])
