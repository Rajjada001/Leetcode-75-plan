class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        prev = 0
        max_candies = max(candies) 
        i = 0
        res = [False for _ in range(len(candies))]
        while i<len(candies):
            if candies[i]+extraCandies >= max_candies:
                res[i] = True

            i+=1
        return res 
            
