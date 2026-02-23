from src.location.distance import Distance 

def main():
    # Opprett to lager/lokasjoner
    warehouse1 = Distance("Stryn", latitude=61.83, longitude=6.78)
    warehouse2 = Distance("Oslo", latitude=59.91, longitude=10.75)

    # Legg til komponenter i lager 1
    #warehouse1.add_component("Screws", 100)
    #warehouse1.add_component("Nuts", 50)

    # Bestill og forbruk komponenter
    #warehouse1.order_component("Screws", 20)
    #warehouse1.consume_component("Nuts", 10)

    # Vis lagerstatus
    #warehouse1.show_inventory()

    # Vis lagerstatus for lager 2 (tomt lager)
    #warehouse2.show_inventory()

    # Beregn avstand mellom lager 1 og lager 2
    distance_km = warehouse1.distance_to(warehouse2)
    print(f"\nDistance from {warehouse1.name} to {warehouse2.name}: {distance_km:.2f} km")

    # Estimer reisetid mellom lager 1 og lager 2
    travel_stats = warehouse1.estimated_travel_time(warehouse2)
    print("\nEstimated travel time (hours):")
    print(f"Mean: {travel_stats['mean_hours']:.2f} h")
    print(f"Std: {travel_stats['std_hours']:.2f} h")
    print(f"Min: {travel_stats['min_hours']:.2f} h")
    print(f"Max: {travel_stats['max_hours']:.2f} h")

if __name__ == "__main__":
    main()