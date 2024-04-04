def main():
    book_path= "books/frankeistein.txt"

    text = get_book(book_path)
    word_count = get_word_count(text)
    letter_count_dict = get_letter_count_dict(text)
    sorted_letter_list = letter_dict_to_list(letter_count_dict)

#Prints out a book report
    print(f"--- Book report for {book_path} ---")
    print()
    print(f"There are {word_count} words found in the book")
    print()
    for item in sorted_letter_list:
        print(f"The letter '{item['char']}' appears {item['num']} times")
    print()
    print("--- End of Book Report ---")



#Reads the text from specified book path ie. frankenstein.txt file from /books
def get_book(book_path):
    with open(book_path) as f :
        file_contents = f.read()
        return file_contents

#counts the words in the book
def get_word_count(text):
    words = text.split()
    count = len(words)
    return count

#counts letters in the book. Converts the letters to lowercase, checks if char is aphabetic, counts it and returns a dictionary with the letter and its count {'x' : _ , 'y' : _ , ...etc.}
def get_letter_count_dict(text):
    lower_string = text.lower()
    letters_dict = {}
    for char in lower_string:
        if char.isalpha():
            if char in letters_dict:
                letters_dict[char] += 1
            else:
                letters_dict[char] = 1
    return letters_dict

#A funtion that takes a dictionary and return a value of the "num" key, used for .sort in below function
def sort_on(dict):
    return dict['num']

#Sorts through the dictionary and return a sorted list of dictionaries [{"char" : _ , "num" : _ }]
def letter_dict_to_list(letter_count_dict):
    sorted_list = []
    for letter in letter_count_dict:
        sorted_list.append({"char": letter, "num" : letter_count_dict[letter]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

  
main()