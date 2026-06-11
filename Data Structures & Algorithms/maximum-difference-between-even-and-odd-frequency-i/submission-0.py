class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        odd_freq = {}
        even_freq = {}
        for ch, count in freq.items():
            if count%2!=0:
                odd_freq[ch] = count
            else:
                even_freq[ch] = count
        return max(odd_freq.values()) - min(even_freq.values())
        
        


