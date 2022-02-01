# # 2) Write a script (lab1p2_2.py) that implements the functionality to find whether the string read from 
# the input file can be a palindrome after deleting at most one character from it. (You are not supposed to
#  use any built-in string functions or packages). If it is possible, you need to print 'Yes' and the index
#   of character and the actual character to be deleted (if needed), otherwise print 'No'.
# # Eg: i) Consider that the sample in.txt has the following sentence “abcca”, your algorithm should output 
# 'Yes, delete b at position 1'. Note, python is zero-indexed.
# # ii) Consider that the sample in.txt has the following sentence “abccba”, your algorithm should output 
# 'Yes'. Note: strng itself is a palindrome and no need to delete.
# # iii) Consider that the sample in.txt has the following sentence “abcdcea”, your algorithm should output
#  'No'. 
 
def IsPalindrome(x: str, left: int, right: int) -> bool:
    while left < right:
        if x[left] != x[right]:
            return False
        left += 1
        right -= 1
    return True
    
def PossibleByRemovingOneChar(x: str) -> int:
     
    # Initialize left and right by both the ends of the string
    left = 0
    right = len(x) - 1
 
    # loop until left and right cross each other
    while left < right:
 
        # If both characters are equal then move both pointer towards end
        if x[left] == x[right]:
            left += 1
            right -= 1
        else:
 
            # If removing str[left] makes the whole string palindrome.
            # We basically check if substring str[left+1..right] is
            # palindrome or not.
            if IsPalindrome(x, left + 1, right):
                return left
 
            # If removing str[right] makes the whole string palindrome
            # We basically check if substring str[left+1..right] is
            # palindrome or not
            if IsPalindrome(x, left, right - 1):
                return right
            return -1
 
    # We reach here when complete string will be palindrome 
    # if complete string is palindrome then return mid character
    return -2

# Driver Code

with open('in.txt') as file:
    input = file.read()
    words = ''.join(ch for ch in input if ch.isalnum())     # Removes all non alphanumeric characters
    words = words.lower()       # Makes all uppercase lowercase
    x = PossibleByRemovingOneChar(words)
    if x == -1:
        print("No")
    elif x == -2:
        print("Yes")
    else:
        print("Yes, delete '" + words[x] +"' at index", x)