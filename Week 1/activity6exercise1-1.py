from activity6exercise1 import feet_to_metres, pounds_to_kilograms, kelvin_to_celcius, hours_minutes_to_seconds

def main():
    while True:
        print("\nChoose a conversion:")
        print("1. Convert length (feet & inches to metres)")
        print("2. Convert weight (pounds to kilograms)")
        print("3. Convert temperature (Kelvin to Celsius)")
        print("4. Convert time (hours & minutes to seconds)")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            metres = feet_to_metres()
            print(f"{metres:.2f} metres")
        elif choice == '2':
            kgs = pounds_to_kilograms()
            print(f"{kgs:.2f} kgs")
        elif choice == '3':
            celcius = kelvin_to_celcius()
            print(f"{celcius:.2f}°C")
        elif choice == '4':
            seconds = hours_minutes_to_seconds()
            print(f"{seconds} seconds")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()