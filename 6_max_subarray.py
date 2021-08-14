class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_far=nums[0]
        max_curr=nums[0]
        for i in range(1, len(nums)):
            max_curr += nums[i]
            max_curr = max(max_curr, nums[i])
            max_far = max(max_curr, max_far)
        return max_far
# handles -ve integers as well
            