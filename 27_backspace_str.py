# backspace string

class Solution:
    def backspaceCompare(self, s: str, t: str):
        def solve(S):
            ans=[]
            for i in S:
                if i!='#':
                    ans.append(i)
                elif ans:
                    ans.pop()
            return ''.join(ans)
        return solve(s) == solve (t)

# TC =O(m+n)
#SP = O(m+n)