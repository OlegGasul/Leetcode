class Solution:
    def reformatDate(self, date: str) -> str:
        months = {
            "Jan": "01",
            "Feb": "02",
            "Mar": "03",
            "Apr": "04",
            "May": "05",
            "Jun": "06",
            "Jul": "07",
            "Aug": "08",
            "Sep": "09",
            "Oct": "10",
            "Nov": "11",
            "Dec": "12"
        }

        parts = date.split(' ')

        day = ""
        i = 0
        while i < len(parts[0]) and parts[0][i].isdigit():
            day += parts[0][i]
            i += 1
        
        if len(day) < 2:
            day = "0" + day

        return parts[2] + "-" + months[parts[1]] + "-" + day

solution = Solution()
print(solution.reformatDate("20th Oct 2052"))
print(solution.reformatDate("6th Jun 1933"))
print(solution.reformatDate("26th May 1960"))