from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Denne klassen lagrer byer og deres posisjon.
# Mulig å legge til flere funksjoner senere.

class Location:
    def __init__(self, name, latitude=None, longitude=None):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        if latitude is None or longitude is None:
            self.geocode()

    def geocode(self):
        geolocator = Nominatim(user_agent="location_app", timeout=10)
        location = geolocator.geocode(self.name)
        if location is None:
            raise ValueError(f"Fant ikke koordinater for {self.name}")
        self.latitude = location.latitude
        self.longitude = location.longitude


    # Regner ut avstanden mellom to Location-objekter
    def distance_to(self, other_location) -> float:
        """
        Beregn avstanden til et annet Location-objekt i kilometer.
        """
        point1 = (self.latitude, self.longitude)
        point2 = (other_location.latitude, other_location.longitude)
        return geodesic(point1, point2).kilometers


# Hardkodede koordinater for testing uten nett
oslo = Location("Oslo", 59.9139, 10.7522)
bergen = Location("Bergen", 60.3913, 5.3221)

dist = oslo.distance_to(bergen)
print(f"Avstanden mellom {oslo.name} og {bergen.name} er ca {dist:.2f} km i luftlinje.")