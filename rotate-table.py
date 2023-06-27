import heapq

class Solution1:
    def rotateTable(self, input):
        input.sort()

        pq = []
        users = set()
        prevStart = None

        result = []

        for start, end, user in input:
            if pq:
                while pq and pq[0][0] < start:
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
    
solution1 = Solution1()
print(solution1.rotateTable([(10, 100, 'Abby'), (50, 70, 'Ben'), (60, 120, 'Carla'), (150, 300, 'David')]))

