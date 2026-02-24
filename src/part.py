

class Part:
    def __init__(self, material_nr, name, vehicle, machine, workshop_time, price):
        self.material_nr = int(material_nr)
        self.name = name
        self.vehicle = vehicle          # f.eks. "MB450"
        self.machine = machine          # f.eks. "A1 & M2"
        self.workshop_time = float(workshop_time)  # "Tid i verksted"
        self.price = float(price)       # "Innkjøpspris"

    def __repr__(self):
        return f"Part({self.material_nr}, {self.name}, vehicle={self.vehicle})"