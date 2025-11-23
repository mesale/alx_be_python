
# Global conversion factors (accessible within functions)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0


def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global FAHRENHEIT_TO_CELSIUS_FACTOR.

    Parameters:
        fahrenheit (float): temperature in Fahrenheit

    Returns:
        float: temperature in Celsius
    """
    # Read the global conversion factor to illustrate variable scope.
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32.0) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global CELSIUS_TO_FAHRENHEIT_FACTOR.

    Parameters:
        celsius (float): temperature in Celsius

    Returns:
        float: temperature in Fahrenheit
    """
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32.0


def _parse_temperature_input(temp_str):
    """
    Parse the temperature input string and return it as a float.

    Raises:
        ValueError: with the exact message required when parsing fails.
    """
    try:
        return float(temp_str)
    except (TypeError, ValueError):
        raise ValueError("Invalid temperature. Please enter a numeric value.")


def prompt_and_convert():
    """
    Prompt the user for a temperature and unit, validate input, perform conversion,
    and print the result.

    Raises:
        ValueError: if temperature parsing fails or if the unit is invalid.
    """
    temp_input = input("Enter the temperature to convert: ").strip()
    temp_value = _parse_temperature_input(temp_input)

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
    # Intentionally allow ValueError to propagate so tests can detect it;
    # when used interactively this will show the error and traceback.
    prompt_and_convert()