from collections import Counter
import functools

def watchedVideosByFriends(watchedVideos, friends, id: int, level: int):
    def getFirends():
        nonlocal level

        ids = set([id])
        
        visited = set()
        visited.add(id)

        while level:
            newIds = set()
            for fid in ids:
                for fid1 in friends[fid]:
                    if fid1 in visited:
                        continue
                
                    newIds.add(fid1)
                    visited.add(fid1)

            ids = newIds

            level -= 1

        return ids

    ids = getFirends()

    def compare(a, b):
        if a[1] == b[1]:
            if a[0] > b[0]:
                return 1
            elif a[0] < b[0]:
                return -1
            else:
                return 0
        else:
            return a[1] - b[1]

    counter = Counter()
    for fid in ids:
        for video in watchedVideos[fid]:
            counter[video] += 1

    return [pair[0] for pair in sorted(counter.items(), key = functools.cmp_to_key(compare))]

print(watchedVideosByFriends([["A", "B"], ["C"], ["B", "C"], ["D"]], [[1, 2], [0, 3], [0, 3], [1, 2]], 0, 1))
print(watchedVideosByFriends([["xk", "qvgjjsp", "sbphxzm"], ["rwyvxl", "ov"]], [[1], [0]], 0, 1))