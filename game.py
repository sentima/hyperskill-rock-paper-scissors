import random


def main():
    player_name = input('Enter your name: ')
    print(f'Hello, {player_name}')
    rating = int(get_rating(player_name))
    losing_combo = get_rules(input())
    print("Okay, let's start")
    while True:
        player_chose = player_input_check(rating, losing_combo)
        computer_chose = random.choice(list(losing_combo.keys()))
        rating += game(player_chose, computer_chose, losing_combo)


def get_rules(variants):
    if variants == '':
        return {'scissors': 'rock', 'rock': 'paper', 'paper': 'scissors'}
    options = list(variants.split(','))
    for _ in options:
        options_dict = {key: [] for key in options}
    for item in options:
        if options.index(item) + (len(options) - 1) // 2 < len(options):
            options_dict[item] = options[options.index(item) + 1: options.index(item) + 1 + (len(options) // 2)]
        else:
            weird_list = options[options.index(item) + 1:] + options[: options.index(item) + 1 + (len(options) // 2) - len(options)]
            options_dict[item] = weird_list
    return options_dict


def game(player_chose, computer_chose, losing_combo):
    if player_chose == computer_chose:
        print(f'There is a draw ({player_chose})')
        return 50
    elif computer_chose in losing_combo[player_chose]:
        print(f'Sorry, but the computer chose {computer_chose}')
        return 0
    else:
        print(f'Well done. The computer chose {computer_chose} and failed')
        return 100


def get_rating(player_name):
    with open('rating.txt', 'r') as file:
        file_list = file.readlines()
    for item in file_list:
        if item.split(' ')[0] == player_name:
            return item.split(' ')[1].rstrip('\n')
    return 0


def player_input_check(player_rating, losing_combo):
    while True:
        player_chose = input()
        if player_chose == '!exit':
            print('Bye!')
            exit()
        if player_chose == '!rating':
            print(player_rating)
        elif player_chose in list(losing_combo.keys()):
            return player_chose
        else:
            print('Invalid input')


if __name__ == "__main__":
    main()
