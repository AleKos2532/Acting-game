import random as r

def new_game(action_list: list, people_list: list):
    """
    This function starts a new game and choses a person and an action,
    the rest of the people will be asigned a number based on the performance
    the acting should have.

    Args:
        action_list (list): A list with the actions.
        people_list (list): A list with the people playing.
    """    
    chosen_action = r.choice(actions)
    chosen_person = r.choice(people)
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


def add_people():
    """
    This functions adds new people to the party.
    """    
    while True:
        name = input("Insert a name: ")
        if name.lower().strip() in ['d', 'no']:
            break
        else:
            people.append(name)
            print("Wan't to add another player?")


def replay():
    replay_prompt = 'Do you wan\'t to play again?'
    replay_prompt += '\nType "yes" or "no".'
    print(replay_prompt)
    play_again = input().lower().strip()
    if play_again == "yes":
        new_game(actions, people[:])
    elif play_again in ['no', '']:
        print("Thanks for playing.")
    else:
        replay()


# The list of people and actions
actions = [
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


# Game running

intro_prompt = "Welcome to the game, please enter a name."
intro_prompt += "\nOnce you're done type \"d\"."
print(intro_prompt)

add_people()

new_game(actions, people[:])