def safe_divide(numerator, denominator):

    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Both numerator and denominator must be numeric."
    
    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    
    return f"Result: {result}"
