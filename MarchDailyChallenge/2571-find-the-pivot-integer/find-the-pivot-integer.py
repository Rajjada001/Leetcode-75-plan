class Solution:
    def pivotInteger(self, n: int) -> int:
        s = (n+1)*n//2
        pivot = (int)(math.sqrt(s))
        if pivot * pivot == s:
            return int(pivot)
        else:
            return -1