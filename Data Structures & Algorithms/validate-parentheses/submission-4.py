class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        opening_brackets = ["(", "[", "{"]
        bracket_pairs = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        brackets_encountered = []

        for i in range(len(s)):
            if s[i] in opening_brackets:
                brackets_encountered.append(s[i])
            
            else:
                if len(brackets_encountered) == 0:
                    return False
                elif bracket_pairs[brackets_encountered[-1]] == s[i]:
                    brackets_encountered.pop()
                else:
                    return False

        if len(brackets_encountered) == 0:
            return True
        else:
            return False