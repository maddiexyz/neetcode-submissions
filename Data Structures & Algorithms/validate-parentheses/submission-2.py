class Solution:
    def isValid(self, s: str) -> bool:
        pairs = (("{","}"),("(",")"),("[","]"))
        stack=[]
        for char in s:
            print(stack)
            for left,right in pairs:
                if char==left:
                    stack.append(char)
                if char==right:
                    if not stack or stack[-1]!=left:
                        return False
                    else:
                        stack.pop()
        return not stack
            