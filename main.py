
def print_book_report(book_path):
    """Prints a report of a book/text file to console"""
    with open(book_path) as f:
        print(f"--- Begin report of {book_path} ---")
        contents = f.read()
        contents = contents.lower()
        words = contents.split()
        print(f"{len(words)} words found in the document")
        letters = {}
        for letter in contents:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        letter_list = [ (letter, letters[letter]) for letter in letters ]
        letter_list.sort(key=lambda x: x[1], reverse=True)
        for letter in letter_list:
            if letter[0].isalpha():
                print(f"The '{letter[0]}' character was found {letter[1]} times")
        print(f"--- End report ---")

if __name__ == "__main__":
    book_path = "books/frankenstein.txt"
    print_book_report(book_path)