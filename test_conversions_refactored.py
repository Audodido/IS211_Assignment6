import conversions
from conversions_refactored import convert
import unittest





class TestRefactoredMethod(unittest.TestCase):

    def test_ConvertMilesToYards(self):
        self.assertEqual(convert('miles', 'yards', 2.0), 3520.0)

    def test_ConvertMilesToMeters(self):
        self.assertEqual(convert('miles', 'meters', 2.0), 3218.69)

    def test_ConvertYardsToMiles(self):
        self.assertEqual(convert('yards', 'miles', 100.0), .06)



if __name__ == "__main__":

    unittest.main()
