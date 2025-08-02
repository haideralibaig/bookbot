from stats import number_of_words
from stats import character_count
from stats import sorted_list
import sys

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])
        book_words = number_of_words(text)
        print("============ BOOKBOT ============")
        print("Analyzing book found at",sys.argv[1] + "...")
        print("----------- Word Count ----------")
        print("Found",book_words,"total words")
        print("--------- Character Count -------")
        #print(character_count(text))
        final_list = sorted_list(character_count(text))

        for dictionary in final_list:
        #for value in dictionary.values():
            if dictionary["char"].isalpha():
                print(dictionary["char"] + ":",dictionary["num"])

        print("============= END ===============")

def get_book_text (book_id):
    with open(book_id, 'r') as f:
        content = f.read()
    return content

main()
