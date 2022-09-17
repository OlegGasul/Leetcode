import heapq
import functools
from collections import Counter

def mostBooked(n: int, meetings) -> int:
    meetings.sort()

    counter = Counter()

    rooms = [i for i in range(n)]
    heapq.heapify(rooms)

    meetingRooms = []
    heapq.heapify(meetingRooms)

    for meet in meetings:
        # Release all rooms where end time is earlier than current start time
        while meetingRooms and meetingRooms[0][0] <= meet[0]:
            time, room = heapq.heappop(meetingRooms)
            heapq.heapify(meetingRooms)

            heapq.heappush(rooms, room)
            heapq.heapify(rooms)
        
        if not rooms:
            # If all rooms are busy at this moment
            time, room = heapq.heappop(meetingRooms)
            heapq.heappush(meetingRooms, [meet[1] + (time - meet[0]), room])
            heapq.heapify(meetingRooms)

            counter[room] += 1
        else:
            room = heapq.heappop(rooms)
            heapq.heapify(rooms)

            heapq.heappush(meetingRooms, [meet[1], room])
            heapq.heapify(meetingRooms)

            counter[room] += 1
    
    return counter.most_common()[0][0]


print(mostBooked(2, [[19, 20], [14, 15], [13, 14], [11, 20]]))
print(mostBooked(4, [[19, 20], [14, 15], [13, 14], [11, 20]]))
print(mostBooked(4, [[18, 19], [3, 12], [17, 19], [2, 13], [7, 10]]))
print(mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]]))
print(mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]))