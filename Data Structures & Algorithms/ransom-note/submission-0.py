class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = Counter(ransomNote)
        b = Counter(magazine)
        if len(ransomNote) > len(magazine):
            return False
        elif len(ransomNote)==len(magazine):
            return (True if a == b else False)
        for count in a:
            if a[count] > b[count]:
                return False
        return True
        