class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen = {}
        s1map = {}
        left = 0
        if len(s1)>len(s2):
            return False
        for c in s1:
            s1map[c]=s1map.get(c,0) + 1
        for right in range(len(s2)):
            seen[s2[right]]=seen.get(s2[right],0) + 1
            if right - left + 1 > len(s1):
                seen[s2[left]]-=1
                if seen[s2[left]]==0:
                    del seen[s2[left]]
                left+=1
            if seen == s1map:
                return True
        return False
            