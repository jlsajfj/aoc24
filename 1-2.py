# Read input from 1.txt and create left and right arrays
with open('1.txt', 'r') as file:
    left = []
    right = []
    for line in file:
        a, b = map(int, line.strip().split())
        left.append(a)
        right.append(b)

counter = {}
for num in right:
    if num in counter:
        counter[num] += 1
    else:
        counter[num] = 1

ans = 0
for num in left:
    if num in counter:
        ans += num * counter[num]

print(ans)
