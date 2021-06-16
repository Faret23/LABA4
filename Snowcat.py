from Material import Material
from Machinery import Machinery
from FuelType import FuelType


class Snowcat(Machinery):
    def __init__(self, fuel_type: FuelType, material_of_the_tracks: Material, model: str = "", wheel_formula: str = "", mileage: float = 0, fuel_comsumption_per_hour: float = 0, bucket_scope_in_meters: float = 0):
        super().__init__(fuel_type, model, wheel_formula, mileage, fuel_comsumption_per_hour)
        self.bucket_scope_in_meters = bucket_scope_in_meters
        self.material_of_the_tracks = material_of_the_tracks

    def get_info(self):
        return f"model: {self.model} \n" \
               f"fuel type: {self.fuel_type} \n" \
               f"wheel formula: {self.wheel_formula} \n" \
               f"mileage: {self.mileage} \n" \
               f"fuel consumption per hour: {self.fuel_comsumption_per_hour} \n" \
               f"bucket scope in meters: {self.bucket_scope_in_meters} \n" \
               f"material of the tracks: {self.material_of_the_tracks} \n" \