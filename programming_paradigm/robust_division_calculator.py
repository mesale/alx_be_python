import sys

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

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
