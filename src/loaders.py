
from pathlib import Path
import csv

from src.machine import Machine
from src.location import Location
from src.part import Part
from src.vehicle import Vehicle


"Veit ikke helt hva denne skal gjøre. La den stå så lenge"



# prosjektrot = mappen som inneholder "src" og "data-ugradert"
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data-ugradert"


def load_locations_with_machines(filename="maskiner.csv"):
    path = DATA_DIR / filename
    locations = {}

    with open(path, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sted = row["Sted"]

            if sted not in locations:
                locations[sted] = Location(sted)

            machine = Machine(
                row["MaskinNr"],
                row["Maskinens navn"],
                row["Vedlikeholds stopp per år"],
                row["Produksjons effektivitet"],
                row["Tilgjengelighet personell"],
                row["Kostnad per time"],
            )

            locations[sted].add_machine(machine)

    return locations


def load_vehicles_with_parts(filename="deler.csv"):
    path = DATA_DIR / filename
    vehicles = {}

    with open(path, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            part = Part(
                row["MaterialNr"],
                row["Delens navn"],
                row["Kjøretøy"],
                row["MaskinNr"],
                row["Tid i verksted"],
                row["Innkjøpspris"],
            )

            vname = part.vehicle
            if vname not in vehicles:
                vehicles[vname] = Vehicle(vname)

            vehicles[vname].add_part(part)

    return vehicles