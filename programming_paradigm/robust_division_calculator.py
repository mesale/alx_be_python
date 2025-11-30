def safe_divide(numerator, denominator):

    try:
        # Convert inputs to float
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    
    try:
        result = num / denom
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    return f"The result of the division is {result}"
