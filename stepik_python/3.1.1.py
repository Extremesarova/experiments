# https://stepik.org/lesson/24469/step/6?unit=6775
import sys

sys.stdin = open("3.1.1_input.txt", "r")

s = sys.stdin.readline().strip()
a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

counter = 0
while True:
    if a not in s:
        print(counter)
        break
    elif counter > 1000:
        print("Impossible")
        break
    else:
        s = s.replace(a, b)
        counter += 1
