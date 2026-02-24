from src.loaders import load_locations_with_machines, load_vehicles_with_parts


def main():
    locations = load_locations_with_machines("maskiner.csv")
    vehicles = load_vehicles_with_parts("deler.csv")

    mb450 = vehicles.get("MB450")

    if mb450 and mb450.parts:
        part = mb450.parts[0]

        print("Del:", part)
        print("Kan Sted A reparere?",
              locations["Sted A"].can_repair(part))


if __name__ == "__main__":
    main()