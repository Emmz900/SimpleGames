import random

rolls = {
    'rock': {
        'defeats': ['scissors'],
        'defeated_by': ['paper'],
    },
    'paper': {
        'defeats': ['rock'],
        'defeated_by': ['scissors'],
    },
    'scissors': {
        'defeats': ['paper'],
        'defeated_by': ['rock'],
    },
}


def main():
    show_header()
    play_game("You", "Computer")


def show_header():
    print("-----------------------------------")
    print("       Rock Paper Scissors")
    print("       Data Upgrade Edition")
    print("-----------------------------------")


def find_winner(wins, names):
    best_of = 3
    for name in names:
        if wins.get(name, 0) >= best_of:
            return name
    return None


def play_game(player_1, player_2):
    wins = {player_1: 0, player_2: 0}

    roll_name = list(rolls.keys())

    while not find_winner(wins, wins.keys()):
        roll1 = get_roll(player_1, roll_name)
        roll2 = random.choice(roll_name)
        if not roll1:
            print("Can't play that, try again.")
            continue

        print(f"{player_1} roll {roll1}")
        print(f"{player_2} rolls {roll2}")

        # result
        winner = get_winner(player_1, player_2, roll1, roll2)

        if winner is None:
            print("This round was a tie!")
        else:
            print(f"The winner of this round is {winner}!")
            wins[winner] += 1
        print(f"Score is {player_1}: {wins[player_1]} and {player_2}: {wins[player_2]}")
        print()

    overall_winner = find_winner(wins, wins.keys())
    print(f"The winner is {overall_winner}!")


def get_winner(player_1, player_2, roll1, roll2):
    winner = None
    if roll1 == roll2:
        print('The play was a tie')
    outcome = rolls.get(roll1, {})
    if roll2 in outcome.get('defeats'):
        return player_1
    elif roll2 in outcome.get('defeated_by'):
        return player_2
    return winner


def get_roll(player_name, roll_name):
    print("Available rolls:")
    for index, r in enumerate(roll_name, start=1):
        print(f"{index}. {r}")  # print rolls with number options
    text = input(f"{player_name}, what is your roll? ")
    selected_index = int(text) - 1  # indexes start at 0, numbers start at 1
    if selected_index < 0 or selected_index >= len(rolls):
        print(f"Sorry {player_name}, {selected_index + 1} is not an option!")
        return None
    return roll_name[selected_index]


if __name__ == '__main__':
    main()
