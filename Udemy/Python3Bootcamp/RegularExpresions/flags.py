import re

pat = re.compile(r'^([a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2,6})$')

pattern = re.compile(r"""
    ^                   # Start of line marker
    ([a-z0-9_\.-]+)     # username part of email address
    @                   # single @ sign
    ([0-9a-z\.-]+)      # email provider
    \.                  # single dot
    ([a-z\.]{2,6})      # Type of organizaiont (com, edu, net, etc.)
    $                   # End of word marker
""", re.VERBOSE | re.IGNORECASE)

match = pattern.search("Nowacki69@gmail.com")
print(match.group())
print(match.groups())
