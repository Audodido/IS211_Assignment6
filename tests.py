import conversions
import unittest



# def convertCelsiusToKelvin(temp):
#     return 0.0


class TestConverters(unittest.TestCase):

    def test_con_cel_kel(self):
        self.assertEquals(conversions.convertCelsiusToKelvin(30), 303.15 )


if __name__ == "__main__":

    unittest.main()