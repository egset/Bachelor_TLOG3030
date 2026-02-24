

class Vehicle:
    def __init__(self, name):
        self.name = name
        self.parts = []   # liste med Part-objekter

    def add_part(self, part):
        # sikkerhet: delen må høre til riktig kjøretøy
        if part.vehicle != self.name:
            return
        self.parts.append(part)

    def __repr__(self):
        return f"Vehicle({self.name}, parts={len(self.parts)})"
        