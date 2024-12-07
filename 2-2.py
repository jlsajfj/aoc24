reports = []
with open("2.txt", "r") as file:
    for line in file:
        reports.append(list(map(int, line.strip().split())))


def test_report(report: list[int]) -> bool:
    prev = report[1]
    if len(report) == 1:
        return True
    elif len(report) == 2:
        if 0 < abs(report[0] - prev) <= 3:
            return True
    else:
        direction = prev - report[0]
        if not (0 < abs(direction) <= 3):
            return False
        for num in report[2:]:
            if num == prev or (num - prev) * direction < 0 or abs(num - prev) > 3:
                break
            prev = num
        else:
            return True

    return False


ans = 0
for report in reports:
    if test_report(report):
        ans += 1
    else:
        for i in range(len(report)):
            modified_report = report[:i] + report[i+1:]
            if test_report(modified_report):
                ans += 1
                break
print(ans)
