FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    temp_in_fahrenheit = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    return temp_in_fahrenheit

def convert_to_fahrenheit(celsius):
    temp_in_celsius = (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32
    return temp_in_celsius

temp_to_convert = float(input("Enter the temperature to convert: "))
type_of_temp = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if type_of_temp == "F":
    result = convert_to_celsius(temp_to_convert)
    print(f"{temp_to_convert}°F is {result}°C")

elif type_of_temp == "C":
    result = convert_to_fahrenheit(temp_to_convert)
    print(f"{temp_to_convert}°C is {result}°F")

else:
    print("Invalid unit. Please enter 'C' or 'F'.")