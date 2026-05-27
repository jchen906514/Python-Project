#Jiaying
#A simulation of the popular madlibs game where silly stories are generated using input from the player

#init
import random
#functions

def random_word(word_type):
    word = {"adjective": ["fluffy", "sticky", "loud", "sparkling", "ancient"], "noun":["banana", "spaceship", "potato", "robot", "castle"], "verb": ["jiggle", "sprint", "slap", "whisper", "float"]}
    return random.choice(word.get(word_type, ["word"]))

def madlibs():
    print("Welcome to the Python Mad Libs Game!")
    print("We'll ask you for a few words to complete a silly story.")
    print("If you're stuck, just type 'random' and we'll pick a word for you!")
    user_noun = input("Enter a noun (e.g., table): ")
    if user_noun == 'random':
        user_noun = random_word("noun")
    user_verb = input("Enter a verb (e.g., run): ")
    if user_verb == 'random':
        user_verb = random_word("verb")
    user_adjective_1 = input("Enter an adjective (e.g., happy): ")
    if user_adjective_1 == 'random':
        user_adjective_1 = random_word("adjective")
    user_adjective_2 = input("Enter another adjective (e.g., smelly): ")
    if user_adjective_2 == 'random':
        user_adjective_2 = random_word("adjective")

    final_noun = user_noun.upper()
    final_verb = user_verb.upper()
    final_adjective_1 = user_adjective_1.upper()
    final_adjective_2 = user_adjective_2.upper()

    story = f"Once upon a time, a \033[1m{final_adjective_1} {final_noun}\033[0m decided to learn how to \033[1m{final_verb}\033[0m. It practiced every day, even when things got \033[1m{final_adjective_2}\033[0m. Eventually, it became a master!"
    print(story)

#main
madlibs()
