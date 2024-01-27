def checking_palindrome(palindrome):
  index = 0
  index_2 = -1
  is_palindrome = True

  while is_palindrome:
      final_word = palindrome.lower()
      lenghth = len(palindrome)
      center_index = (lenghth - 1) // 2

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


print("Check that word is palindrome")
input_word = input()
checking_palindrome(input_word)