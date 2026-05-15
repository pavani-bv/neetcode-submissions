class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        lmax=0
        rmax=0
        res=0
        while left < right:
            if height[left]<height[right]:
                if height[left]>=lmax:
                    lmax=height[left]
                else:
                    res += lmax-height[left]
                left+=1
            else:
                if height[right]>=rmax:
                    rmax=height[right]
                else:
                    res += rmax-height[right]
                right-=1
        return res
                    