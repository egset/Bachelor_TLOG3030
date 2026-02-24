import csv
from src.part import Part


class Vehicle:
    def __init__(self, name,is_active=True):
        self.name = name
        self.is_active = is_active # indikerer om kjøretøyet er operasjonelt eller ikke
        self.parts = {}  # dictionary med material_nr -> Part


    def add_part(self, part: Part):
        if part.vehicle == self.name:
            self.parts[part.material_nr] = part

    
    # Velger om kjøretøyet skal være aktivt eller ikke, basert på om noen deler er i verksted
    def set_active(self, active: bool):
        self.is_active = active


    def check_active_status(self):
        # Hvis noen deler er i verksted, er kjøretøyet ikke aktivt
        for part in self.parts:
            if part.time_in_workshop > 0:
                self.is_active = False
                return
        self.is_active = True

    def __repr__(self):
        return f"Vehicle({self.name}, parts={len(self.parts)})"