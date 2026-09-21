import random as r

def main_menu():
    """
    Starts the menu with multiple options.
    """
    print(intro_prompt)
    choice = input().lower()
    if choice in ["1", "1."]:
        start_new_game()
    else:
        print("\nThat's not an option.\n")
        main_menu()


def start_new_game():
    print(name_prompt)
    add_people()
    new_game(actions1, people[:])


def add_people():
    """
    This functions adds new people to the party.
    """    
    while True:
        name = input("Insert a name: ")
        if name.lower().strip() in ['d', 'no', '']:
            break
        else:
            people.append(name)
            print("Wan't to add another player?")


def new_game(action_list: list, people_list: list):
    """
    This function starts a new game and choses a person and an action,
    the rest of the people will be asigned a number based on the performance
    the acting should have.

    Args:
        action_list (list): A list with the actions.
        people_list (list): A list with the people playing.
    """    
    chosen_action = r.choice(action_list)
    chosen_person = r.choice(people_list)
    people_list.remove(chosen_person)

    print(f'\nThe judge is {chosen_person}.')
    print(f'The action is {chosen_action}.')
    input('Continue ')
    print()

    for actor in people_list:
        number = r.randint(1, 10)
        print(f'\t{actor}: {number}')
    input("\nContinue ")
    replay()


def replay():
    print(replay_prompt)
    play_again = input().lower().strip()
    if play_again == "yes":
        new_game(actions1, people[:])
    elif play_again in ['no', '']:
        print("Thanks for playing.")
    else:
        replay()


# The list of people and actions
actions1 = [
    'Flying',
    'Diving',
    'Swimming',
    'Smell flowers',
    'Paracaidism',
    # 'Bungee jump',
    'Horse riding',
    'Eating a slice of pizza',
    # 'Hitting someone',
    'Playing the piano',
    'Going to the beach',
    'Going to a fair',
    'Going to the zoo',
    'Going to an amusement park',
    'Deliver a package',
    'Getting shot',
    'Doing Yoga',
    'Go camping',
    'Take care of a baby',
    'Play a sport',
    'Go buy something',
    'Running a marathon',
    'To climb',
    'To measure an object',
    'Fishing',
    'To fix something',
    'Sleep',
    'To shower',
    'To cook',
    'To dig',
    'Gardening',
    'Defuse a bomb',
    'Get on a rocket',
    'Drive',
    'Pass the street',
    'Playing with a dog',
    'Be a spy',
    'Go to the bathroom',
    # 'Make an apology video',

    # 'Doxxear a alguien',
    # 'Suplantación de identidad',
    # 'María esta a 10km de tí',
    # 'Uso de IA generativa',
    # 'Robar ideas de otros creadores',
    # 'Broma salió mal',
    # 'Fake info',
    # 'Hacer trampa en un juego',
    # 'Abandono de amigos',
    ]
    
people = []

# Constants and texts
choice = ""

intro_prompt = "Welcome to the acting game, please choose an option."
intro_prompt += "\n1. New game"
intro_prompt += "\n2. Instructions (coming soon)"
intro_prompt += "\n3. Options (coming soon)"

name_prompt = "\nPlease enter a name"
name_prompt += "\nOnce you're done type \"d\"."

replay_prompt = 'Do you wan\'t to play again?'
replay_prompt += '\nType "yes" or "no".'

# Game running

main_menu()
