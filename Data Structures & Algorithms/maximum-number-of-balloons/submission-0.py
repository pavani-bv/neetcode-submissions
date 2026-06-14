class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        smap = {}
        for c in text:
            smap[c] = smap.get(c,0) + 1
        smap2 = {}
        text2 = "balloon"
        for c in text2:
            smap2[c] = smap2.get(c,0) + 1
        ans = float('inf')
        for c in smap2:
            ans = min(ans, smap.get(c,0)//smap2[c])
        return ans