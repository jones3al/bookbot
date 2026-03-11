def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_each_character(text):
    char_count = {}
    lower_text = text.lower()  # Convert to lowercase for case-insensitive counting
    for char in lower_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sorted_character_counts(char_count):
    #filter to only alphabetical characters, then sort in descending order
    alphabetical_only = {k: v for k, v in char_count.items() if k.isalpha()}
    return dict(sorted(alphabetical_only.items(), key=lambda item: item[1], reverse=True))
    
    
     