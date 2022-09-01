class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n <= 1:
            return ""
        isodd = n%2!=0
        for i in range(((n)//2)+1):
            if not palindrome[i] == "a":
                if isodd and (i == (n-1)//2):
                    break
                palindrome = palindrome[0:i] + "a" + palindrome[i+1:n]
                return palindrome
            
        palindrome = palindrome[0:n-1] + "b"
        return palindrome