import streamlit as st
st.set_page_config(page_title="Unit Converter")

conversions = {
    "Length": {
        "Meter": 1,
        "Kilometer": 0.001,
        "Centimeter": 100,
        "Millimeter": 1000,
        "Mile": 0.000621371,
        "Yard": 1.09361,
        "Foot": 3.28084,
        "Inch": 39.3701,
        "Micrometer": 1e+6,
        "Nanometer": 1e+9,
        "Nauticalmile": 0.000539957,
    },
    "Temperature": {
        "Celsius": "c",
        "Fahrenheit": "f",
        "Kelvin": "k",
    },
    "Mass": {
        "Tonne": 1,
        "Kilogram": 1000,
        "Gram": 1e+6,
        "Milligram": 1e+9,
        "Microgram": 1e+12,
        "Imperial ton": 0.984207,
        "US ton": 1.10231,
        "Stone": 157.473,
        "Pound": 2204.62,
        "Ounce": 35274,
    },
    "Speed": {
        "Meters per second": 1,
        "Kilometers per hour": 3.6,
        "Miles per hour": 2.23694,
        "Feet per second": 3.28084,
        "Knots": 1.94384,
    },
    "Volume": {
        "Cubic meter": 1,
        "Liter": 1000,
        "Milliliter": 1e+6,
        "Cubic centimeter": 1e+6,
        "Cubic inch": 61023.7,
        "Cubic foot": 35.3147,
        "US gallon": 264.172,
        "US pint": 2113.38,
    },
    "Time": {
        "Second": 1,
        "Millisecond": 1000,
        "Microsecond": 1e+6,
        "Minute": 1/60,
        "Hour": 1/3600,
        "Day": 1/86400,
    },
    "Pressure": {
        "Pascal": 1,
        "Bar": 1e-5,
        "PSI": 0.000145038,
        "Atmosphere": 9.86923e-6,
        "Torr": 0.00750062,
    },
    "Energy": {
        "Joule": 1,
        "Kilojoule": 0.001,
        "Calorie": 0.239006,
        "Kilocalorie": 0.000239006,
        "Watt hour": 0.000277778,
        "Kilowatt hour": 2.7778e-7,
    },
    "Area": {
        "Square meter": 1,
        "Square kilometer": 1e-6,
        "Square centimeter": 1e+4,
        "Square millimeter": 1e+6,
        "Square mile": 3.861e-7,
        "Square yard": 1.19599,
        "Square foot": 10.7639,
        "Square inch": 1550,
        "Hectare": 0.0001,
        "Acre": 0.000247105,
    }
}

def to_celsius(value, from_unit):
    if from_unit == "Celsius":
        return value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5 / 9
    elif from_unit == "Kelvin":
        return value - 273.15

def from_celsius(value, to_unit):
    if to_unit == "Celsius":
        return value
    elif to_unit == "Fahrenheit":
        return value * 9 / 5 + 32
    elif to_unit == "Kelvin":
        return value + 273.15

def convert_units(value, from_unit, to_unit, unit_type):
    formula = ""
    
    if unit_type == "Temperature":
        celsius_value = to_celsius(value, from_unit)
        result = from_celsius(celsius_value, to_unit)
        formula = f"{value} {from_unit} → {round(celsius_value, 2)} °C → {round(result, 2)} {to_unit}"
    else:
        base = value / conversions[unit_type][from_unit]  
        result = base * conversions[unit_type][to_unit]   
        formula = f"{value} × (1 / {conversions[unit_type][from_unit]}) × {conversions[unit_type][to_unit]} = {round(result, 4)}"

    return round(result, 4), formula

st.title(" Unit Converter")
value = st.number_input(" Enter value")
unit_type = st.selectbox(" Conversion Type", list(conversions.keys()))
unit_list = list(conversions[unit_type].keys())
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From", unit_list, key="from")
with col2:
    to_unit = st.selectbox("To", unit_list, key="to")

if value:
    result, formula = convert_units(value, from_unit, to_unit, unit_type)
    st.markdown("###  Converted Result")
    st.success(f"{value} {from_unit} = {result} {to_unit}")
    st.markdown("###  Formula Used")
    st.code(formula)
