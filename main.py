from MachineryManager import MachineryManager
from Machinery import Machinery
from Loader import Loader
from FuelType import FuelType
from Snowcat import Snowcat
from Material import Material


def main():
    machinery = Machinery(fuel_type=FuelType.DIESEL, model="model_001", wheel_formula="5x2", mileage=430,
                          fuel_consumption_per_hour=2)
    loader = Loader(fuel_type=FuelType.GASOLINE, model="model_002", wheel_formula="7x1", mileage=500,
                    fuel_comsumption_per_hour=4, load_capacity_in_grams=10000000, angle_of_the_lift=90)
    snowcat = Snowcat(fuel_type=FuelType.GAS, material_of_the_tracks=Material.STEEL, model="model_003",
                      wheel_formula="4x2",
                      mileage=350, fuel_comsumption_per_hour=3, bucket_scope_in_meters=3)
    machine = MachineryManager([machinery, loader, snowcat])

    print('Sorted by mileage in ascending order:\n' + str(machine.sort_by_mileage([machinery, loader, snowcat])) + '\n')
    print('Sorted by fuel consumption in descending order:\n' + str(machine.sort_by_fuel_consumption([machinery, loader, snowcat],True)) + '\n')
    print('Searching the object by the fuel type: ' + str(machine.search_by_fuel_type(fuel_type=FuelType.DIESEL)) + '\n')
    print('Searching the object by the wheel formula: ' + str(machine.search_by_wheel_formula(wheel_formula="7x1")) + '\n')

if __name__ == '__main__':
    main()