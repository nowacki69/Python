import requests as req

urls = ["http://www.google.com", "http://www.reddit.com"]

for url in urls:
    response = req.get(url)
    print(f"your request to {url} came back w/ status code {response.status_code}")

print()
print("Done!")
