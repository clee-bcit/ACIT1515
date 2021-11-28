# ACIT1515
# Exercise 1
# Chris Chanwoo Lee
import string
def read_contents(file_name):
    file_name = input('Please enter your file name: ')
    with open(file_name, 'r') as my_file:
        data = my_file.read().splitlines()
        return data
        
def user_letter():
    file_count = 0
    word_count = 0
    while True:
        try:
            singleletter = input('Enter a letter from [a-z] or [A-Z]: ')
            if len(singleletter) == 1 and singleletter in string.ascii_letters:
                with open('new_words.txt', 'r') as my_file:
                    data = my_file.read().splitlines()
                    for line in data:
                        if line.startswith(singleletter):
                            file_count += 1
                    for line in data:
                        word_count += 1
                    print(f'Enter a letter from a-z or A-Z: {singleletter}')
                    print(f'File new_words.txt contains {word_count} words.')
                    print(f'There are {file_count} words that start with the letter {singleletter}')
                    break
            else:
                print('**** Invalid ltter')
        except ValueError:
            print("Invalid")
            continue
            
def validate():
    singleletter = input('Enter a letter from [a-z] or [A-Z]: ')
    # file_count = 0
    # word_count = 0
    if len(singleletter) == 1 and singleletter in string.ascii_letters:
        #  with open('new_words.txt', 'r') as my_file:
        #     data = my_file.read().splitlines()
        #     for line in data:
        #         if line.startswith(singleletter):
        #             file_count += 1
                    
        #     for line in data:
        #         word_count += 1
        #     print(f'Enter a letter from a-z or A-Z: {singleletter}')
        #     print(f'File new_words.txt contains {word_count} words.')
        #     print(f'There are {file_count} words that start with the letter {singleletter}')
        return True

    else:
        return False
        # print('*** Invalid letter')

def count_words(singleletter, listofword):
    upper_count = 0
    lower_count = 0
    total_count = 0
    while True:
        try:
            singleletter = input('Enter a letter from [a-z] or [A-Z]: ')
            upper_letter = singleletter.upper()
            lower_letter = singleletter.lower()

            if len(singleletter) == 1 and singleletter in string.ascii_letters:
                with open('new_words.txt', 'r') as my_file:
                    data = my_file.read().splitlines()
                    for line in data:
                        if line.startswith(upper_letter):
                            upper_count += 1
                    for line in data:
                        if line.startswith(lower_letter):
                            lower_count += 1
                    total_count = upper_count + lower_count
                    print(f'There are {total_count} words that start with the letter {singleletter}')
                    break
            else:
                print('**** Invalid ltter')
        except ValueError:
            print("Invalid")
            continue

        return total_count
            
  

def main():
    file_name = ''
    read_contents(file_name)

    user_letter()

    singlestring = ''
    validate(singlestring)
    
    singleletter = ''
    listofword = ''
    count_words(singleletter, listofword)
    
if __name__ == '__main__':
    main() 

