from collections import Counter

def countMatches2(items, ruleKey: str, ruleValue: str) -> int:
    counters = {
        "type": Counter(),
        "color": Counter(),
        "name": Counter()
    }
        
    for item in items:
        counters["type"][item[0]] += 1
        counters["color"][item[1]] += 1
        counters["name"][item[2]] += 1
            
        
    return counters[ruleKey][ruleValue]

def countMatches(items, ruleKey: str, ruleValue: str) -> int:
    indecies = {
        "type": 0,
        "color": 1,
        "name": 2
    }

    index = indecies[ruleKey]
    result = 0
    for item in items:
        if item[index] == ruleValue:
            result += 1

    return result


print(countMatches([["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]], "color", "silver"))
print(countMatches([["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]], "type", "phone"))