def sortColors( nums):
        a, arr_size = nums, len(nums)
        lo = mid = 0
        hi = arr_size - 1
        while mid <= hi:
            if a[mid] == 0:
                a[lo], a[mid] = a[mid], a[lo]
                lo = lo + 1
                mid = mid + 1
            elif a[mid] == 1:
                mid = mid + 1
            else:
                a[mid], a[hi] = a[hi], a[mid]
                hi = hi - 1
        return nums

print(sortColors( nums = [2,0,2,1,1,0]))