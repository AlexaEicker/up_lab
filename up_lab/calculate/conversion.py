#converts most common units

#temperature

def K_to_C(K):
    """Kelvin to Celsius.
    Arg:
    K: float or array_like
        Temperature in Kelvin
    Return:
    C: float or array_like
    """
    return K-273.15

def C_to_K(C):
    """Celsius to Kelvin.
    Arg:
    C: float or array_like.
        Temperature in Celsius
    Return:
    K: float or array_like
    """
    return C+273.15

def F_to_K(F):
    """Fahrenheit to Kelvin.
    Arg:
    F: float or array_like
    Return:
    K: float or array_like
    """
    return (F-32)*5/9+273.15


#length

def in_to_m(inch):
    """Inch to meter.
    Arg:
    inch: float or array_like
    Return:
    m: float or array_like
    """
    return inch*0.0254

def m_to_in(meter):
    """Meter to inch.
    Arg:
    meter: float or array_like
    Return:
    inch: float or array_like
    """
    return meter/0.0254

def ft_to_m(ft):
    """Feet to meter.
    Arg:
    ft: float or array_like
    Return:
    m: float or array_like
    """
    return ft*0.3048

def m_to_ft(meter):
    """Meter to feet
    Arg:
    meter: float or array_like
    Return:
    feet: float or array_like
    """
    return meter/0.3048

def mi_to_m(mi):
    """Mile to meter.
    Arg:
    mi: float or array_like
    Return:
    m: float or array_like
    """
    return mi*1609.344

def m_to_mi(meter):
    """Meter to mile.
    Arg:
    meter: float or array_like
    Return:
    mile: float or array_like
    """
    return meter/1609.344

#mass

def oz_to_kg(oz):
    """Ounce to kilogram.
    Arg:
    oz: float or array_like
    Return: 
    kg: float or array_like
    ================
    Caution:
    International avoirdupois ounce
    """
    return oz*28.349523125*10**(-3)

def kg_to_oz(kg):
    """Kilogram to ounce.
    Arg:
    kg: float or array_like
    Return: 
    oz: float or array_like
    ================
    Caution:
    International avoirdupois ounce"""
    return (kg/28.349523125)*10**(3)

def lbs_to_kg(lbs):
    """Pound to kilogram.
    Arg:
    lbs: float or array_like
    Return:
    kg: float or array_like
    =============
    Caution:
    Avoirdupois weight, not troy or apothecaries weight
    """
    return lbs*0.45359237 

def kg_to_lbs(kg):
    """Kilogram to pound.
    Arg:
    kg: float or array_like
    Return:
    lbs: float or array_like
    ==============
    Caution:
    Avoirdupois weight, not troy or apothecaries weight
    """
    return kg/0.45359237

#time

def min_to_sec(min):
    """Converts minutes to seconds.
    Arg:
    min: float or array_like
    Return:
    sec: float or array_like
    """
    return min*60

def sec_to_min(sec):
    """Converts seconds to minutes.
    Arg:
    sec: float or array_like
    Return:
    min: float or array_like
    """
    return sec/60

def h_to_min(h):
    """Converts hours to minutes.
    Arg:
    h: float or array_like
    Return:
    min: float or array_like"""
    return h*60

def min_to_h(min):
    """Converts minutes to hours.
    Arg: 
    min: float or array_like
    Return:
    h: float or array_like
    """
    return min/60

def sec_to_h(sec):
    """Converts seconds to hours
    Arg:
    sec: float or array_like
    Return:
    h: float or array_like
    """
    return sec*3600

def h_to_sec(h):
    """Converts hours to seconds
    Arg:
    h: float or array_like
    Return:
    sec: float or array_like
    """
    return h/3600
