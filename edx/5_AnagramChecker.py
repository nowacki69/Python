#Write a function called are_anagrams. The function should
#have two parameters, a pair of strings. The function should
#return True if the strings are anagrams of one another,
#False if they are not.
#
#Two strings are considered anagrams if they have only the
#same letters, as well as the same count of each letter. For
#this problem, you should ignore spaces and capitalization.
#
#So, for us: "Elvis" and "Lives" would be considered
#anagrams. So would "Eleven plus two" and "Twelve plus one".
#
#Note that if one string can be made only out of the letters
#of another, but with duplicates, we do NOT consider them
#anagrams. For example, "Elvis" and "Live Viles" would not
#be anagrams.


#Write your function here!
def are_anagrams(string1, string2):
    characters = {}
    for char in string1.lower():
        if char in characters:
            characters[char] += 1
        else:
            if char == ' ': continue
            characters[char] = 1

    for char in string2.lower():
        if char in characters:
            characters[char] -= 1
            if characters[char] < 0: return False
        else:
            if char == ' ': continue
            return False

    sum = 0
    for value in characters.values():
        sum += value

    if value != 0:
        return False
    else:
        return True


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, False, True, False, each on their own line.
print(are_anagrams("Elvis", "Lives"))
print(are_anagrams("Elvis", "Live Viles"))
print(are_anagrams("Eleven plus two", "Twelve plus one"))
print(are_anagrams("Nine minus seven", "Five minus three"))
print(are_anagrams("Belgium", "Big Mule"))
