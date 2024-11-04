def problem_1():
    try:
        num1 = int(input("Enter a number: " ))
        num2 = int(input("Enter another number: " ))

        if num1 > num2:
            if num1%num2 == 0:
                print(num1, " is a multiple of ", num2)
        else:
            if num2%num1 == 0:
                print(num2, " is a multiple of ", num1)
    except ZeroDivisionError as e:
        print("Error occured:", e)

def problem_2():
    try:
        names = input("List of names: ") 
        nameList = names.split()
        print(nameList[1000])
    except IndexError as e:
        print("Error occured:", e)

def problem_3():
    try:
        randomList = ['67', 53, '3O',72, '10']

        for i in randomList:
            print(int(i) * 10)
    except ValueError as e:
        print("Error occured:", e)

def problem_4():
    try:
        fileName = input("Enter File: ")
        print(open(fileName).read())
    except FileNotFoundError as e:
        print("Error occured", e)

def main():
    while True:
        print("\nChoose an option:")
        print("1. Problem 1: Check if a number is a multiple of another")
        print("2. Problem 2: Access an out-of-range index")
        print("3. Problem 3: Convert list items to integers")
        print("4. Problem 4: Open a file")
        print("0. Exit")
        
        choice = input("Enter your choice (0-4): ")

        if choice == '1':
            problem_1()
        elif choice == '2':
            problem_2()
        elif choice == '3':
            problem_3()
        elif choice == '4':
            problem_4()
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 4.")

if __name__ == "__main__":
    main()