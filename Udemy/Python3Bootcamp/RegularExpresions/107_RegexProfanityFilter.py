# Define a function called censor that accepts a single string. Rather than censoring any real profanity, we're going
# to censor words that start with "frack". This includes "fracking", "fracker", "frack", etc. Replace the entire word
# with the string "CENSORED". Your regex should be case insensitive.
import re

def censor(text):
    pattern = re.compile(r'((frack)[a-z]+)|(frack)', re.IGNORECASE)
    result = pattern.sub("CENSORED", text)
    return(result)

print(censor("Frack you"))                 # "CENSORED you"
print(censor("I hope you fracking die"))   # "I hope you CENSORED die"
print(censor("you fracking frack"))        # "You CENSORED CENSORED"
