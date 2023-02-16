class Solution(object):
    def isPalindrome(self, x):
        reverse = []
        y = list(str(x))
        for index in range(len(y)-1, -1, -1):
            reverse.append(y[index])
        return str(x) == "".join(reverse)
