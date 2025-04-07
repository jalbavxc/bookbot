def get_book_text(file):
    with open(file) as f:
        file_content=f.read()
    return file_content

def get_num_words(file):
    num_words=len(get_book_text(file).split())
    print(f"Found {num_words} total words")

def get_all_characters_count(file):
    char_count={}
    for char in get_book_text(file).lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(item):
    return item[1]

def sort_char_count(file):
    char_count=get_all_characters_count(file)
    filter_items=[item for item in char_count.items() if item[0].isalpha()]
    sorted_chars=sorted(filter_items,reverse=True,key=sort_on)
    for char,count in sorted_chars:
        print(f"{char}: {count}")
    return sorted_chars
    