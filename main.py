def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    #print(word_count)
    stripped_text = ''.join(c for c in text if c.isalpha())
    character_count = count_characters(stripped_text)
    #print(character_count)
    chars = list_characters(character_count)
    print_report(book_path, word_count, chars)
 
    


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lower_text = text.lower()
    character_count = {}
    for c in lower_text:
        if c in character_count:
            character_count[c] += 1
        else:
            character_count[c] = 1
    return character_count

def list_characters(char_dict):
    list_of_chars = []
    for c in char_dict:
        list_of_chars.append({"char" : c, "count" : char_dict[c]})
    
    list_of_chars.sort(reverse = True, key=sort_on)
    return list_of_chars

def sort_on(d):
    return d["count"]

def print_report(book_path, word_count, chars):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for char in chars:
        print(f"The '{char['char']}' character was found {char['count']} times")
    
    print("--- End report ---")

main()