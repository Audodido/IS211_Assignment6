
class TypeError(TypeError):
    pass


def convert(fromUnit, toUnit, value):
    """takes a string as unit to be converted, another string as the unit to convert to and a float as the value of fto be converted."""

    fromUnit, toUnit = fromUnit.lower(), toUnit.lower() #make sure strings are lower case

    miles_yards = 1760.0

    # # converting miles to meters/yards
    # if fromUnit == 'miles':
    #     if toUnit == 'yards':
    #         converted_val = round(value * 1760.0, 2)
    #     elif toUnit == 'meters':
    #         converted_val = round(value * 1609.344, 2)
    #     # else:
    #     #     raise TypeError(f"can't convert {fromUnit} to {toUnit}")


    # # converting yards to miles/meters
    # elif fromUnit == 'yards':
    #     if toUnit == 'miles':
    #         converted_val = round(value / 1760.0, 2)
    #     elif toUnit == 'meters':
    #         converted_val = round(value / 1.094, 2)


    # # # converting meters to miles/yards
    # elif fromUnit == 'meters':
    #     if toUnit == 'miles':
    #         converted_val = round(value / 1609.344, 2)
    #     elif toUnit == 'yards':
    #         converted_val = round(value * 1.094, 2)
    
    # else:
    #     converted_val = 0 #change to error

    return float(converted_val)


