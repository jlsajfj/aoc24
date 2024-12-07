# Read input from 1.txt and create left and right arrays
with open('1.txt', 'r') as file:
    left = []
    right = []
    for line in file:
        a, b = map(int, line.strip().split())
        left.append(a)
        right.append(b)

# Sort left and right arrays separately
left.sort()
right.sort()

ans = 0
for a, b in zip(left, right):
    ans += abs(a - b)

print(ans)
