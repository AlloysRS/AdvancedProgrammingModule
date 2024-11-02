def left_triangle(rows):
    for i in range(1, rows + 1):
        print("*" * i)

def right_triangle(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i), end = "")
        print("*" * i)

def diamond(rows):

    top_rows = (rows + 1) // 2
    bottom_rows = rows // 2

    for i in range(1, top_rows + 1):
        print(" " * (top_rows - i) + "*" * (2 * i - 1))
    for i in range(bottom_rows, 0, -1):
        print(" " * (top_rows - i) + "*" * (2 * i - 1))

def display_menu():
    print("\nChoose a shape to print:")
    print("1. Left Triangle")
    print("2. Right Triangle")
    print("3. Diamond")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "4":
            print("Exiting program.")
            break

        # Menu options
        if choice in {"1", "2", "3"}:
            try:
                rows = int(input("Enter the number of rows: "))
                if rows < 1:
                    print("Enter a positive integer above zero")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                continue

            # Choices
            if choice == "1":
                left_triangle(rows)
            elif choice == "2":
                right_triangle(rows)
            elif choice == "3":
                diamond(rows)
        else:
            print("Invalid choice. Please choose a valid option. (1-4)")

if __name__ == "__main__":
    main()