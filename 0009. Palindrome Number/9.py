class Solution:
    def isPalindrome(self, x: int) -> bool:
        list_x = list(str(x))
        reverse_x = list(reversed(list_x))
        if(list_x != reverse_x):
            return False
        else:
            return True