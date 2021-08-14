# min subarr sum to target
# O(n)

import sys
def minSubArrayLen( target: int, nums):
        left = 0
        res = sys.maxsize
        subSum = 0
        for r, val in enumerate(nums):
            subSum += val
            while subSum >= target:
                res = min(res, r - left + 1)
                subSum -= nums[left]
                left += 1
        return res if res!=sys.maxsize else 0


            