from src.part import Part


class Vehicle:
    def __init__(self, name):
        self.name = name
        self.parts = []  # liste av Part

    def add_part(self, part: Part):
        if part.vehicle == self.name:
            self.parts.append(part)

    def __repr__(self):
        return f"Vehicle({self.name}, parts={len(self.parts)})"