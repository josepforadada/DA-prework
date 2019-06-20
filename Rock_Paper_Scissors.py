print("\t\nROCK PAPER SCISSORS (LIZARD, SPOCK\n")

print("Let's play the famous game against our computer:")

print("\nThere are 2 options")

print("\n\t1 - Stone, paper, scissors")
print("\t2 - Stone, paper, scissors, lizard, spock")

option_game = input("\nSelect the game using numbers: ")

is_a_number = 0
is_odd = 0
user_win = 0
mach_win = 0
draws = 0

while is_a_number == 0:
        try:
            option_game = int(option_game)
            is_a_number = 1
            if option_game == 1:
                total_var = 3
            if option_game == 2:
                total_var = 5
            if not option_game == 1 and not option_game == 2:
                option_game = input("\nPlease, select with number 1 or 2: ")
                if not option_game == "1" and not option_game == "2":
                    is_a_number = 0
        except:
            option_game = input("\nPlease, select the game using numbers: ")
            if not option_game == "1" and not option_game == "2":
                    is_a_number = 0

games_number = input("\nSelect the number of game rounds (1, 3, 5...): ")

while is_odd == 0:
         try:
            games_number = int(games_number)
            is_odd = 1
            odd = games_number % 2
            if odd == 0:
                is_odd = 0
                games_number = input("\nPlease, select odd number: ")
         except:
            games_number = input("\nPlease, select the game using numbers: ")


import random, math

game_options = {
    1: "Stone",
    2: "Paper",
    3: "SCissors",
    4: "Lizard",
    5: "Spock"
}

game_results = {

    0: "\nThis round is a draw.",
    1: "\nUser wins the round",
    2: "\nMachine wins the round"
}
print("\n-------------------------------------------------")
print("\nThe game will start... the winner is the first to win %d rounds" % games_number)

def ask_user(num,round):

    print("\n-------------------------------------------------")
    print("\nROUND %d" % round)

    print("\n\n**** press Q to quit the game ****")
    if num == 1:
        print("\n\t\t1 - Stone\n\t\t2 - Paper\n\t\t3 - Scissors")

        return input("\n\t\tSelect an  option: ")

    if num == 2:
        (print("\n\t\t1 - Stone\n\t\t2 - Paper\n\t\t3 - Scissors\n\t\t4 - Lizard\n\t\t5 - Spock"))

        return input("\n\t\tSelect an option: ")

def machine_choice(num):

    if num == 1:
        return random.randint(1, 3)
    else:
        return random.randint(1,5)


def compare(user,machine,num):

     while user == 1:
        if machine == 1:
            # 0 = Draw, # 1 = Win # 2 = Loose
            return (0)
        if machine == 2:
            return (2)
        if machine == 3:
            return (1)
        if num == 2:
            if machine == 4:
                return (1)
            else:
                return (2)
     while user == 2:
        if machine == 1:
            # 0 = Draw, # 1 = Win # 2 = Loose
            return (1)
        if machine == 2:
            return (0)
        if machine == 3:
            return (2)
        if num == 2:
            if machine == 4:
                return (2)
            else:
                return (1)
     while user == 3:
        if machine == 1:
            # 0 = Draw, # 1 = Win # 2 = Loose
            return (2)
        if machine == 2:
            return (1)
        if machine == 3:
            return (0)
        if num == 2:
            if machine == 4:
                return (1)
            else:
                return (2)
     while user == 4:
        if machine == 1:
            # 0 = Draw, # 1 = Win # 2 = Loose
            return (2)
        if machine == 2:
            return (1)
        if machine == 3:
            return (2)
        if num == 2:
            if machine == 4:
                return (0)
            else:
                return (1)
     while user == 5:
        if machine == 1:
            # 0 = Draw, # 1 = Win # 2 = Loose
            return (1)
        if machine == 2:
            return (2)
        if machine == 3:
            return (1)
        if num == 2:
            if machine == 4:
                return (2)
            else:
                return (0)
round = 1
election_possible = "None"

total_games = 1
exit = 0

while user_win < games_number and mach_win < games_number:

    while election_possible == "None":

        election = ask_user(int(option_game),round) # si no es int donava error

        try:
            election_possible = str(game_options.get(int(election)))

            if int(election) == 0 or int(election) > total_var:
                print("\nPLEASE ENTER A VALID NUMBER")
                election_possible = "None"
        except:
            if str(election) == "Q" or str(election) == "q":
                exit = 1
                break
            print("\nPLEASE ENTER A VALID NUMBER")
            election_possible = "None"

    if exit == 1:
        break
    election_machine = machine_choice(option_game)
    print("\nUser's choice: %s\t\tMachine's choice: %s" % (game_options[int(election)].upper(), game_options[int(election_machine)].upper()))

    val = compare(int(election),int(election_machine),int(option_game))

    print(game_results[val].upper())
    if val == 1:
        user_win += 1
    elif val == 2:
        mach_win += 1
    else:
        draws += 1
    print("\n\t\tTotal user's wins: %d\n\t\tTotal machine's wins: %d\n\t\tTotal draws: %d" % (user_win,mach_win,draws))
    round += 1
    total_games += 1
    election_possible = "None"
    exit = 0

print("-------------------------------------------------")
print("-------------------------------------------------")

if user_win == games_number:
    print("\n\t\tTHE GAME IS OVER, USER WINS")
elif mach_win == games_number:
    print("\n\t\tTHE GAME IS OVER, MACHINE WINS")
else:
    print("\n\t\tYOU EXIT THE GAME")
print("\n-------------------------------------------------")
