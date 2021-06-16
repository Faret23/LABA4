from FuelType import FuelType


class Machinery:
    def __init__(self, fuel_type: FuelType,  model: str = "", wheel_formula: str = "", mileage: float = 0, fuel_consumption_per_hour: float = 0):
        self.model = model
        self.fuel_type = fuel_type
        self.wheel_formula = wheel_formula
        self.mileage = mileage
        self.fuel_consumption_per_hour = fuel_consumption_per_hour

    def get_info(self):
        return f"model: {self.model} \n" \
               f"fuel type: {self.fuel_type} \n" \
               f"wheel formula: {self.wheel_formula} \n" \
               f"mileage: {self.mileage} \n" \
               f"fuel consumption per hour: {self.fuel_comsumption_per_hour} \n" \