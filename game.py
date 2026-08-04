import random as r

actions = [
    'Flying',
    'Diving',
    'Swim',
    'Paracaiding',
    'Bungee jump',
    'Horse riding',
    'Eating a slice of pizza',
    'Hitting Zuri',
    'Playing the piano',
    'Getting shot',
    'Doing Yoga',
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
    'Make an apology video',

    # 'Doxxear a alguien',
    # 'Suplantación de identidad',
    # 'María esta a 10km de tí',
    # 'Uso de IA generativa',
    # 'Robar ideas de otros creadores',
    # 'Broma salió mal',
    # 'Fake info',
    # 'Hcacer trampa en un juego',
    # 'Lily',
    # 'Abandono de amigos',
    ]

people = ['Vik', 'Zuri', 'Alec']

chosen_action = r.choice(actions)
chosen_person = r.choice(people)
people.remove(chosen_person)

print(f'The judge is {chosen_person}.')
print(f'The action is {chosen_action}.')
input('Continue')
print()

for actor in people:
    number = r.randint(1, 10)
    print(f'{actor}: {number}')
