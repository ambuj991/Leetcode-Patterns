def rob( nums):
        rob1, rob2 = 0, 0
        for n in nums:
            t = max(rob1 + n, rob2)
            rob1 = rob2 
            rob2 = t
        return rob2
print(rob(1, 2, 3, 1))
