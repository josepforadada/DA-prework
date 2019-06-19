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

while is_a_number == 0:
        try:
            option_game = int(option_game)
            is_a_number = 1
            if not 1 <= option_game <= 2:
                option_game = input("\nPlease, select with number 1 or 2")
        except:
            option_game = input("\nPlease, select the game using numbers: ")

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

    0: "This round is a draw.",
    1: "User wins the round",
    2: "Machine wins the round"
}

print("\nThe game will start... the winner is the first to win %d rounds" % games_number)

def ask_user(num,round):

    print("\n\nROUND %d" % round)
    if num == 1:
        print("\n\t\t1 - Stone\n\t\t2 - Paper\n\t\t3 - Scissors")
        return input("\n\t\tSelect an option: ")
    else:
        (print("\n\t\t1 - Stone\n\t\t2 - Paper\n\t\t3 - Scissors\n\t\t4 - Lizard\n\t\t5 - Spock"))
        return input("\n\t\tSelect an option: ")

def machine_choice(num):

    if num == 1:
        return random.randint(1, 3)
    else:
        return random.randint(1,5)


def compare(user,machine,num):
     print(user)
     print(machine)
     print(num)
     while user == 1:
        if machine == 1:
            # 0 = Draw, # 1 = Win # 2 = Loose
            return (0)
        if machine == 2:
            return (2)
        if machine == 3:
            return (1)
        if num == 5:
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
        if num == 5:
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
        if num == 5:
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
        if num == 5:
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
        if num == 5:
            if machine == 4:
                return (2)
            else:
                return (0)

while user_win < 5 and mach_win < 5:

    election = ask_user(option_game,1)

    print("\nUser's choice: %s\t\tMachine's choice: %s" % (game_options[int(election)].upper(), game_options[int(machine_choice(option_game))].upper()))

    val = compare(int(election),machine_choice(option_game),option_game)

    print(game_results[val])

print("THE GAME IS OVER")
