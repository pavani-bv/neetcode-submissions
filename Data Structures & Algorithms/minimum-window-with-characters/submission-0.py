class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
             return ""
        left = 0
        need = {}
        window = {}
        for c in t:
            need[c]=need.get(c,0)+1
        def valid():
            for c in need:
                if window.get(c,0)<need[c]:
                    return False
            return True
        
        res = ""
        for right in range(len(s)):
            window[s[right]]=window.get(s[right],0) + 1
            while valid():
                if not res or (right - left + 1)<len(res):
                    res = s[left:right+1]
                window[s[left]]-=1
                left+=1
        return res

