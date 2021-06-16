import unittest

from LoomManager import LoomManager
from Bench import Bench
from PneumaticLoom import PneumaticLoom
from HydraulicLoom import HydraulicLoom
from StopType import StopType
from FabricMaterial import FabricMaterial




class Test(unittest.TestCase):
    bench = Bench(fabric_material=FabricMaterial.SILK, model="model_001", weight=120, fabric_width=2, fabric_area=4,
                  power=1200)

    hydraulicloom = HydraulicLoom(fabric_material=FabricMaterial.WOOL, model="model_002", weight=220, fabric_width=4,
                                  fabric_area=16,
                                  power=1200, lubrication_system="+1", air_supply="+2", edge_forming_mechanism="+3")

    pneumaticloom = PneumaticLoom(fabric_material=FabricMaterial.LINEN, stop_type=StopType.AUTOMATIC, model="model_003",
                                  weight=200,
                                  fabric_width=3,
                                  fabric_area=9, number_of_revolutions_ps=4, flange_diameter=3)

    benches = LoomManager([bench, hydraulicloom, pneumaticloom])

    def test_sort_by_fabric_area(self):
        self.assertEqual(self.bench.sort_by_fabric_area([self.pneumaticloom, self.hydraulicloom, self.benches]), [self.pneumaticloom, self.hydraulicloom, self.benches])

    def test_sort_by_power(self):
        self.assertEqual(self.bench.sort_by_power([self.pneumaticloom, self.hydraulicloom, self.benches], True), [self.pneumaticloom, self.hydraulicloom, self.benches])

    def  test_search_by_stop_type(self):
        self.assertEqual(self.bench.search_by_stop_type(stop_type=StopType.AUTOMATIC), [self.benches])

