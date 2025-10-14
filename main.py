#oct 3 inital code
#oct 6 split into seperate files
#oct 12 update 

import sys
from stats import total_words, each_char, sorted_list 

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = (sys.argv[1])
    text = get_book_text(path)
    num_words = total_words(text)
    print('=' * 12 + "BOOKBOT" + '=' *12 )
    print(f"Analyzing book found at" +path + "...")
    print('-' * 11 + "Word Count" + '-' * 11)
    print(f"Found {num_words} total words")
    print('-' * 11 + "Character Count" + '-' * 11)

    #total_words(text)
    print_char = each_char(text)
    print_sorted = sorted_list(print_char)
    print('=' * 12 + "END" + '=' * 12)

def get_book_text(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
	main()
