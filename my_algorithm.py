# TODO: Here you should write the algorithm that your peer explain to you

#czwartek, 17:00
from os import system, name
from time import sleep
from random import choice

from textwrap import dedent

def cls() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def random_user_id(username: str) -> int:
    return random(1,6)

def question (question: str = "Type rather \'y\': ") -> str:
    user_input = input(question)
    while user_input.lower() in ['y','n']:
        user_input = input(question)
    
    return (user_input == 'y')



def main():
    username = ""
    user_id = 0

    round_score_count = 0
    scores = [0,0]
    score_to_reach = 100

    actual_winner = False

    cls()
    print("Game is starting\n")
    
    while not actual_winner:
        player_name = f"{user_id+1}"
        cube_side = random_user_id(player_name)
        if cube_side == 1:
            print(f"{player_name} threw out {cube_side}. You've lost your {round_score_count}. You're staying at: {scores[user_id]}")
            round_score_count = 0
            actual_winner = 0 if actual_winner == 1 else 1
            continue
        round_score_count += cube_side
        print(f"{player_name} you've threw out: {cube_side}")

        actual_winner = (score_to_reach <= scores[user_id] + round_score_count)
        if not actual_winner:
            do_you_want_throw_again = dedent(f"Your score is: {score[user_id]}.\n Your score at this round is: {round_score_count} \n Do you like to threw cube again?")
            thrown_again = question(do_you_want_throw_again)
            cls()
            if not thrown_again:
                print(f"Your actual score is: {score[user_id]}")
                score[user_id] += round_score_count
                round_score_count = 0
                actual_winner = 0 if actual_winner == 1 else 1

    print(f"{user_id} is winner")
    
if __name__ == '__main__':
    main()