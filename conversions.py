
# celsius
def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    kelvin = celsius + 273.15
    
    return kelvin


def convertCelsiusToFahrenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = celsius * 9 / 5 + 32
    
    return fahrenheit


# farenheit
def convertFarenheitToKelvin(farenheit):
    """Takes in a float representing a Farenheit measurement, and returns that temperature converted into Kelvin"""
    kelvin = (farenheit + 459.67) * 5/9

    return kelvin


def convertFarenheitToCelsius(farenheit):
    """Takes in a float representing a Farenheit measurement, and returns that temperature converted into Celsius"""
    celsius = (farenheit - 32) * 5/9

    return celsius


# kelvin
def convertKelvinToFarenheit(kelvin):
    """Takes in a float representing a Farenheit measurement, and returns that temperature converted into Kelvin"""
    farenheit = kelvin * 9/5 - 459.67

    return round(farenheit, 2)


def convertKelvinToCelsius(kelvin):
    """Takes in a float representing a Farenheit measurement, and returns that temperature converted into Celsius"""
    celsius = kelvin - 273.15

    return round(celsius, 2)

