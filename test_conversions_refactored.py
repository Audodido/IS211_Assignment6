import conversions
from conversions_refactored import convert
import unittest


class TestRefactoredMethod(unittest.TestCase):

    # testing miles conversion
    def test_ConvertMilesToYards(self):
        self.assertEqual(convert('miles', 'yards', 2.0), 3520.0)

    def test_ConvertMilesToMeters(self):
        self.assertEqual(convert('miles', 'meters', 2.0), 3218.69)
    # testing yards conversion
    def test_ConvertYardsToMiles(self):
        self.assertEqual(convert('yards', 'miles', 100.0), .06)

    def test_ConvertYardsToMeters(self):
        self.assertEqual(convert('yards', 'meters', 10.0), 9.14)
    # testing meters conversion
    def test_ConvertMetersToMiles(self):
        self.assertEqual(convert('meters', 'miles', 5000), 3.11)

    def test_ConvertMetersToYards(self):
        self.assertEqual(convert('meters', 'yards', 5000), 5470.0)




if __name__ == "__main__":

    unittest.main()
