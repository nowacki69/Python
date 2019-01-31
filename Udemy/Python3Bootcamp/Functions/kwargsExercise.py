# **kwargs Exercise

# for this exercise, make use of **kwargs; no default parameters allowed!

# Write a runction called combine_words which accpts a single string called word
# and a number of additional key word arguments. If a prefix is provided, return
# the prefixfollowd by the word. If a suffix is provided, return the word
# followed by the suffix. If neither is provided, just return the word. It might
# sound confusing, but the examples should make this a lot clearer!

def combine_words(word, **kwargs):
    if len(kwargs) == 0:
        return word

    for ext, addon in kwargs.items():
        if ext == 'prefix':
            return addon + word
        elif ext == 'suffix':
            return word + addon

def comine2(word, **kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word


print(combine_words("child"))               # child
print(combine_words("child", prefix="man")) # manchild
print(combine_words("child", suffix="ish")) # childish
print(combine_words("work", suffix="er"))   # worker
print(combine_words("work", prefix="home")) # homework
print()
print(comine2("child"))               # child
print(comine2("child", prefix="man")) # manchild
print(comine2("child", suffix="ish")) # childish
print(comine2("work", suffix="er"))   # worker
print(comine2("work", prefix="home")) # homework
