import numpy as np
from geopy.geocoders import Nominatim # Gjør stednavn om til koordinater
from geopy.distance import geodesic # Beregner korteste avstand på mellom to punkter


"Klassen Location lager et objekt for et geografisk sted med navn og koordinater. "
"Koordinatene kan skrives inn direkte, eller hentes via geokoding basert på navnet."


# Konstruktøren
class Location:
    def __init__(self, name, latitude=None, longitude=None):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        if latitude is None or longitude is None:
            self.geocode()


    # Henter koordinater basert på stednavn dersom de ikke er oppgitt. Bruker OpenStreetMap via geopy.
    def geocode(self):
        geolocator = Nominatim(user_agent="location_app", timeout=10) 
        location = geolocator.geocode(self.name)

        if location is None:
            raise ValueError(f"Coordinates for {self.name} not found")
        self.latitude = location.latitude
        self.longitude = location.longitude
        

   # Regner avstanden i kilometer mellom to Location-objekter.
    def distance_to(self, other_location) -> float:
        point1 = (self.latitude, self.longitude)
        point2  = (other_location.latitude, other_location.longitude)
        return geodesic(point1, point2).kilometers
    

    def estimated_travel_time(self, other_location,
                              road_factor = 1.5,
                              avg_speed = 75,
                              std_speed = 8,
                              simulations = 1000):
        
        luftlinje = self.distance_to(other_location)
        veiavstand = luftlinje * road_factor

        hastigheter = np.random.normal(loc=avg_speed, scale=std_speed, size=simulations)
        hastigheter = hastigheter[hastigheter > 30]

        tider = veiavstand / hastigheter

        return {
            "mean_hours": np.mean(tider),
            "std_hours": np.std(tider),
            "min_hours": np.min(tider),
            "max_hours": np.max(tider)
        }
    

lillehammer = Location("Lillehammer", 60.5825, 11.0742)
bjerkvik = Location("Bjerkvik", 68.5468, 17.5757)

resultat = lillehammer.estimated_travel_time(bjerkvik)
print(f"Estimated travel time from Lillehammer to Bjerkvik: {resultat['mean_hours']:.2f} hours (± {resultat['std_hours']:.2f} hours)")


    


        