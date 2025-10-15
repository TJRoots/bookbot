def get_book_text(path_to_file):
    with open(path_to_file) as f:# do something with f (the file) here
        file_contents = f.read()# f is a file object
        return file_contents
    
def main():
    print(get_book_text("/home/toby/projects/bookbot/books/frankenstein.txt"))

main()