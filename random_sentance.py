import random

def get_random(thing):
    random_word = random.choice(thing)
    return random_word


names = ["Peter", "Sofia", "Michael", "Jane", "Steve"]

places = ["Sofia", "Plovdiv", "Varna", "Burgas"]

verbs = ["eats", "holds", "sees", "plays with", "brings"]

nouns = ["stones", "cake", "apple", "laptop", "bikes"]

adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly"]

details = ["near the river", "at home", "in the park"]

action = "again"

while action != "end" or action != "End":
    print(get_random(names), end= " ")
    print(get_random(places), end= " ")
    print(get_random(verbs), end= " ")
    print(get_random(nouns), end= " ")
    print(get_random(adverbs), end= " ")
    print(f"{get_random(details)}.")
    print(" ")

    print("Type 'end/End' to end program, type 'again' for another random sentance.")

    action = input()
