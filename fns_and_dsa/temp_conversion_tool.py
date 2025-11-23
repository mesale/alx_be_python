# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    
    Args:
        fahrenheit: Temperature in Fahrenheit
    
    Returns:
        Temperature in Celsius
    """
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius


def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Args:
        celsius: Temperature in Celsius
    
    Returns:
        Temperature in Fahrenheit
    """
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit


def main():
    """
    Main function to handle user interaction for temperature conversion.
    """
    try:
        # Get temperature input from user
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)
        
        # Get unit input from user
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        # Validate unit input
        if unit not in ['C', 'F']:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        
        # Convert temperature based on unit
        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:  # unit == 'C'
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
    
    except ValueError as e:
        if "could not convert" in str(e):
            print("Invalid temperature. Please enter a numeric value.")
        else:
            print(str(e))


if __name__ == "__main__":
    main()