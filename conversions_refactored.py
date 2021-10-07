
class ConversionNotPossible(ValueError):
    pass


def convert(fromUnit, toUnit, value):
    """takes a string as unit to be converted, another string as the unit to convert to and a float as the value of fto be converted."""

    fromUnit, toUnit =  fromUnit.lower(), toUnit.lower() #make sure strings are lower case

    converted_val = 0.0
    error_message = f"Can't convert {fromUnit} to {toUnit}" ##put this in class?
    miles_yards = 1760.0
    miles_meters = 1609.344
    yards_meters = 1.094

    if fromUnit == toUnit:
        converted_val = value

    # converting miles to meters/yards
    elif fromUnit == 'miles':
        if toUnit == 'yards':
            converted_val = value * miles_yards
        elif toUnit == 'meters':
            converted_val = value * miles_meters
        else:
            raise ConversionNotPossible(error_message)

    # converting yards to miles/meters
    elif fromUnit == 'yards':
        if toUnit == 'miles':
            converted_val = value / miles_yards
        elif toUnit == 'meters':
            converted_val = value / yards_meters
        else:
            raise ConversionNotPossible(error_message)

    # # converting meters to miles/yards
    elif fromUnit == 'meters':
        if toUnit == 'miles':
            converted_val = value / miles_meters
        elif toUnit == 'yards':
            converted_val = value * yards_meters
        else:
            raise ConversionNotPossible(error_message)
    
    else:
        raise ConversionNotPossible(error_message)


    converted_val = round(converted_val, 2)

    return converted_val


# print(convert('miles', 'kelvin', 200))

