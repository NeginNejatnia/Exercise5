word = input()
def isPalindrome(word):
 return word == word[::-1]  # reversing a string
result = isPalindrome(word) 
if result:
 print("palindrome")
else:
 print("not palindrome")