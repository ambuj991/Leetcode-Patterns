class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i ,v in enumerate(nums):
            if i>0 and v == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                three_sum = v+nums[l]+nums[r]
                if three_sum > 0:
                    r = r-1
                elif three_sum < 0:
                    l = l+1
                else:
                    res.append([v, nums[l], nums[r]])
                    l = l+1
                    while l<r and nums[l] == nums[l-1]:
                        l=l+1
        return res

# O(n^2)