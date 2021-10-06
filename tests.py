import conversions
import unittest




class TestConverters(unittest.TestCase):

    # celcius
    def test_convertCelsiusToKelvin(self):
        self.assertEqual(conversions.convertCelsiusToKelvin(30), 303.15)

    def test_convertCelsiusToFahrenheit(self):
        self.assertEqual(conversions.convertCelsiusToFahrenheit(30), 86.0)

    # farenheit
    def test_convertFarenheitToKelvin(self):
        self.assertEqual(conversions.convertFarenheitToKelvin(50), 283.15)

    def test_convertFarenheitToCelsius(self):
        self.assertEqual(conversions.convertFarenheitToCelsius(50), 10)

    # kelvin
    def test_convertKelvinToFarenheit(self):
        self.assertEqual(conversions.convertKelvinToFarenheit(300), 80.33)
    
    def test_convertKelvinToCelsius(self):
        self.assertEqual(conversions.convertKelvinToCelsius(300), 26.85)

    


if __name__ == "__main__":
    unittest.main()