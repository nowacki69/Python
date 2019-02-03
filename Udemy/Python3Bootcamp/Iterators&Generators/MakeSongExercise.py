# Write a function called make_song, which takes a count and a beverage, and returns a generator that yields versus
# from a popular song about the beverage. The number of verses in the song is determined by the count

# Each vers of the song should involve one fewer beverage, until there are no beverages remaining

# Te default count should be 99 and the default beverage should be soda

def make_song(count = 99, beverage = "soda"):
    while True:
        if count > 1:
            msg = "{} bottles of {} on the wall.".format(count, beverage)
        elif count == 1:
            msg = "Only {} bottle of {} left!".format(count, beverage)
        elif count == 0:
            msg = "No more {}!".format(beverage)
        else:
            raise StopIteration

        yield msg
        count -= 1

# kombucha_song = make_song(5, "kombucha")
# print(next(kombucha_song)) # '5 bottles of kombucha on the wall.'
# print(next(kombucha_song)) # '4 bottles of kombucha on the wall.'
# print(next(kombucha_song)) # '3 bottles of kombucha on the wall.'
# print(next(kombucha_song)) # '2 bottles of kombucha on the wall.'
# print(next(kombucha_song)) # 'Only 1 bottle of kombucha left!'
# print(next(kombucha_song)) # 'No more kombucha!'
# print(next(kombucha_song)) # StopIteration

default_song = make_song()
print(next(default_song)) # '99 bottles of soda on the wall.'
