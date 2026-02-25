import unittest
from Lab4task2 import Name, Length, Speed, Capacity, Year, SeaBoat
class TestSeaBoat(unittest.TestCase):
    def setUp(self):
        self.boats = [
            SeaBoat(Name("Odessa"), Length(30.5), Speed(45), Capacity(120), Year(2010)),
            SeaBoat(Name("Neptune"), Length(25.0), Speed(60), Capacity(80), Year(2015)),
            SeaBoat(Name("BlackSea"), Length(40.2), Speed(50), Capacity(200), Year(2008)),
            SeaBoat(Name("Poseidon"), Length(35.0), Speed(55), Capacity(150), Year(2012)),
            SeaBoat(Name("Atlantis"), Length(28.7), Speed(48), Capacity(100), Year(2018))
        ]

    def test_equality(self):
        boat1 = SeaBoat(Name("Odessa"), Length(30.5), Speed(45), Capacity(120), Year(2010))
        boat2 = SeaBoat(Name("Odessa"), Length(30.5), Speed(45), Capacity(120), Year(2010))
        boat3 = SeaBoat(Name("Neptune"), Length(25.0), Speed(60), Capacity(80), Year(2015))
        self.assertEqual(boat1, boat2)
        self.assertNotEqual(boat1, boat3)

    def test_sort_by_length(self):
        sorted_boats = sorted(self.boats, key=lambda b: b.length.meters)
        lengths = [b.length.meters for b in sorted_boats]
        self.assertEqual(lengths, sorted(lengths))

    def test_sort_by_speed_desc(self):
        sorted_boats = sorted(self.boats, key=lambda b: -b.speed.kmh)
        speeds = [b.speed.kmh for b in sorted_boats]
        self.assertEqual(speeds, sorted(speeds, reverse=True))

    def test_search_boat(self):
        target = SeaBoat(Name("Poseidon"), Length(35.0), Speed(55), Capacity(150), Year(2012))
        found = any(b == target for b in self.boats)
        self.assertTrue(found)

    def test_repr(self):
        boat = self.boats[0]
        self.assertIsInstance(repr(boat), str)
        self.assertIn("SeaBoat", repr(boat))
        self.assertIn("Name", repr(boat))
        self.assertIn("Length", repr(boat))

if __name__ == "__main__":
    unittest.main()
