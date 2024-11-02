def anagram_check(word1, word2):
    # Initialise empty letter lists
    word1_letters = []
    word2_letters = []

    # Add letters in each word to relevant list 
    for letter in word1:
        word1_letters.append(letter)
    for letter in word2:
        word2_letters.append(letter)

    # Sort both lists
    word1_letters.sort()
    word2_letters.sort()

    # Return boolean on whether both lists contents match
    return word1_letters == word2_letters

def main():
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")
    
    anagram = anagram_check(word1, word2)
    if anagram:
        print("These are Anagrams.")
    else:
        print("These are not Anagrams.")

if __name__ == "__main__":
    main()
