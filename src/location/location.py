from geopy.geocoders import Nominatim # Gjør stednavn om til koordinater


"Klassen Location lager et objekt for et geografisk sted med navn og koordinater. "
"Koordinatene kan skrives inn direkte, eller hentes via geokoding basert på navnet."

"Denne filen tar IKKE hensyn til pauser og hviletider i estimert reisetid."


# Konstruktøren
class Location:
    def __init__(self, name, latitude=None, longitude=None, inventory=None):
        """
        Location constructor
        
        :param name: str, navn på lokasjonen
        :param latitude: float, breddegrad
        :param longitude: float, lengdegrad
        :param inventory: dict, key = komponentens navn, value = mengde tilgjengelig
        """
        self.name = name
        self.inventory = inventory if inventory is not None else {}
        self.latitude = latitude
        self.longitude = longitude
        if latitude is None or longitude is None:
            self.geocode()


    """ Henter koordinater basert på stednavn dersom de ikke er oppgitt. Bruker OpenStreetMap via geopy """
    def geocode(self):
        geolocator = Nominatim(user_agent="location_app", timeout=10) 
        location = geolocator.geocode(self.name)

        if location is None:
            raise ValueError(f"Coordinates for {self.name} not found")
        self.latitude = location.latitude
        self.longitude = location.longitude
    


    def add_component(self, component, quantity):
        """Legger til komponenter i lokasjonens lager."""
        if component in self.inventory:
            self.inventory[component] += quantity
        else:
            self.inventory[component] = quantity
        print(f"{quantity} enheter av {component} lagt til ved {self.name}. Totalt: {self.inventory[component]}")
    


    def consume_component(self, component, quantity):
        """Forbruker komponenter fra lokasjonens lager."""
        if component not in self.inventory:
            print(f"{component} does not exist in inventory.")
            return False
        if self.inventory[component] < quantity:
            print(f"Ikke nok {component} i lageret. Tilgjengelig: {self.inventory[component]}")
            return False
        self.inventory[component] -= quantity
        print(f"{quantity} enheter av {component} forbrukt. Tilgjengelig: {self.inventory[component]}, {self.name}")
        return True
    


    def order_component(self, component, quantity):
        """Bestill komponenter fra lokasjonens lager."""
        print(f"Order: {quantity} enheter av {component}")
        success = self.consume_component(component, quantity)
        if not success:
            print(f"Bestilling kunne ikke fullføres. Tilgjengelig mengde: {self.inventory.get(component, 0)}")
        return success
    


    def show_inventory(self):
        """Viser innholdet i lokasjonens lager."""
        print(f"Lager '{self.name}', koordinater: ({self.latitude}, {self.longitude}):")
        for comp, qty in self.inventory.items():
            print(f"  {comp}: {qty} enheter")



