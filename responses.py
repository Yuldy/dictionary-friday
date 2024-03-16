from random import choice, randint


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    # Replace logic later and response algorithm
    if lowered == '':
        return "Well you are awfully silent.."
    elif 'hello' in lowered:
        return "Hello there!"
    elif 'bye' in lowered:
        return "See you!"
    
    else:
        return choice(["I do not understand.", "What did you say?"])