def numberOfRounds(loginTime: str, logoutTime: str) -> int:
    loginTime = loginTime.split(":")
    loginTime = int(loginTime[0]) * 60 + int(loginTime[1])

    logoutTime = logoutTime.split(":")
    logoutTime = int(logoutTime[0]) * 60 + int(logoutTime[1])

    nextDayLogout = logoutTime < loginTime

    if loginTime % 15 != 0:
        loginTime += 15
    loginTime //= 15
    logoutTime //= 15

    if nextDayLogout:
        result = (96 - loginTime) + logoutTime
    else:
        result = logoutTime - loginTime

    return result if result > 0 else 0
        

print(numberOfRounds("23:46", "00:01"))
print(numberOfRounds("23:48", "23:16"))
print(numberOfRounds("00:01", "00:00"))
print(numberOfRounds("00:47", "00:57"))
print(numberOfRounds("22:59", "23:32"))
print(numberOfRounds("09:31", "10:14"))
print(numberOfRounds("21:30", "03:00"))