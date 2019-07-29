def isPalindrome(s):
    s = "".join(e.lower() for e in s if e.isalnum())
    for i in range(len(s)):
        if i > len(s) / 2:
            break
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

class Solution(object):
    def isPalindrome(self, s):
        return isPalindrome(s)
