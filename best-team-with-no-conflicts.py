import functools

def bestTeamScore(scores, ages) -> int:
    length = len(scores)

    dp = [0] * length

    for i in range(length):
        dp[i] = [ages[i], scores[i]]

    def compare(a, b):
        return b[0] - a[0]

    dp = sorted(dp, key = functools.cmp_to_key(compare))

    print(dp)


# print(bestTeamScore(
#     [1, 3, 5, 10, 15],
#     [1, 2, 3, 4, 5]))

# print(bestTeamScore(
#     [4, 5, 6, 5],
#     [2, 1, 2, 1]))

print(bestTeamScore(
    [1, 2, 3, 5],
    [8, 9, 10, 1]))