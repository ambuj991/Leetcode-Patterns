
def generateParenthesis( n: int) :
        stack, res = [], []
        def backtrack(openb, closeb):
            if openb == closeb == n:
                res.append(''.join(stack))
            if openb < n:
                stack.append('(')
                backtrack(openb+1 , closeb)
                stack.pop()
            if closeb < openb :
                stack.append(')')
                backtrack(openb , closeb+1)
                stack.pop()
        backtrack(0, 0)
        return res

print(generateParenthesis(3))

# T(c) = https://leetcode.com/problems/generate-parentheses/discuss/842989/Easy-to-understand-time-complexity-analysis-(with-pictures)
                