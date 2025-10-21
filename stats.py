
def count_words(file_path):
    with open(file_path) as f:# do something with f (the file) here
        file_contents = f.read()# f is a file object
    
    words = file_contents.split()
    return len(words)

def count_characters(file_path):
    with open(file_path) as f:# do something with f (the file) here
        file_contents = f.read()# f is a file object
    character_counts = {}
    for char in file_contents.lower():
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts

def sorted_character_count(file_path):
    character_counts = count_characters(file_path)
    sorted_by_freq = sorted(character_counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_by_freq
