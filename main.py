from stats import *
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    print("Usage: python3 main.py <path_to_book>")
    path = sys.argv[1]
    text = get_book_text(path)
    number = num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]} ")
    print("----------- Word Count ----------")
    print(f"Found {number} total words")
    count = word_count(text)
    print("--------- Character Count -------")
    sorts = structure(count)
    for char in sorts:
        ch = char["char"]
        if ch.isalpha():
            print(f"{ch}: {char["num"]}")
    print("============= END ===============")
    


main()

    
