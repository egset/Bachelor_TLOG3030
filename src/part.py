
class Part:
    def __init__(self, material_nr, name, vehicle, machine_code,
                 workshop_time, price):
        self.material_nr = int(material_nr)
        self.name = name
        self.vehicle = vehicle
        self.machine_code = machine_code
        self.workshop_time = float(workshop_time)
        self.price = float(price)

    def required_machines(self):
        if not self.machine_code:
            return set()

        # Fjern mellomrom og splitt på "&"
        parts = self.machine_code.split("&")
        return {p.strip() for p in parts}