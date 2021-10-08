import conversions
import conversions_refactored as cr
from conversions_refactored import convert
import unittest
import random


test_int = random.random() * 100

class TestRefactoredMethod(unittest.TestCase):

    units = ['miles', 'yards', 'meters', 'farenheit', 'celsius', 'kelvin']

    # #converting celsius 
    # def test_convertCelsiusToKelvin(self):
    #     self.assertEqual(convert('celsius', 'kelvin', 30), 303.15)

    # testing miles conversion
    def test_ConvertMilesToYards(self):
        self.assertEqual(convert('miles', 'yards', 2.0), 3520.0)

    # def test_ConvertMilesToMeters(self):
    #     self.assertEqual(convert('miles', 'meters', 2.0), 3218.69)
    # # testing yards conversion
    # def test_ConvertYardsToMiles(self):
    #     self.assertEqual(convert('yards', 'miles', 100.0), .06)

    # def test_ConvertYardsToMeters(self):
    #     self.assertEqual(convert('yards', 'meters', 10.0), 9.14)
    # # testing meters conversion
    # def test_ConvertMetersToMiles(self):
    #     self.assertEqual(convert('meters', 'miles', 5000), 3.11)

    # def test_ConvertMetersToYards(self):
    #     self.assertEqual(convert('meters', 'yards', 5000), 5470.0)
    # # testing improper inputs
    # def test_MismatchedValue(self):
    #     self.assertRaises(cr.ConversionNotPossible, cr.convert, 'meters', 'kelvin', test_int)
    # #testing that converting from one unit to itself returns the same value for all units 
    # def test_fromUnit_toUnit_same(self): 
    #     for unit in self.units:
    #         self.assertEqual(convert(unit, unit, 200.0), 200.0)


#self.assertRaises(roman6.InvalidRomanNumeralError, roman6.from_roman, '')

if __name__ == "__main__":

    unittest.main()
