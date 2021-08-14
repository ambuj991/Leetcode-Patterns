def subsets( nums):
        res, subset = [], []
        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                
                return 
            subset.append(nums[i])
            print(subset)
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res
    
print( subsets([1,2,3]))
    
# O(n) = n*2^n