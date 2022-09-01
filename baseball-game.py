def calPoints(ops) -> int:
    score = []

    for record in ops:
        if record[0] == "-" or record.isdigit():
            if record[0] == "-":
                value = - int(record[1:])
            else:
                value = int(record)
            score.append(value)
        elif record == "+":
            score.append(score[-1] + score[-2])
        elif record == "C":
            score.pop()
        elif record == "D":
            score.append(score[-1] * 2)

    return sum(score)

print(calPoints(["5", "2", "C", "D", "+"]))
print(calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))