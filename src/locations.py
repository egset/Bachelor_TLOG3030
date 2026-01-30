from geopy.geocoders import Nominatim

#Denne klassen lager lagrer byer og deres posisjon.
#Mulig å legge til flere funksjoner senere.

class Location:
    def __init__(self, name):
        self.name = name
        self.latitude = None
        self.longitude = None
        self.geocode()

    def geocode(self):
        geolocator = Nominatim(
            user_agent="location_app",
            timeout=10
        )

        location = geolocator.geocode(self.name, exactly_one=True)

        if location is None:
            raise ValueError(f"Fant ikke koordinater for {self.name}")

        self.latitude = location.latitude
        self.longitude = location.longitude


oslo = Location("oslo") 
print(oslo.latitude, oslo.longitude)