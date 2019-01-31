import requests
#print(dir(requests))
#print(requests.__file__)

url = "https://icanhazdadjoke.com/search"

res = requests.get(
    url,
    headers={"Accept":"application/json"},
    params={'term': "cat"}
)

data = res.json()

print(data['results'])
# print(data['joke'])
# print(f"status: {data['status']}")
