from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special super-special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
el = soup.select(".special")[0]
print(el.get_text())

print()
for el in soup.select(".special"):
    print(el.get_text())

print()
for el in soup.select(".special"):
    print(el.name)
    print(el.attrs)

attr = soup.find("h3")["data-example"]
print(attr)
print()

attr = soup.find("div")
print(attr)
print()

attr = soup.find("div")["id"]
print(attr)
print()
