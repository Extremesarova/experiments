#https://stepik.org/lesson/24462/step/7?unit=6768
import sys


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None


sys.stdin = open("1.6.1_input.txt", "r")

classes = {}
n = int(sys.stdin.readline().strip())
for _ in range(n):
    line = str(sys.stdin.readline()).split()
    classes[line[0]] = line[2:]

q = int(sys.stdin.readline().strip())
for i in range(q):
    possible_ancestor, possible_heir = map(str, str(sys.stdin.readline()).split())
    if find_path(classes, possible_heir, possible_ancestor):
        print("Yes")
    else:
        print("No")
