import json
from pprint import pprint
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

with open("blm.json", "r") as fp:
    data = json.load(fp)

features = data["features"]
print(len(features))

my_loc = Point(39.675052, -112.663235)

found_place = None

for i, feat in enumerate(features):
    try:
        points = []
        for coord in feat["geometry"]["coordinates"][0][0]:
            points.append((coord[1], coord[0]))

        poly = Polygon(points)
        if poly.contains(my_loc):
            found_place = feat
    except:
        print(f"Exception on entry {i}")
        raise

print(f"You are on {found_place['properties']}")