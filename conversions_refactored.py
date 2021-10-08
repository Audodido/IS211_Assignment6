
class ConversionNotPossible(ValueError):
    pass


def convert(fromUnit, toUnit, value):
    """takes a string as unit to be converted, another string as the unit to convert to and a float as the value of fto be converted."""

    fromUnit, toUnit =  fromUnit.lower(), toUnit.lower() #make sure strings are lower case

    converted_val = 0.0
    error_message = f"Can't convert {fromUnit} to {toUnit}" ##put this in class?
    
    # important values for conversion equations
    c_k = 273.15
    c_f1, c_f2 = 9/5, 32 
    f_k1, f_k2 = 459.67, 5/9
    f_c1, f_c2 = 32, 5/9
    k_f1, k_f2 = 9/5, 459.67
    m_y = 1760.0
    m_m = 1609.344
    y_m = 1.094

    #store formulas
    the_math = {
        ('celsius', 'kelvin') : lambda a : a + c_k,
        ('celsius', 'farenheit') : lambda a : a * c_f1 + c_f2,
        ('farenheit', 'kelvin') : lambda a : (a + f_k1) * f_k2,
        ('farenheit', 'celsius') : lambda a : (a - f_c1) * f_c2,
        ('miles', 'yards') : lambda a : a * m_y,
        ('miles', 'meters') : lambda a : a * m_m,
        ('yards', 'miles') : lambda a : a / m_y,
        ('yards', 'meters') : lambda a : a / y_m,
        ('meters', 'miles') : lambda a : a / m_m,
        ('meters', 'yards') : lambda a : a * y_m,
    }

    if fromUnit == toUnit:
        converted_val = value # if args are same, return value as ==
        return converted_val

    else:
        try:
            converted_val = round(the_math[fromUnit, toUnit](value), 2)
            return converted_val
        except:
            raise ConversionNotPossible(error_message)




    
    # else:
    #     raise ConversionNotPossible(error_message)




# print(convert('miles', 'kelvin', 200))


