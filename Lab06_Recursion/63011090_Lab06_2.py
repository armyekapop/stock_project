def palindrome(char):
    return len(char)<2 or char[0] == char[-1] and palindrome(char[1:-1])
A = input('Enter Input : ')
if palindrome(A) == True:
    print("'"+A+"' is palindrome")
else:
    print("'"+A+"' is not palindrome")
