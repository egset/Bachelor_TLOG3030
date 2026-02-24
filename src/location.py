
class Location:
    def __init__(self, name):
        self.name = name
        self.vehicle_counts = {}  # {"MB450": 70, ...}

    def add_vehicles(self, vehicle_name, amount):
        self.vehicle_counts[vehicle_name] = self.vehicle_counts.get(vehicle_name, 0) + int(amount)

    def get_count(self, vehicle_name):
        return self.vehicle_counts.get(vehicle_name, 0)

    def __repr__(self):
        return f"Location({self.name}, vehicle_types={len(self.vehicle_counts)})"