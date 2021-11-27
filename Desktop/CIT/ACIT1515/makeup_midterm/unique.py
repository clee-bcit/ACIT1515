# Chris Chanwoo Lee
# ACIT1515 - SET B
# A01016225

"""Module to calculate the total number and number unique letters in  a word

Hints:
    Determining the length of a sequence: 
        https://learn.zybooks.com/zybook/BCITACIT1515LaneFall2021/chapter/3/section/1?content_resource_id=49219136
    Set Basics: 
        https://learn.zybooks.com/zybook/BCITACIT1515LaneFall2021/chapter/3/section/4
    Function Basics: 
        https://learn.zybooks.com/zybook/BCITACIT1515LaneFall2021/chapter/4/section/1
    Docstrings and Doctests: 
        https://learn.zybooks.com/zybook/BCITACIT1515LaneFall2021/chapter/4/section/16?content_resource_id=49219776
        Course Content -> Class 4 -> Code Style -> Run-able Examples: doctest

"""

# add the unique_letters function, the docstring is below
"""Calculate and return the number of unique letters in word

Args:
    word (str): the word to calculate the number of unique letters

Returns:
    int: the number of unique letters in the word

Examples:
    >>> unique_letters('midterm')
    6

    >>> unique_letters('banana')
    3
"""

def unique_letters(word):
    unique_letters_set = ''.join(set(word))
    return len(unique_letters_set)

# add the letter_count function, the docstring is below
    """Calculate and return the number of letters in a word

    Args:
        word (str): the word to calculate the number of letters

    Returns:
        int: the number of letters in the word

    Examples:
        >>> letter_count('midterm')
        7

        >>> letter_count('banana')
        6
    """
def letter_count(word):
    return len(word)

def main():
    """Get a word from the user and print the total letters and unique letters"""

    word = input("Please enter a word")
    print(
        f"There are {letter_count(word)} letters, and {unique_letters(word)} unique letters in {word}"
    )


if __name__ == "__main__":
    main()