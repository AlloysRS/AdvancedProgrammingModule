def get_valid_input(prompt, min_val, max_val):
    # Loop to get valid input and reprompt the user if input is not in allowed range (passed to function by args) or int
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def generate_calendar(days_in_month, start_day):
    # Print calendar headers, adjust start_day for 0 based indexing, and add blank spaces for each day before start_day
    print("\nMon Tue Wed Thu Fri Sat Sun")
    start_day -= 1
    calendar = ["    "] * start_day  # Four spaces for each day before the 1st

    # Add each day of the month to the calendar list
    for day in range(1, days_in_month + 1):
        calendar.append(f"{day:>3} ")  # Format each day, right aligned with 3 characters, plus a space after, so it matches in line with day

    # Add four spaces for each day at the end to complete the last week until calendar length modulo 7 = 0
    while len(calendar) % 7 != 0:
        calendar.append("    ")

    # Print the calendar in week view (7 day increments), ie first row calendar[0:7] then calendar[7:14]
    for weeks in range(0, len(calendar), 7):
        week = calendar[weeks:weeks + 7]
        for day in week:
            print(day, end="")
        print()

def main():
    # User input for number of days and starting day
    days_in_month = get_valid_input("Enter the number of days in the month (28-31): ", 28, 31)
    start_day = get_valid_input("Enter the starting day of the week (1=Monday, 7=Sunday): ", 1, 7)
    
    # Generate and print calendar
    generate_calendar(days_in_month, start_day)

if __name__ == "__main__":
    main()
