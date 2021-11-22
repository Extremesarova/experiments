import sys

sys.stdin = open("python/3.1.2_input.txt", "r")

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

counter = 0
for i in range(len(s) - len(t) + 1):
    check = s[i:i + len(t)]
    if check == t:
        counter += 1

print(counter)