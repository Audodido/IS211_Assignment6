
class ConversionNotPossible(ValueError):
    pass

def convert(fromUnit, toUnit, value):
    """takes a string as unit to be converted, another string as the unit to convert to and a float as the value of fto be converted."""

    fromUnit, toUnit =  fromUnit.lower(), toUnit.lower() #make sure strings are lower case

    converted_val = 0.0
    error_message = f"Can't convert {fromUnit} to {toUnit}" ##put this in class?
    m_y = 1760.0
    m_m = 1609.344
    y_m = 1.094

    equations = {
        ('miles', 'yards') : lambda a : a * m_y
    }

    if fromUnit == toUnit:
        converted_val = value

    else:
        try:
            converted_val = equations[fromUnit, toUnit](value)
            return converted_val
        except:
            raise ConversionNotPossible(error_message)

print(convert('miles', 'yards', 2.0))