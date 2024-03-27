from random import choice, randint

# PROJECT FRIDAY:
def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()


    # CURRENTLY SIMPLE IF AND ELSE CHECK STATEMENTS
    # Replace logic later and response algorithm
    if lowered.startswith('/'):
        # Removes the leading '/':
        command = lowered[1:]

        if len(command) == 0 or command == '':
            return "Invalid command. Nothing was inputted."
        


        # if lowered == '':
        #     return "Well you are awfully silent.."
        # elif 'hello' in lowered:
        #     return "Hello there!"
        # elif 'bye' in lowered:
        #     return "See you!"
        
        # else:
        #     return choice(["I do not understand.", "What did you say?"])
    

#def print_menu() -> str:
