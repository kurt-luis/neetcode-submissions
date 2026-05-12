class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = []
        for i in s:
            if i.lower() in "abcdefghijklmnopqrstuvwxyz0123456789":
                letters.append(i.lower())
        
        
        if letters == list(reversed(letters)):
            return True
        else:
            return False