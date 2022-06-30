class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for parenthesis in s:
            if parenthesis in ["(", "{", "["]:
                stack.append(parenthesis)
            else:
                if not stack:
                    return False
                parenthesis_check = stack.pop()
                if parenthesis_check == "(":
                    if parenthesis != ")":
                        return False
                if parenthesis_check == "{":
                    if parenthesis != "}":
                        return False               
                if parenthesis_check == "[":
                    if parenthesis != "]":
                        return False              
        if stack:
            return False
        return True