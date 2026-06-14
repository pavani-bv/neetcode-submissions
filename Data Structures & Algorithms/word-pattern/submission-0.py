class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mappw , mapwp = {} , {}
        word = s.split()
        if len(pattern) != len(word):
            return False
       
        for i in range(len(word)):
            c1, c2 = word[i], pattern[i]
            if ((c1 in mappw and mappw[c1]!=c2) or (c2 in mapwp and mapwp[c2]!=c1)):
                return False
            mappw[c1] = c2
            mapwp[c2] = c1
        return True