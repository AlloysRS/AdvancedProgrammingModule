# Stack Implementation (LIFO)

def stack_menu():
    stack = []

    while True:
        print("\nStack Menu:")
        print("1. Push")
        print("2. Pop")
        print("3. View")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter item to push: ")
            stack.append(item)
            print(f"Item '{item}' pushed to the stack.")
        
        elif choice == "2":
            if stack:
                item = stack.pop()
                print(f"Item '{item}' popped from the stack.")
            else:
                print("Stack is empty. Cannot pop.")
        
        elif choice == "3":
            print("Current Stack:", stack if stack else "Empty Stack")
        
        elif choice == "4":
            print("Exiting Stack Program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

stack_menu()

