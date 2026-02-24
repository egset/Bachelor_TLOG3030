
class Location:
    def __init__(self, name):
        self.name = name
        self.vehicle_counts = {}  # {"MB450": 70, ...}
        self.machines = []        # liste av Machine-objekter

    def add_vehicle(self, vehicle_name, amount):
        self.vehicle_counts[vehicle_name] = self.vehicle_counts.get(vehicle_name, 0) + int(amount)

    def add_machine(self, machine):
        self.machines.append(machine)

    def machine_codes(self):
        return {m.code for m in self.machines}

    def can_repair(self, part):
        return part.required_machines().issubset(self.machine_codes())

    def __repr__(self):
        return f"Location({self.name}, machines={len(self.machines)})"