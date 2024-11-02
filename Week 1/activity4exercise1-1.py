# Queue Implementation (FIFO)

def queue_menu():
    queue = []

    while True:
        print("\nQueue Menu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. View")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter item to enqueue: ")
            queue.append(item)
            print(f"Item '{item}' added to the queue.")
        
        elif choice == "2":
            if queue:
                item = queue.pop(0)
                print(f"Item '{item}' removed from the queue.")
            else:
                print("Queue is empty. Cannot dequeue.")
        
        elif choice == "3":
            print("Current Queue:", queue if queue else "Empty Queue")
        
        elif choice == "4":
            print("Exiting Queue Program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

queue_menu()

