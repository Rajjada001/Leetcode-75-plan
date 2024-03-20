class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rc = Counter(ransomNote)
        mc = Counter(magazine)
        for key in rc:
            if rc[key] > mc[key]:
                return False
            elif rc[key] < mc[key]:
                continue
        return True