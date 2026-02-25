import unittest
from Lab4task1 import Letter, Punctuation, Word, Sentence, Text, SeaBoat

class TestTextStructure(unittest.TestCase):
    def test_letter_creation(self):
        l = Letter('A')
        self.assertEqual(str(l), 'A')

    def test_word_creation(self):
        w = Word("Boat")
        self.assertEqual(str(w), "Boat")
        self.assertEqual(len(w.letters), 4)
        self.assertTrue(all(isinstance(l, Letter) for l in w.letters))

    def test_sentence_creation_simple(self):
        s = Sentence("Hello, world!")
        self.assertEqual(str(s), "Hello, world!")
        self.assertTrue(any(isinstance(c, Punctuation) for c in s.components))
        self.assertTrue(any(isinstance(c, Word) for c in s.components))

    def test_sentence_creation_multiple_spaces(self):
        s = Sentence("  Hello    world!   ")
        self.assertEqual(str(s), "Hello world!")

    def test_text_creation(self):
        t = Text("Hello world! This is a test.")
        self.assertEqual(len(t.sentences), 2)
        self.assertEqual(str(t), "Hello world! This is a test.")

class TestSeaBoat(unittest.TestCase):
    def setUp(self):
        self.boats = [
            SeaBoat("Odessa", 30.5, 45, 120, 2010),
            SeaBoat("Neptune", 25.0, 60, 80, 2015),
            SeaBoat("BlackSea", 40.2, 50, 200, 2008),
            SeaBoat("Poseidon", 35.0, 55, 150, 2012),
            SeaBoat("Atlantis", 28.7, 48, 100, 2018)
        ]

    def test_creation(self):
        boat = SeaBoat("Titanic", 50.0, 40, 300, 1912)
        self.assertEqual(str(boat.name), "Titanic")
        self.assertEqual(boat.length, 50.0)
        self.assertEqual(boat.speed, 40)
        self.assertEqual(boat.capacity, 300)
        self.assertEqual(boat.year, 1912)

    def test_name_text_structure(self):
        boat = self.boats[3]  # Poseidon
        name_text = boat.name
        self.assertIsInstance(name_text, Text)
        self.assertTrue(len(name_text.sentences) >= 1)
        first_sentence = name_text.sentences[0]
        self.assertTrue(all(isinstance(c, Word) or isinstance(c, Punctuation)
                            for c in first_sentence.components))
        for comp in first_sentence.components:
            if isinstance(comp, Word):
                self.assertTrue(all(isinstance(l, Letter) for l in comp.letters))

    def test_equality(self):
        boat1 = SeaBoat("Poseidon", 35.0, 55, 150, 2012)
        boat2 = SeaBoat("Poseidon", 35.0, 55, 150, 2012)
        boat3 = SeaBoat("Neptune", 25.0, 60, 80, 2015)
        self.assertTrue(boat1 == boat2)
        self.assertFalse(boat1 == boat3)

    def test_sort_by_length(self):
        sorted_boats = sorted(self.boats, key=lambda b: (b.length, -b.speed))
        lengths = [b.length for b in sorted_boats]
        self.assertEqual(lengths, [25.0, 28.7, 30.5, 35.0, 40.2])

    def test_sort_by_speed_desc(self):
        sorted_boats = sorted(self.boats, key=lambda b: (-b.speed, b.length))
        speeds = [b.speed for b in sorted_boats]
        self.assertEqual(speeds, [60, 55, 50, 48, 45])

    def test_search_boat(self):
        target = SeaBoat("Poseidon", 35.0, 55, 150, 2012)
        found = any(b == target for b in self.boats)
        self.assertTrue(found)
        not_found = any(b == SeaBoat("NonExistent", 0, 0, 0, 0) for b in self.boats)
        self.assertFalse(not_found)

if __name__ == "__main__":
    unittest.main()
