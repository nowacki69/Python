# Write a function called revers_vowels. This function should revers the vowels in a string. Any
# characters which are not vowels should remain in their original position. You should not
# consider "y" to be a vowel.
def reverse_vowels(string):
    aList = list(string)
    vowels = []
    new_string = []

    for char in string:
        if char.lower() in 'aeiou': vowels.append(char)

    vowel_index = -1
    for char in string:
        if char.lower() in 'aeiou':
            new_string.append(vowels[vowel_index])
            vowel_index -= 1
        else:
            new_string.append(char)

    return "".join(new_string)


print(reverse_vowels("Hello!"))                             # "Holle!"
print(reverse_vowels("Tomatoes"))                           # "Temotaos"
print(reverse_vowels("Reverse Vowels In A String"))         # "RivArsI Vewols en e Streng"
print(reverse_vowels("aeiou"))                              # "uoiea"
print(reverse_vowels("why try, shy fly?"))                  # "why try, shy fly?"
