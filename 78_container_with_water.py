class Solution:
    def maxArea(self, height):
        nums = height
        res = 0
        l, r = 0,len(nums)-1
        
        while l < r:
            area = (r - l)*min(nums[l], nums[r])
            res = max(res, area)
            if nums[l] > nums[r]:
                r= r-1
            else:
                l= l+1
        return res
        
# O(n)