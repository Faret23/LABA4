from Machinery import Machinery
from FuelType import FuelType


class Loader(Machinery):
    def __init__(self, fuel_type: FuelType,
                 model: str = "",
                 wheel_formula: str = "",
                 mileage: float = 0,
                 fuel_comsumption_per_hour: float = 0,
                 load_capacity_in_grams: int = 0,
                 angle_of_the_lift: int = 0):
        super().__init__(fuel_type, model, wheel_formula, mileage, fuel_comsumption_per_hour)
        self.load_capcity_in_grams = load_capacity_in_grams
        self.angle_of_the_lift = angle_of_the_lift

    def get_info(self):
        return f"model: {self.model} \n" \
               f"fuel type: {self.fuel_type} \n" \
               f"wheel formula: {self.wheel_formula} \n" \
               f"mileage: {self.mileage} \n" \
               f"fuel consumption per hour: {self.fuel_comsumption_per_hour} \n" \
               f"load capacity in grams: {self.load_capcity_in_grams} \n" \
               f"angle of the lift: {self.angle_of_the_lift} \n" \