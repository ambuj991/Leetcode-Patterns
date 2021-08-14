class Solution:
    def permuteUnique(self, nums) :
        res,perm =  [], []
        count = {n:0 for n in nums}
        for n in nums:
            count[n] += 1
       
        def dfs():
            if len(perm) == len(nums):
                res.append(perm[:])
                print( res)
                return 
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1
                    dfs()
                    count[n] +=1
                    perm.pop()
        dfs()
        return res
s  =Solution()
print(s.permuteUnique([1, 1, 2 ]))

# Time Complexity: \mathcal{O}\big(\sum_{k = 1}^{N}{P(N, k)}\big)O(∑ 
# k=1
# N
# ​
#  P(N,k)) where P(N, k) = \frac{N!}{(N - k)!} = N (N - 1) ... (N - k + 1)P(N,k)= 
# (N−k)!
# N!
# ​
 

