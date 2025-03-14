def is_Palindrome(word):
    reversed_word = "".join(reversed(word))
    if word == reversed_word:
        print("Yes, it is palindrome")
    else:
        print("No, it is not a palindrome")
word = input("Enter:")
is_Palindrome(word)            