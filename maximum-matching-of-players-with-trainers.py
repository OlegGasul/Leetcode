def matchPlayersAndTrainers(players, trainers) -> int:
    players.sort()
    trainers.sort()
        
    result = 0
    while players and trainers:
        if players[0] <= trainers[0]:
            players.pop(0)
            trainers.pop(0)
            result += 1
        else:
            trainers.pop(0)
                
    return result

print(matchPlayersAndTrainers([4, 7, 9], [8, 2, 5, 8]))
print(matchPlayersAndTrainers([1, 1, 1], [10]))