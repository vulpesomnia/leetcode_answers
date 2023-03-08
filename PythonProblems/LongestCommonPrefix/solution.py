class Solution(object):#https://leetcode.com/problems/longest-common-prefix/
    def longestCommonPrefix(self, strs):
        Lastprefix = ""
        prefix = ""
        biggest = ""
        for word in strs:
            if len(word) > len(biggest):
                biggest = word
        for x in range(len(biggest)):
            lastPrefix = prefix
            prefix = biggest[:x+1]
            for word in strs:
                if word[:len(prefix)] != prefix:
                    return lastPrefix
        return prefix