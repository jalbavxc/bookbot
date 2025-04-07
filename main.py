import sys
from stats import sort_char_count, get_num_words

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
filepath = sys.argv[1]

print("============ BOOKBOT ============")
print(sys.argv[1])
print("----------- Word Count ----------")
get_num_words(filepath)
print("--------- Character Count -------")
sort_char_count(filepath)
print("============= END ===============")