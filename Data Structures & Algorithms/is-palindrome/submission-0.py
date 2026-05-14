class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower=s.lower()
        s_r=""
        for ch in s_lower:
            if ch.isalnum():
                s_r+=ch
        s_rev=s_r[ ::-1]
        if s_r==s_rev:
            return True
        return False