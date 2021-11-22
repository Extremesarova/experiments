# https://stepik.org/lesson/24463/step/7?unit=6771
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


sys.stdin = open("2.1.2_input.txt", "r")

exceptions = {}
n = int(sys.stdin.readline().strip())
for _ in range(n):
    line = str(sys.stdin.readline()).split()
    exceptions[line[0]] = line[2:]

q = int(sys.stdin.readline().strip())
previous_errors = []
for i in range(q):
    error = str(sys.stdin.readline()).strip()
    previous_errors.append(error)
    if len(previous_errors) == 1:
        continue
    else:
        for previous_error in previous_errors[:-1]:
            if find_path(exceptions, error, previous_error):
                print(error)
                break

"""
Sample Input:

4
ArithmeticError
ZeroDivisionError : ArithmeticError
OSError
FileNotFoundError : OSError
4
ZeroDivisionError
OSError
ArithmeticError
FileNotFoundError
Sample Output:

FileNotFoundError
"""


