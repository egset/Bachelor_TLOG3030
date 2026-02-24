from src.vehicle import Vehicle
from src.machine import Machine


class Location:
    def __init__(self, name):
        self.name = name
        self.vehicle_counts = {}   # {"MB450": 70}
        self.vehicles = {}         # {"MB450": Vehicle-objekt}
        self.machines = []


def get_vehicle(self, vehicle_name):
        return self.vehicles.get(vehicle_name)


def get_machine(self, machine_code):
        for machine in self.machines:
            if machine.code == machine_code:
                return machine
        return None
   



