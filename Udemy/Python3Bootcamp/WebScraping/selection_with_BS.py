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
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# find an element with an id of foo
soup.find(id="#first")
soup.select("#first")             # Select always returns a list, use [0] to return a string instead
soup.select("#first")[0]

# find all elements with a class of bar
# careful! "class" is a reserved word in Python
soup.find_all(class_="special")
soup.select(".special")

# find all elements with a data attribute of "data-example"
# using the general attrs kwarg
soup.find_all(attrs={"data-example": True})
soup.select("[data-example]")
