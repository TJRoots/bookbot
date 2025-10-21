
from stats import count_words, count_characters, sorted_character_count
    
word_count = count_words("books/frankenstein.txt")
character_count = count_characters("books/frankenstein.txt")

print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
print("Found " + str(word_count) + " total words")
#print(character_count)
print("--------- Character Count -------")
for char, count in sorted_character_count("books/frankenstein.txt"):
    if char.isalpha():
        print(char + ": " + str(count))
print("============= END ===============")