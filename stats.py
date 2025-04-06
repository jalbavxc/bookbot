def get_book_text(pathfile):
    with open(pathfile) as f:
        file_content=f.read()
    return file_content

def get_num_words():
    file = "books/frankenstein.txt"
    num_words=len(get_book_text(filepath).split())
    print(f"{num_words} words found in the document")

def get_all_characters_count():
    filepath = "books/frankenstein.txt"
    char_count={}
    for char in get_book_text(filepath).lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    print(char_count)