class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num in nums1:
            if num in nums2:
                found = False
                index = nums2.index(num)
                for x in nums2[index+1:]:
                    if x > num:
                        res.append(x)
                        found = True
                        break
            if not found:
                res.append(-1)
        return res 

            