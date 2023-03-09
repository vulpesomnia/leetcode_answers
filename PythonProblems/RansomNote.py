class Solution(object):#https://leetcode.com/problems/ransom-note/
    def canConstruct(self, ransomNote, magazine):
        ransomArray = list(ransomNote)
        magazineArray = list(magazine)
        for letter in ransomArray:
            if letter in magazineArray:
                magazineArray.remove(letter)
            else:
                return False
        return True