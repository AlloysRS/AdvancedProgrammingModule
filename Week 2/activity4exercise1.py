import re

def count_occurrences(word, content):
    return len(re.findall(rf'\b{word}\b', content, flags=re.IGNORECASE))

def count_words_with_pp(content):
    return len(re.findall(r'\b\w*pp\w*\b', content, flags=re.IGNORECASE))

def replace_exclamation(content):
    return re.sub(r'!', '#', content)

def find_t_words(content):
    return re.findall(r'\bt\w*[^e]\b', content, flags=re.IGNORECASE)

def main_menu():
    print("\n--- Menu ---")
    print("1. Count occurrences of the word 'shrieked'")
    print("2. Count occurrences of the word 'bleak'")
    print("3. Count words containing 'pp'")
    print("4. Replace all '!' with '#' and save to a new file")
    print("5. Find words starting with 't' and not ending with 'e'")
    print("0. Exit")

def main():
    file_path = 'The_Raven.txt'
    output_file_path = 'The_Raven_Modified.txt'

    try:
        with open(file_path, 'r', encoding='UTF-8') as file:
            content = file.read()

        while True:
            main_menu()
            choice = input("Select an option (1-6): ")

            if choice == '1':
                shrieked_count = count_occurrences("shrieked", content)
                print(f"Occurrences of 'shrieked': {shrieked_count}")

            elif choice == '2':
                bleak_count = count_occurrences("bleak", content)
                print(f"Occurrences of 'bleak': {bleak_count}")

            elif choice == '3':
                pp_count = count_words_with_pp(content)
                print(f"Occurrences of words containing 'pp': {pp_count}")

            elif choice == '4':
                modified_content = replace_exclamation(content)
                with open(output_file_path, 'w', encoding='UTF-8') as file:
                    file.write(modified_content)
                print(f"Modified file saved as '{output_file_path}' with exclamation marks replaced by hash symbols.")

            elif choice == '5':
                t_words = find_t_words(content)
                print(f"Words that start with 't' but do not end with 'e': {t_words}")
                print(f"Total 't' words count: {len(t_words)}")

            elif choice == '0':
                print("Exiting program.")
                break

            else:
                print("Invalid option. Please select again.")

    except FileNotFoundError as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    main()
