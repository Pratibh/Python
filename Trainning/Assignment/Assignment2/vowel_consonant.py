__author__ = 'pratibh'

# Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
vowels=('a','e','i','o','u','A','E','I','O','U')
def check_vowel(x):
    if x in vowels:
        print "true"
    else:
        print "False"

print "Enter the character"
character_input = raw_input()
check_vowel(character_input)