import heapq

class Solution:
    def rotateTable(self, input):
        input.sort()

        pq = []
        users = set()
        prevStart = None

        result = []

        for start, end, user in input:
            if pq:
                while pq and pq[0][0] <= start:
                    endTime, u = heapq.heappop(pq)
                    result.append((', '.join(users), prevStart, endTime))

                    users.discard(u)
                    prevStart = endTime
            
            if prevStart and users:
                result.append((', '.join(users), prevStart, start))

            heapq.heappush(pq, (end, user))
            users.add(user)

            prevStart = start

        if prevStart:
            result.append((', '.join(users), prevStart, end))

        return result
    
solution = Solution()
assert solution.rotateTable([(10, 100, 'Abby'), (50, 70, 'Ben'), (60, 120, 'Carla'), (150, 300, 'David')]) == [('Abby', 10, 50), ('Abby, Ben', 50, 60), ('Abby, Ben, Carla', 60, 70), ('Abby, Carla', 70, 100), ('Carla', 100, 120), ('David', 150, 300)]
assert solution.rotateTable([(10, 20, 'Abby'), (20, 30, 'Ben'), (30, 40, 'Carla'), (40, 50, 'David')]) == [('Abby', 10, 20), ('Ben', 20, 30), ('Carla', 30, 40), ('David', 40, 50)]