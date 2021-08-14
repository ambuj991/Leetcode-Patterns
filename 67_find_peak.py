def findPeakElement(nums):
        low, high = 0, len(nums)-1
        while low < high:
            mid =  ((high+low)//2)
            if nums[mid] < nums[mid+1]:
                low = mid+1
            else:
                high = mid
        return low
nums = [1,2,3,1]
print(findPeakElement(nums))

# O(log(n)) Binary Search:
# How does binary search work for this problem?
# Let's look at mid.
# If nums[mid] < nums[mid+1], then there has to be a peak element in the right side of mid.
# Either the numbers increase until we reach the end and then the last element will be a peak, or at some point a number gets smaller and right there we will have a peak.
# Same for the left side of mid.