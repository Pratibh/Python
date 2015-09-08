__author__ = 'pratibh'

# 4) Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards).
# For example, is_palindrome("radar") should return True.

print("Enter a string to check if it is a palindrome or not")
palindrome_string = raw_input()

def is_palindrome(string_input):
    # reverse the string
    reversed_string = string_input[::-1]
    print reversed_string

    if(string_input == reversed_string):
        print "It is a palindrome"
    else:
        print "It is not a palindrome"

is_palindrome(palindrome_string)
