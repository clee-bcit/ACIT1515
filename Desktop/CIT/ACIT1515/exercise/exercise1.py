# ACIT1515
# Exercise 1
# Chris Chanwoo Lee

import string
# f = open('new_words.txt', 'r')
# a = f.read()
# c = f.close()
# user_input = input('Enter a single-letter from a-z or A-Z: ')
# if user_input == 'Open':
#     print(a)
    
# elif user_input == 'Close':
#     print(c)


# def read_contents():
#     f = open('new_words.txt', 'r')
#     user_input = ('Open or Close file?')
#     if user_input == 'Open':
#         print(f.read);

##############
# my_file = open('new_words.txt')

# print(my_file.read())

# my_file.close()

################
def read_contents():
    with open('new_words.txt', 'r') as my_file:
        print(my_file.read())
        
def user_letter():
    singleletter = input('Enter a letter from [a-z] or [A-Z]: ')
    file_count = 0
    word_count = 0
    with open('new_words.txt', 'r') as my_file:
        data = my_file.read().splitlines()
        for line in data:
            if line.startswith(singleletter):
                file_count += 1
                
        for line in data:
            word_count += 1
        
    print(f'Enter a letter from a-z or A-Z: {singleletter}')
    print(f'File new_words.txt contains {word_count} words.')
    print(f'There are {file_count} words that start with the letter'
          
def validate

        
        
def main():
    # read_contents()
    user_letter()
    
    
if __name__ == '__main__':
    main() 

