from collections import defaultdict

class Solution:
    def splitPainting(self, segments):
        line = defaultdict(int)
        
        for start, end, color in segments:
            line[start] += color
            line[end] -= color
        
        painting = []
        prev_color, prev_point = 0, 0
        
        for point in sorted(line.keys()):
            if prev_color:
                painting.append([prev_point, point, prev_color])
            prev_point = point
            prev_color += line[point]
        
        return painting

solution = Solution()
print(solution.splitPainting([[1, 4, 5], [4, 7, 7], [1, 7, 9]]))