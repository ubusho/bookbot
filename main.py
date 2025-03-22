import sys
from stats import get_num_words
from stats import count_characters
from stats import unsorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    text = get_book_text(sys.argv[1])
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    characters = count_characters(text)
    list = unsorted_list(characters)
    def sort_on(dict):
        return dict["num"]

    list.sort(reverse=True, key=sort_on)
    for item in list:
        print(f"{item["character"]}: {item["num"]}")
    print("============= END ===============")

main()