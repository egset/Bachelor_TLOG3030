import numpy as np
from src.distance.distance import Distance


"Denne filen tar inn et Location-objekt og lager en subklasse TruckLocation."
"Denne filen tar hensyn til pauser og hviletider i estimert reisetid, og er tilpasset realistiske forhold for lastebiltransport."


#TruckDistance arver fra Distance
class TruckDistance(Distance):

    def estimated_travel_time_realistic(
        self, # Lokasjon som skal kjøres fra
        other_location, # Lokasjon som skal kjøres til
        road_factor=1.5, # Forholdet mellom veiaavstand og luftlinjeavstand
        avg_speed=75, # Gjennomsnittshastighet (km/h) i Norge
        std_speed=8, # Standardavvik for hastighet (km/h)
        simulations=10_000, # Antall simuleringer for Monte Carlo
        max_driver_hours=4.5, # Maks kjøretid før pause (timer/dag)
        break_duration=0.75, # Pausevarighet (timer), 45 min
        max_daily_hours=9, # Maks kjøretid per dag (timer)
        daily_rest=11 # Døgnpause (timer) 
    ):
        
        # Luftlinje → vei
        air_distance = self.distance_to(other_location)
        road_distance = air_distance * road_factor


        # Simuler hastigheter
        velocities = np.random.normal(avg_speed, std_speed, simulations)
        velocities = velocities[velocities > 30]


        # Kjøretid
        driving_time = road_distance / velocities


        # Pauser etter 4,5 time
        num_breaks = np.floor(driving_time / max_driver_hours)
        pause_time = num_breaks * break_duration

        effective_time = driving_time + pause_time


        # Antall kjøredager
        days = np.ceil(effective_time / max_daily_hours)


        # Døgnpauser (ikke etter siste dag)
        daily_rest_time = np.maximum(0, days - 1) * daily_rest

        total_time = effective_time + daily_rest_time

        return {
            "mean_hours": np.mean(total_time),
            "std_hours": np.std(total_time),
            "min_hours": np.min(total_time),
            "max_hours": np.max(total_time),
            "share_multiday": np.mean(days > 1)
        }
