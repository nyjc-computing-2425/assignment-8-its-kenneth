# Built-in imports


def reverse(text: str) -> str:
    '''
    Reverses a string
    Parameter
    ---------
    text: str
        string to be reversed
    Return
    ------
    str:
        reverse of text
    '''
    if len(text) < 2:
        return text
    else:
        return reverse(text[1:]) + text[0]

def is_palindrome(word: str) -> bool:
    '''
    Determines whether a word is a palindrome
    Parameter
    ---------
    word: str
        word to be checked
    Return
    ------
    bool:
        whether the word is a palindrome
    '''
    word = word.lower().strip()
    if len(word) < 2:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return is_palindrome(word[1:-1])