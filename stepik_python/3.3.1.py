import sys
import requests
from bs4 import BeautifulSoup
sys.stdin = open("python/3.3.1_input.txt", "r")

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

a_res = requests.get(a)
a_content = a_res.content
a_text = a_res.text
result = "No"
a_soup = BeautifulSoup(a_content, "lxml")
for a_tag in a_soup.findAll('a', href=True):
    c = a_tag['href']
    c_res = requests.get(c)
    c_content = c_res.content
    c_soup = BeautifulSoup(c_content, "lxml")
    for c_tag in c_soup.findAll('a', href=True):
        possible_b = c_tag['href']
        if b == possible_b:
            result = "Yes"
            break
print(result)


