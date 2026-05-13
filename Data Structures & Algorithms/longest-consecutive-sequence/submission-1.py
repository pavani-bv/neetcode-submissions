class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        leng=0
        for n in s:
            if n-1 not in s:
                cur=n
                count=1
                while cur+1 in s:
                    cur+=1
                    count+=1
                leng=max(leng,count)
        return leng

        