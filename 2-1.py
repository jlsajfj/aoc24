reports = []
with open("2.txt", "r") as file:
    for line in file:
        reports.append(list(map(int, line.strip().split())))

ans = 0
for report in reports:
    prev = report[1]
    if len(report) == 1:
        ans += 1
    elif len(report) == 2:
        if 0 < abs(report[0] - prev) <= 3:
            ans += 1
    else:
        direction = prev - report[0]
        if not (0 < abs(direction) <= 3):
            continue
        for num in report[2:]:
            if num == prev or (num - prev) * direction < 0 or abs(num - prev) > 3:
                break
            prev = num
        else:
            ans += 1
print(ans)
