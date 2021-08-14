def rob(nums):
        def helper(arr):
            r1 = r2 = 0
            for i in arr:
                t = max(r1+i , r2)
                r1 = r2
                r2 = t
            return r2
            
            
            
        m = max(nums[0], helper(nums[:-1]), helper(nums[1:]))
        return m


print(rob([2, 3, 2]))