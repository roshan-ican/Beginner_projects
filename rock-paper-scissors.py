import random
import math

def play():
    user = input("Whats your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return (0, user, computer)
    # r > s, s > p, p > r

    if is_win(user, computer):
        return (1, user, computer)

    return (-1, user, computer)

def is_win(player, opponent):
    # return true if the player beats the opponent
    # winning conitions r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

def play_best_of(n):
    # play against the computer until someone wins best of n games
    #to, win you must win ceil(n/2) games (i.e 2/3, 3/5, 4/7)

    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    print(wins_necessary)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()
        #Tie
        if result == 0:
            print("It's a Tie. You and the computer have both chosen {}. \n".format(user))
        elif result == 1:
            player_wins += 1
            print("You chose {} and the computer chose{}. You Won!!!:)\n")
        else:
            computer_wins+= 1
            print("You choose {} and the computer chose{}. You lost :(\n".format(user, computer))
        print("\n")

    if player_wins > computer_wins:
        print('You have won the best of {} games! What a champ :D'.format(n))
    else:
        print("Unfortunately, the computer has won the best out of {} games...:( Better luck next time B")




if __name__== '__main__':
    play_best_of(3)
    play_best_of(5)
    play_best_of(7)

