
from math import cos, sin, radians, atan2, sqrt
radius = 6371  # km

# voila la modification

def distance(origin, destination):
    """
    Determine distance between 2 sets of [lat,lon] in km
    """
    if origin == destination:
        return 0
# fin de la modification du fichier initial

    lat1, lon1 = origin[0], origin[1]
    lat2, lon2 = destination[0], destination[1]
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    sindlat = sin(dlat / 2)
    sindlon = sin(dlon / 2)
    a = (sindlat * sindlat +
         cos(radians(lat1)) *
         cos(radians(lat2)) *
         sindlon * sindlon)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    d = radius * c

    return d
