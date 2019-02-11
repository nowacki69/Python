# Beautiful Soup Documentation
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# Import the BeautifulSoup library
from bs4 import BeautifulSoup


print("Tag")
print()
print("1. A Tag object corresponds to an XML or HTML tag in the original document:")
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', "html.parser")
tag = soup.b
print(f"   type(tag): {type(tag)}")		# <class 'bsr.element.Tag'>
print()

print("Name")
print("1. Every tag has a name, accessible as .name:")
print(f"   tag.name: {tag.name}")
print("2. If you change a tag’s name, the change will be reflected in any HTML markup")
print("   generated by Beautiful Soup:")
print()
tag.name = "blockquote"
print("   tag.name = 'blockquote'")
print(f"   tag: {tag}")				# <blockquote class="boldest">Extremely bold</blockquote>
print()

print("Attributes")
print('1. A tag may have any number of attributes. The tag <b id="boldest"> has an')
print('   "attribute “id” whose value is “boldest”.')
print("   You can access a tag’s attributes by treating the tag like a dictionary:")
print()
soup = BeautifulSoup('<b id="boldest">Extremely bold</b>', "html.parser")
tag = soup.b
print(f"tag['id']: {tag['id']}")		# 'boldest'
print()
print("2. You can access that dictionary directly as .attrs:")
print()
print(f"   tag.attrs: {tag.attrs}")		# {'id': 'boldest'}
print()


print("3. You can add, remove, and modify a tag’s attributes. Again, this is done by")
print("   treating the tag as a dictionary:")
print()
tag['id'] = 'verybold'
tag['another-attribute'] = 1
print(f"   tag: {tag}")				# <b another-attribute="1" id="verybold"></b>
print()

del tag['id']
del tag['another-attribute']
print(f"   tag: {tag}")						# <b></b>
print()
print("4. Since we deleted the 'id' above, the following will produce a KeyError:")
print("   print(tag['id']): KeyError 'id'")
print()
print(f"   tag.get('id'): {tag.get('id')}")	#None
print()
print()
print()


print("Multi-valued attributes")
print("1. HTML 4 defines a few attributes that can have multiple values. HTML 5 removes a couple of them,")
print("   but defines a few more. The most common multi-valued attribute is class (that is, a tag can have")
print("   more than one CSS class). Others include rel, rev, accept-charset, headers, and accesskey.")
print("   Beautiful Soup presents the value(s) of a multi-valued attribute as a list:")
print()
print("""   css_soup = BeautifulSoup('<p class="body"></p>', 'html.parser')""")
css_soup = BeautifulSoup('<p class="body"></p>', 'html.parser')
print(f"   css_soup.p['class']: {css_soup.p['class']}")			# ["body"]
print()
print("""2.  css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser')""")
css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser')
print(f"   css_soup.p['class']: {css_soup.p['class']}")			# ["body", "strikeout"]
print()
print("3. If an attribute looks like it has more than one value, but it’s not a multi-valued")
print("   attribute as defined by any version of the HTML standard, Beautiful Soup will leave")
print("   the attribute alone:")
print()
print("""   id_soup = BeautifulSoup('<p id="my id"></p>', 'html.parser')""")
id_soup = BeautifulSoup('<p id="my id"></p>', 'html.parser')
print(f"   id_soup.p['id']: {id_soup.p['id']}")				# 'my id'
print()

print("4. When you turn a tag back into a string, multiple attribute values are consolidated:")
print("""   rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>','html.parser')""")
rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>','html.parser')
print()
print(f"   rel_soup.a['rel']:   {rel_soup.a['rel']}")			# ['index']
print("   rel_soup.a['rel'] = ['index', 'contents']")
rel_soup.a['rel'] = ['index', 'contents']
print()
print(f"   rel_soup.p: {rel_soup.p}")					# <p>Back to the <a rel="index contents">homepage</a></p>
print()

print("5. You can use `get_attribute_list to get a value that’s always a list, string,")
print("   whether or not it’s a multi-valued atribute")
print()
print(f"   id_soup.p.get_attribute_list('id'): {id_soup.p.get_attribute_list('id')}")	# [“my id”]
print()
# print("6. If you parse a document as XML, there are no multi-valued attributes:")
# print("""  xml_soup = BeautifulSoup('<p class="body strikeout"></p>','xml')""")
# xml_soup = BeautifulSoup('<p class="body strikeout"></p>','xml')
# # print(f"   {xml_soup.p['class']}")			# u'body strikeout'
print()


print("NavigableString")
print()
print("1. A string corresponds to a bit of text within a tag. Beautiful Soup uses the")
print("   NavigableString class to contain these bits of text:")
print("")
print(f"   tag.string: {tag.string}")						# u'Extremely bold'
print(f"   type(tag.strinng){type(tag.string)}")				# <class 'bs4.element.NavigableString'>
print()
print()
print("2. A NavigableString is just like a Python Unicode string, except that it also")
print("   supports some of the features described in Navigating the tree and Searching")
print("   the tree. You can convert a NavigableString to a Unicode string with unicode():")
print("   Python 3 renamed the unicode type to str, the old str type has been replaced by bytes.")
print()
print("   unicode_string = str(tag.string)")
unicode_string = str(tag.string)
print(f"   unicode_string: {unicode_string}")				# 'Extremely bold'
print(f"   type(unicode_string): {type(unicode_string)}")			# <class 'str'>
print()
print("   You can’t edit a string in place, but you can replace one string with another,")
print("   using replace_with():")
print()
print('   tag.string.replace_with("No longer bold")')
tag.string.replace_with("No longer bold")
print(f"   tag: {tag}")							# <blockquote>No longer bold</blockquote>
print()
print()
print("The BeautifulSoup object itself represents the document as a whole. For most")
print("purposes, you can treat it as a Tag object. This means it supports most of")
print("the methods described in Navigating the tree and Searching the tree.")
print()
print("Since the BeautifulSoup object doesn’t correspond to an actual HTML or XML")
print("tag, it has no name and no attributes. But sometimes it’s useful to look at")
print('its .name, so it’s been given the special .name “[document]”')
print()
print()
print("BeautifulSoup")
print()
print(f"   soup.name: {soup.name}")								# [document]
print()
print()

print("Comments and other special strings")

print("1. Tag, NavigableString, and BeautifulSoup cover almost everything you’ll see")
print("   in an HTML or XML file, but there are a few leftover bits. The only one")
print("   you’ll probably ever need to worry about is the comment:")
print()
print('   markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"')
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
print("   soup = BeautifulSoup(markup, 'html.parser')")
soup = BeautifulSoup(markup, 'html.parser')
print("   comment = soup.b.string")
comment = soup.b.string
print()
print(f"   type(comment): {type(comment)}")					# <class 'bs4.element.Comment'>
print()
print()
print("The Comment object is just a special type of NavigableString:")
print()
print(f"   comment: {comment}")							# u'Hey, buddy. Want to buy a used parser'
print()
print("But when it appears as part of an HTML document")
print("a Comment is displayed with special formatting:")
print()
print(f"   soup.b.prettify(): {soup.b.prettify()}")		# <b>
    													#  <!--Hey, buddy. Want to buy a used parser?-->
    													# </b>
print()

print("Beautiful Soup defines classes for anything else that might show up in an")
print("XML document: CData, ProcessingInstruction, Declaration, and Doctype. Just")
print("like Comment, these classes are subclasses of NavigableString that add")
print("something extra to the string. Here’s an example that replaces the comment")
print("with a CDATA block:")
print()
print("""
    from bs4 import CData
    cdata = CData("A CDATA block")
    comment.replace_with(cdata)
    print(soup.b.prettify())
""")
from bs4 import CData
cdata = CData("A CDATA block")
comment.replace_with(cdata)
print(soup.b.prettify())    # <b>
                            #  <![CDATA[A CDATA block]]>
                            # </b>
print()
print()
print()
# # Navigating the tree
# # Here’s the “Three sisters” HTML document again:
# print("Navigation the tree")
#
# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="story">...</p>
# """
#
# soup = BeautifulSoup(html_doc, 'html.parser')
#
# # I’ll use this as an example to show you how to move from one part of a
# # document to another.
#
# # Going down
# print("Going down")
#
# # Tags may contain strings and other tags. These elements are the tag’s
# # children. Beautiful Soup provides a lot of different attributes for
# # navigating and iterating over a tag’s children.
#
# # Note that Beautiful Soup strings don’t support any of these attributes,
# # because a string can’t have children.
#
# # Navigating using tag names
# print('1. Using tag names:')
# # The simplest way to navigate the parse tree is to say the name of the tag
# # you want. If you want the <head> tag, just say soup.head:
# print(f"a.  {soup.head}")					# <head><title>The Dormouse's story</title></head>
# print(f"b.  {soup.title}")					# <title>The Dormouse's story</title>
# print()
#
# # You can do use this trick again and again to zoom in on a certain part of
# # the parse tree. This code gets the first <b> tag beneath the <body> tag:
# print(f"2. {soup.body.b}")					# <b>The Dormouse's story</b>
#
# # Using a tag name as an attribute will give you only the first tag by that name:
# print(f"3. {soup.a}")		# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
#
# # If you need to get all the <a> tags, or anything more complicated than the
# # first tag with a certain name, you’ll need to use one of the methods
# # described in Searching the tree, such as find_all():
#
# print(f"4. {soup.find_all('a')}")	# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# 							#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# 							#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
#
# print()
# print()
#
# # .contents and .children
# print(".contents AND .children")
#
# # A tag’s children are available in a list called .contents:
# head_tag = soup.head
# print("soup.head")
# print(f"1. {head_tag}")				# <head><title>The Dormouse's story</title></head>
# print()
# print("soup.head.contents")
# print(f"2. {head_tag.contents}")	# [<title>The Dormouse's story</title>]
# print()
# title_tag = head_tag.contents[0]
# print("soup.head.contents[0]")
# print(f"3. {title_tag}")			# <title>The Dormouse's story</title>
# print()
# print("soup.head.contents.contents")
# print(f"4. {title_tag.contents}")	# [u'The Dormouse's story']
# print()
#
# # The BeautifulSoup object itself has children. In this case, the <html> tag
# # is the child of the BeautifulSoup object.:
# print("The BeautifulSoup object")
# print(f"Len(soup.contents) = {len(soup.contents)}")				# 1
# print(f"soup.contents[0] = {soup.contents[0].name}")	# None
# print(f"soup.contents[1] = {soup.contents[1].name}")	# 'html'
# print()
#
# # # A string does not have .contents, because it can’t contain anything:
# # text = title_tag.contents[0]
# # print(text.contents)			# AttributeError: 'NavigableString' object has no attribute 'contents'
#
# # Instead of getting them as a list, you can iterate over a tag’s children
# # using the .children generator:
# print("Iterating over a tag's children with .children")
# for child in title_tag.children:
#     print(child)					# The Dormouse's story
# print()
# print()
#
#
# # .descendants
# # The .contents and .children attributes only consider a tag’s direct children.
# # For instance, the <head> tag has a single direct child– the <title> tag:
# print(head_tag.contents)			# [<title>The Dormouse's story</title>]
#
# # But the <title> tag itself has a child: the string “The Dormouse’s story”.
# # There’s a sense in which that string is also a child of the <head> tag.
# # The .descendants attribute lets you iterate over all of a tag’s children,
# # recursively: its direct children, the children of its direct children,
# # and so on:
# for child in head_tag.descendants:
#     print(child)					# <title>The Dormouse's story</title>
# 									# The Dormouse's story
# print()
#
# # The <head> tag has only one child, but it has two descendants: the <title> tag
# # and the <title> tag’s child. The BeautifulSoup object only has one direct
# # child (the <html> tag), but it has a whole lot of descendants:
# print("len(list(soup.children))")
# print(len(list(soup.children)))		# 2
# print("len(list(soup.descendants))")
# print(len(list(soup.descendants)))	# 25
# print()
#
#
# # .string
#
# # If a tag has only one child, and that child is a NavigableString, the child
# # is made available as .string:
# print("title_tag.string")
# print(title_tag.string)		# u'The Dormouse's story'
# print()
#
# # If a tag’s only child is another tag, and that tag has a .string, then the
# # parent tag is considered to have the same .string as its child:
# print("head_tag.contents")
# print(head_tag.contents)	# [<title>The Dormouse's story</title>]
# print()
# print("head_tag.string")
# print(head_tag.string)		# u'The Dormouse's story'
# print()
#
# # If a tag contains more than one thing, then it’s not clear what .string
# # should refer to, so .string is defined to be None:
# print("print(soup.html.string)")
# print(soup.html.string)			# None
# print()
#
#
# # .strings and stripped_strings
#
# # If there’s more than one thing inside a tag, you can still look at just the
# # strings. Use the .strings generator:
#
# for string in soup.strings:
#     print(repr(string))
# # u"The Dormouse's story"
# # u'\n\n'
# # u"The Dormouse's story"
# # u'\n\n'
# # u'Once upon a time there were three little sisters; and their names were\n'
# # u'Elsie'
# # u',\n'
# # u'Lacie'
# # u' and\n'
# # u'Tillie'
# # u';\nand they lived at the bottom of a well.'
# # u'\n\n'
# # u'...'
# # u'\n'
