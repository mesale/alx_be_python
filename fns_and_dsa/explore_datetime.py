from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    
    # Format and display
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    
    return current_date  # Returning in case the main() needs it

def calculate_future_date(days_to_add):
    # Get the current date
    current_date = datetime.now()
    
    # Calculate the future date
    future_date = current_date + timedelta(days=days_to_add)
    
    # Format and display
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    
    return future_date

def main():
    # Part 1: Display current date and time
    display_current_datetime()
    
    # Part 2: Prompt user and calculate future date
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
