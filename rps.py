import random


def is_valid_play(play):
    return play in ['rock', 'paper', 'scissors']


def random_play():
    return random.choice(['rock', 'paper', 'scissors'])


def determine_game_result(human, computer):
    """Retuns str with human, computer or tie"""
    if human == computer:
        return 'tie'
    elif human+computer in 'rockpaperscissorsrock':
        return 'computer'
    else:
        return 'human'


def main():
    human = ''
    while not is_valid_play(human):
        human = input('rock, paper or scissors? ')

    computer = random_play()

    print(computer)

    result = determine_game_result(human, computer)
    if result == 'tie':
        print('it\'s a tie!')
    else:
        print(result, 'wins')

if __name__ == '__main__':
    main()























