def feet_to_metres():
    while True:
        try:
            feet = int(input("Enter feet: "))
            if feet < 0:
                print("Feet cannot be negative. Please enter a valid value.")
                continue
            inches = int(input("Enter inches: "))
            if inches < 0:
                print("Inches cannot be negative. Please enter a valid value.")
                continue
            inches += feet * 12
            metres = inches * 0.0254
            return metres
        except ValueError:
            print("Invalid input. Please enter an integer.")

def pounds_to_kilograms():
    while True:
        try:
            lbs = float(input("Enter pounds (lbs): "))
            if lbs < 0:
                print("Pounds cannot be negative. Please enter a valid value.")
                continue
            kgs = lbs / 2.205
            return kgs
        except ValueError:
            print("Invalid input. Please enter a number.")

def kelvin_to_celcius():
    while True:
        try:
            kelvin = float(input("Enter temperature (Kelvin): "))
            if kelvin < 0:
                print("Kelvin cannot be negative. Please enter a valid value.")
                continue
            celcius = kelvin - 273.15
            return celcius
        except ValueError:
            print("Invalid input. Please enter a number.")

def hours_minutes_to_seconds():
    while True:
        try:
            hours = int(input("Enter hours: "))
            if hours < 0 or hours > 24:
                print("Hours must be between 0 and 24. Please enter a valid value.")
                continue
            minutes = int(input("Enter minutes: "))
            if minutes < 0 or minutes >= 60:
                print("Minutes must be between 0 and 59. Please enter a valid value.")
                continue
            seconds = ((hours * 60) + minutes) * 60
            return seconds
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    print("Not intended for standalone use, please import")

if __name__ == "__main__":
    main()