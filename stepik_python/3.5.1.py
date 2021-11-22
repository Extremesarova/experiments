import requests

params = {
    "json": True
}

with open("python/3.5.1_input.txt", "r") as f:
    for number in f:
        api_url = f"http://numbersapi.com/{int(number)}/math"
        res = requests.get(api_url, params=params)
        is_found = res.json()['found']
        if is_found:
            print("Interesting")
        else:
            print("Boring")