from Machinery import Machinery
from FuelType import FuelType
from typing import List

class MachineryManager:
    def __init__(self, machines = list):
        self.machines = machines

    def sort_by_mileage(self, machines: List[Machinery], reverse: bool = False):
        return sorted(machines, key=lambda s: s.mileage, reverse=reverse)

    def sort_by_fuel_consumption(self, machines: List[Machinery], reverse: bool = False):
        return sorted(machines, key=lambda s: s.fuel_consumption_per_hour, reverse=reverse)

    def search_by_fuel_type(self, fuel_type: FuelType):
        return [machines for machines in self.machines if machines.fuel_type == fuel_type]

    def search_by_wheel_formula(self, wheel_formula):
        return [machines for machines in self.machines if machines.wheel_formula == wheel_formula]