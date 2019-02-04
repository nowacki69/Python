from random import choice
# Inner functions can access outer function's scope
def make_laugh_at_func(person):
    def get_laugh():
        laugh = choice(('HAHAHAHA','lol','teehehehe'))
        return f"{laugh} {person}"

    return get_laugh

laugh_at = make_laugh_at_func("Chrissy")

print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())
