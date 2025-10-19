
from stats import count_words, count_characters
    
word_count = count_words("/home/toby/projects/bookbot/books/frankenstein.txt")
character_count = count_characters("/home/toby/projects/bookbot/books/frankenstein.txt")

print("Found " + str(word_count) + " total words")
print(character_count)