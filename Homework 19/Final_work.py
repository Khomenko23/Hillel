import random
from enum import IntEnum


class Choice(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4


victories = {
    Choice.Rock: [Choice.Lizard, Choice.Scissors],
    Choice.Scissors: [Choice.Lizard, Choice.Paper],
    Choice.Paper: [Choice.Spock, Choice.Rock],
    Choice.Lizard: [Choice.Spock, Choice.Paper],
    Choice.Spock: [Choice.Scissors, Choice.Rock]
}


def get_user_choice():
    choices = [f"{action.name}[{action.value}]" for action in Choice]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Choice(selection)
    return action


def computer_choice():
    selection = random.randint(0, len(Choice) - 1)
    action = Choice(selection)
    print(f'Computer choice: {action}')
    return action


def game(user_choice, computer_choice):
    defeats = victories[user_choice]
    if user_choice == program_choice:
        print(f"Both players selected {user_choice.name}. It's a tie!")
    elif computer_choice in defeats:
        print(f"{user_choice.name} beats {computer_choice.name}! You win!")
    else:
        print(f"{computer_choice.name} beats {user_choice.name}! You lose.")


while True:
    try:
        user_choice = get_user_choice()
    except ValueError as error:
        range_str = f"[0, {len(Choice) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue

    program_choice = computer_choice()
    game(user_choice, program_choice)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
