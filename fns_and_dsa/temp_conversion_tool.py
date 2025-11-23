
# Global conversion factors (accessible inside functions)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0

def convert_to_celsius(fahrenheit):

    # We only read the global variable here, no 'global' statement required.
    return (fahrenheit - 32.0) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):

    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32.0

def _prompt_and_convert():

    temp_input = input("Enter the temperature to convert: ").strip()
    # Validate numeric temperature
    try:
        temp_value = float(temp_input)
    except ValueError:
        # Exact message required by the task
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()

    if unit_input in ("f", "fahrenheit"):
        converted = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is {converted}°C")
    elif unit_input in ("c", "celsius"):
        converted = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {converted}°F")
    else:
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    try:
        _prompt_and_convert()
    except ValueError as e:
        # Surface the error message to the user
        print(e)