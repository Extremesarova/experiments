import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
sys.stdin = open("python/3.3.2_input.txt", "r")

site = sys.stdin.readline().strip()

site_res = requests.get(site)
site_content = site_res.content

site_soup = BeautifulSoup(site_content, "html.parser")
res_list = []
for site_tag in site_soup.findAll('a', href=True):
    tag = site_tag['href']
    parsed_uri = urlparse(tag).netloc
    if parsed_uri != "":
        res_list.append(parsed_uri.split(":")[0])

res_list = list(set(res_list))
res_list = sorted(res_list)
for site in res_list:
    print(site)



