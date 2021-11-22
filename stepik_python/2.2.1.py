# https://stepik.org/lesson/24466/step/5?unit=6773
import datetime
import sys

sys.stdin = open("python/2.2.1_input.txt", "r")

year, month, day = [int(number) for number in sys.stdin.readline().strip().split(" ")]
days = int(sys.stdin.readline().strip())

input_date = datetime.date(year, month, day)
output_date = input_date + datetime.timedelta(days)
print(output_date.year, output_date.month, output_date.day)
