# Suppose we're createing a social network application where users can comment on posts and photosself.
# Create a class called  Comment. Each comment shold have the following attributes:
# - username - the username of the person who created the comment.
# - text - the actual comment itself.
# - likes - the number of likes the comment has. (Likes should default to 0).


class Comment():
    def __init__(self, username, text, likes = 0):
        self.username = username
        self.text = text
        self.likes = likes


c = Comment("davey123", "lol you're so silly", 3)
c2= Comment("nowacki69", "Eat 'em up!")

print(f"{c.username} has {c.likes} likes with {c.text}")
print(f"{c2.username} has {c2.likes} likes with {c2.text}")
