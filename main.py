from src.distance.truck_distance import TruckDistance    

def main(): 
    lillehammer = TruckDistance("Lillehammer", 60.5825, 11.0742)
    bjerkvik = TruckDistance("Bjerkvik", 68.5468, 17.5757)


    # Reisetid uten pauser (Det Google Maps ville estimert)
    res = lillehammer.estimated_travel_time(bjerkvik)
    print(f"Estimated travel time from Lillehammer to Bjerkvik: {res['mean_hours']:.2f} hours (± {res['std_hours']:.2f} hours)")


    # Realistisk reisetid for lastebil med pauser og hviletider
    result = lillehammer.estimated_travel_time_realistic(bjerkvik)
    print(f"Estimated realistic travel time from Lillehammer to Bjerkvik for trucks: {result['mean_hours']:.2f} hours (± {result['std_hours']:.2f} hours)")

if __name__ == "__main__":
    main()