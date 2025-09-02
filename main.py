from stats import get_num_words, get_letter_count
import sys

def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    num_words = get_num_words(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    letter_count = get_letter_count(book)
    print('--------- Character Count -------')
    for i in range(0, len(letter_count)):
        print(f"{letter_count[i]["char"]}: {letter_count[i]["num"]}")
    #print(letter_count)
main()