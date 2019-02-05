from random import choice

def eat(food, is_healthy):
    if not isinstance(is_healthy, bool):
        raise ValueError("is_healthy must be a boolean")

    ending = "because YOLO"
    if is_healthy:
        ending = "because my body is a temple."
    return f"I'm eating {food}, {ending}"


def nap(nap_hours):
    if nap_hours <= 2:
        return "I'm feeling refreshed after my 1 hour nap"
    return f"Ugh, I overslept. I didn't mean to nap for {nap_hours} hours"


def is_funny(name):
    if name is 'tim': return False
    return f"{name} should be funny"


def laugh():
    return choice(('lol', 'haha', 'tehehe'))
