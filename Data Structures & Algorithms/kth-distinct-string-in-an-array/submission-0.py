class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        seen = []
        for word, freq in count.items():
            if freq == 1:
                seen.append(word)
        if len(seen) >= k:
            return seen[k-1]
        else:
            return ""

        

        