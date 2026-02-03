import numpy as np
from geopy.distance import geodesic # Beregner korteste avstand på mellom to punkter
from src.location.location import Location

"Klassen Distance arver fra et Location-objekt og regner avstand og estimert reisetid mellom to lokasjoner."
"Denne filen tar IKKE hensyn til pauser og hviletider i estimert reisetid."

class Distance(Location):


    """Kalkulerer avstand (luftlinje) i km multiplisert med veifaktor."""
    def distance_to(self, other_location, road_factor=1.5) -> float:
        point1 = (self.latitude, self.longitude)
        point2 = (other_location.latitude, other_location.longitude)
        return geodesic(point1, point2).kilometers * road_factor


    """Estimerer reisetid langs vei ved bruke av Monte Carlo-metoden."""
    def estimated_travel_time(self, other_location,
                              road_factor=1.5, #forholdet mellom luftlinje og veilengde
                              avg_speed=75,  # km/h
                              std_speed=8,   # km/h
                              simulations=10_000):
        
        air_distance = self.distance_to(other_location, road_factor=1)  # luftlinje
        road_distance = air_distance * road_factor

        velocity = np.random.normal(loc=avg_speed, scale=std_speed, size=simulations)
        velocity = velocity[velocity > 30]  # fjern urealistisk lave hastigheter

        times = road_distance / velocity

        return {
            "mean_hours": np.mean(times),
            "std_hours": np.std(times),
            "min_hours": np.min(times),
            "max_hours": np.max(times)
        }





    


        