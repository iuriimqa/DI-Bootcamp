from anagram_checker import AnagramChecker

def validate_word(word):
    if len(word.split()) > 1:
        print("Error: Only a single word is allowed")
        return False
    if not word.isalpha():
        print("Error: Only alphabetic characters are allowed")
        return False
    return True

def print_anagrams(word, anagrams):
    print(f"\nYOUR WORD: \"{word}\"")
    if anagram_checker.is_valid_word(word):
        print("This is a valid English word.")
    else:
        print("This is NOT a valid English word.")
    if len(anagrams) == 0:
        print("No anagrams found.")
    else:
        print("Anagrams for your word:", ", ".join(anagrams))

anagram_checker = AnagramChecker()

while True:
    choice = input("Enter a word (or 'exit' to quit): ").strip().lower()
    if choice == 'exit':
        break
    if not validate_word(choice):
        continue
    anagrams = anagram_checker.get_anagrams(choice)
    print_anagrams(choice, anagrams)
