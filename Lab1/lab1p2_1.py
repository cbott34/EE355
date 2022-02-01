# # 1) Write a script (lab1p2_1.py) that reads an input text file, in.txt (at most 500 words;
# # words may include special characters and numbers).
# # Your script then verify if the string read from the inputfile is a palindrome and print 'Yes' if it is,
# # and 'No' otherwise. A phrase is a palindrome if, after converting all uppercase letters into lowercase 
# letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric
#  characters include letters and numbers.
# # Consider that the sample in.txt has the following sentence “thisisapalindromemordnilapasisiht”
# # Then your algorithm should print 'Yes' on the screen.
 
 # Function prints whether or not string is palindrome

def IsPalindrome(x):
    y = x[::-1]             # reverses string
    if x == y:
        print('Yes')
    else:
        print('No')

# Driver Code

with open('in.txt') as file:
    input = file.read()
    words = ''.join(ch for ch in input if ch.isalnum())     # Removes all non alphanumeric characters
    words = words.lower()   # Makes all uppercase lowercase
isPalindrome(words)
print (words)