# product subarray less than k
def numSubarrayProductLessThanK(nums, k):
        if k < 1:
            return 0
        l = ans = 0
        prod = 1
        for right , val in enumerate(nums):
            prod = prod*val
            print(prod)
            if prod >= k:
                while prod >= k and l <= right:
                    prod /= nums[l]
                    l=l+1
            ans += right - l + 1
        return ans

# O(n)
print(numSubarrayProductLessThanK( nums = [10,5,2,6], k = 100))










# For those who are confused, let's use the example nums = [10,5,2,6]:

# If we start at the 0th index, [10,5,2,6], the number of intervals is obviously 1.
# If we move to the 1st index, the window is now [10,5,2,6]. The new intervals created are [5] and [10,5], so we add 2.
# Now, expand the window to the 2nd index: [10,5,2,6]. The new intervals are [2], [5,2], and [10,5,2], so we add 3.
# The pattern should be obvious by now; we add right - left + 1 to the output variable every loop!