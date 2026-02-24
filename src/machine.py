
class Machine:
    def __init__(self, code, name, maintenance_stop, efficiency,
                 personnel_availability, cost_per_hour):
        self.code = code
        self.name = name
        self.maintenance_stop = int(maintenance_stop)
        self.efficiency = float(efficiency)
        self.personnel_availability = float(personnel_availability)
        self.cost_per_hour = float(cost_per_hour)

    def __repr__(self):
        return f"Machine({self.code}, {self.name})"