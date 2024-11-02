def main():
    chosen_number = int(input("Choose a number for your times table: "))
    print(f"The even timetable for {chosen_number} is:")
    multiplier = 2
    while multiplier <= 20:
        multiplied_sum = chosen_number * multiplier
        print(f"{multiplier} times {chosen_number} is {multiplied_sum}")
        multiplier += 2

if __name__ == "__main__":
    main()