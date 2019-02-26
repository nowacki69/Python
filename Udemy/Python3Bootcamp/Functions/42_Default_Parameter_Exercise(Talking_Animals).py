# Write a function called speak that accepts a single parameter, animal.
#   - If animal is 'pig', it should return 'oink'
#   - If animal is 'duck', it should return 'quack'
#   - If animal is 'cat', it should return 'meow'
#   - If animal is 'dog', it should return 'woof'
#   - If animal is anything else, it should return '?'
#   - If no animal is specified, it should default to 'dog'

def speak(animal = 'dog'):
    noises = {
        'pig':'oink',
        'duck':'quack',
        'cat':'meow',
        'dog':'woof'
    }

    noise = noises.get(animal)
    if noise:
        return noise
    return "?"
