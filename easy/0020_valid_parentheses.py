# using stack data structure
# time - O(n)
# space - O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        stack = []
        for c in s:
            if c in pairs.values():
                stack.append(c)
            else:
                if stack == []:
                    return False
                if stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
        return stack == []
        
