class Solution(object):#https://leetcode.com/problems/diagonal-traverse
    def findDiagonalOrder(self, mat):#even indexed diagonals are reversed
        width = len(mat[0])
        length = len(mat)
        size = width*length
        i = 0
        j = 0
        result = []
        temp = []
        for x in range(width+length-1):
            if x % 2 != 0:
                temp.reverse()
                result = result+temp
            else:
                result = result+temp
            temp = []
            while i < width+x and j > -1:
                if i >= length:
                    break
                temp.append(mat[i][j])
                j -= 1
                i += 1
            if x+1 < width:#if we havent reached the last column
                j = x+1
                i = 0
            else:#if we have reached the last column
                j = width-1#go to last column
                i = x-width+2
        return result+temp