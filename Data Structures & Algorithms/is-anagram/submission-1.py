class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = list(s)
        l1 = list(t)
        if sorted(s1) == sorted(l1):
            return True
        else:
            return False
        