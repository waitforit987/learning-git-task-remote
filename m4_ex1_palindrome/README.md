# Palindrome Checker

This is a simple Python function `checking_palindrome` that checks whether a given word is a palindrome. A palindrome is a word, phrase, or sequence of characters that reads the same forward as backward.

## Function Signature

```python
def checking_palindrome(palindrome):
    """
    Checks if the given word is a palindrome.

    Parameters:
    - palindrome (str): The word to check.

    Returns:
    - bool: True if the word is a palindrome; False otherwise.
    """
    index = 0
    index_2 = -1
    is_palindrome = True

    while is_palindrome:
        final_word = palindrome.lower()
        length = len(palindrome)
        center_index = (length - 1) // 2

        if (len(final_word)) < 3 and (final_word[index]) == final_word[index_2]:
            print("It's a palindrome")
            break
        if (final_word[index]) == final_word[index_2]:
            index = index + 1
            index_2 = index_2 - 1
            if index <= center_index and index_2 <= center_index:
                print("It's a palindrome")
                break
        else:
            print("It's not a palindrome")
            break
    return True

# Example Usage
print("Check if a word is a palindrome")
input_word = input()
checking_palindrome(input_word