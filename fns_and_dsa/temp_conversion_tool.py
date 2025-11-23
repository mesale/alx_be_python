# Global conversion factors - Demonstrates GLOBAL scope (G in LEGB)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    
    Demonstrates how functions access global variables.
    The global conversion factor is accessed from the GLOBAL namespace.
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit
    
    Returns:
        float: Temperature in Celsius
    """
    # Accessing the global variable FAHRENHEIT_TO_CELSIUS_FACTOR
    # Python searches: Local (L) -> Enclosing (E) -> Global (G) -> Built-in (B)
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius


def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Demonstrates how functions access global variables.
    The global conversion factor is accessed from the GLOBAL namespace.
    
    Args:
        celsius (float): Temperature in Celsius
    
    Returns:
        float: Temperature in Fahrenheit
    """
    # Accessing the global variable CELSIUS_TO_FAHRENHEIT_FACTOR
    # Python searches: Local (L) -> Enclosing (E) -> Global (G) -> Built-in (B)
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit


def get_temperature_input():
    """
    Prompts user for temperature input with validation.
    
    Demonstrates LOCAL scope - variables created here are only 
    accessible within this function.
    
    Returns:
        float: Valid temperature value
        
    Raises:
        ValueError: If input cannot be converted to float
    """
    try:
        # temp_input is a LOCAL variable - only exists in this function's namespace
        temp_input = input("Enter the temperature to convert: ")
        
        # Attempting to convert to float - raises ValueError if invalid
        temperature = float(temp_input)
        return temperature
    except ValueError:
        # Raise the specific error message as per requirements
        raise ValueError("Invalid temperature. Please enter a numeric value.")


def get_unit_input():
    """
    Prompts user for temperature unit (Celsius or Fahrenheit).
    
    Demonstrates LOCAL scope - variables created here are only 
    accessible within this function's namespace.
    
    Returns:
        str: 'C' for Celsius or 'F' for Fahrenheit
        
    Raises:
        ValueError: If unit is not 'C' or 'F'
    """
    # unit is a LOCAL variable - only exists in this function's namespace
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    # Validate unit input
    if unit not in ['C', 'F']:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    return unit


def main():
    """
    Main function to handle user interaction for temperature conversion.
    
    Demonstrates how different scopes work together:
    - LOCAL variables: temperature, unit, converted_temp (created in this function)
    - GLOBAL variables: FAHRENHEIT_TO_CELSIUS_FACTOR, CELSIUS_TO_FAHRENHEIT_FACTOR
    - ENCLOSING scope: (not used in this example, but relevant for nested functions)
    - BUILT-IN scope: print(), input() functions
    """
    try:
        # These variables have LOCAL scope within main()
        temperature = get_temperature_input()
        unit = get_unit_input()
        
        # Convert temperature based on unit
        # The conversion functions access GLOBAL variables
        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:  # unit == 'C'
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
    
    except ValueError as e:
        print(str(e))


if __name__ == "__main__":
    main()