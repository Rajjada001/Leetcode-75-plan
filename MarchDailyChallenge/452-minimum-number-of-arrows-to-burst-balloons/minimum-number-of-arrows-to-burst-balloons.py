class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        print(points)
        start = points[0][1]
        count = 1
        for i in range(len(points)):
            if points[i][0] <= start:
                start = min(start, points[i][1]) 
            else:
                count += 1
                start = points[i][1]
        
        return count