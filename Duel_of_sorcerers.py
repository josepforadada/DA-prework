print("\nDUEL OF SORCERERS\n")

print("You are witnessing an epic battle between two powerful sorcerers.")
print("Gandalf and Saruman. Each sorcerer has 10 spells of variable power")
print("in their mind and they are going to throw them one after the other.")
print("The winner of the duel will be the one who wins more of those")
print("clashes between spells. Spells are represented as a list of 10")
print("integers whose equals the power of the spell.\n")
print("Gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]")
print("Saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]\n")
print("For example:\n")
print("You will create two variables, one for each sorcerer, where the")
print("sum of clashes won will be stored. Depending on which variable is")
print("greater at the end of the duel, you will show one of the following")
print("three results on the screen:\n")
print("\t - Gandalf wins")
print("\t - Saruman wins")
print("\t - Tie\n")


clash_list = []
Num_of_clashes = 0
Round_of_clashes = 0
Gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
Saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]
Name_of_round = {
    0: "First",
    1: "Second",
    2: "Third",
    3: "Fouth",
    4: "Fifth",
    5: "Sixth",
    6: "Seventh",
    7: "Eigth",
    8: "Ninth",
    9: "Tenth"
}
sorcerer = "Saruman"
gandalf_wins = 0
saruman_wins = 0
draws = 0
total_clashes = 10
print("The battle starts...\n")

import random

if len(Gandalf) != len(Saruman):
    print("Any of the sorcerers has more attacks!!")
    print("We are going to remove attacks randomly to match the number of attacks with the lesser.")
    if len(Gandalf) <= len(Saruman):
        times = len(Saruman) - len(Gandalf)
        count = 0
        while count < times:
            new_length = (len(Saruman))
            random_num = random.randint(1, len(Saruman)-1)
            print(random_num)
            Saruman.pop(random_num)
            count += 1
    else:
        times = len(Gandalf) - len(Saruman)
        count = 0
        while count < times:
            random_num = random.randint(0, len(Gandalf)-1)
            print(random_num)
            Gandalf.pop(random_num)
            count += 1

number_round = 0

total_clashes = len(Saruman)

while number_round < total_clashes:
    if Gandalf[number_round] == Saruman[number_round]:
        draws = draws + 1
    elif Gandalf[number_round] < Saruman[number_round]:
        saruman_wins = saruman_wins + 1
    else:
        gandalf_wins = gandalf_wins + 1

    number_round += 1

round_val = 0

while round_val < len(Saruman):
    if Gandalf[round_val] == Saruman[round_val]:
        print(" - The %s round was a draw!" % Name_of_round[round_val])
    elif Gandalf[round_val] < Saruman[round_val]:
        print(" - The winner of the %s round is Saruman" % Name_of_round[round_val].lower())
    else:
        print(" - The winner of the %s round is Gandalf" % Name_of_round[round_val].lower())
    round_val = round_val + 1

print("\nThe final result is Gandalf %d of %d battles - Saruman %d of %d battles." % (gandalf_wins, total_clashes, saruman_wins, total_clashes))
if saruman_wins < gandalf_wins:
    print("\nGandalf wins the battle!")
elif saruman_wins > gandalf_wins:
    print("\nSaruman wins the battle!")
else:
    print("\nThe battle ends with an epic draw!")

print("\n\nDUEL OF SORCERERS - BONUS\n")

print("1 - Spells now have a name and there is a dictionary that relates")
print("    that name to a power.")
print("2 - A sorcerer wins if he succeeds in winning 3 spell clashes in a row")
print("3 - Average of the spells lists.")
print("4 - Standard deviation of each of the spells lists.")

power = {
    "Fireball": 50,
    "Lighting bolt": 40,
    "Magic arrow": 10,
    "Black tentacles": 25,
    "Contagion": 45
}

gandalf_spells = [
    "Fireball",
    "Lighting bolt",
    "Lighting bolt",
    "Magic arrow",
    "Fireball",
    "Magic arrow",
    "Lighting bolt",
    "Fireball",
    "Magic arrow",
    "Fireball"
]

saruman_spells = [
    "Contagion",
    "Contagion",
    "Black tentacles",
    "Fireball",
    "Black tentacles",
    "Lighting bolt",
    "Magic arrow",
    "Contagion",
    "Magic arrow",
    "Magic arrow"
]
who_attacks = 0
random_words_attack = ["attacks with a ", "uses a ", "utilizes a ", "charges with a ", "shoots a "]
random_words_defense = ["refuse it with a ", "stops it with a ", "uses a ", "attacks with a "]
random_interjections = [", ", " and ", " but ", " at the same time ", ". ", " while "]

print("\nThe battle starts...\n")

import random

Round_of_clashes = 0
Total_of__clashes = len(saruman_spells)

saruman_score = 0
gandalf_score = 0
saruman_total_score = 0
gandalf_total_score = 0
total_draws = 0

while saruman_score < 3 and gandalf_score < 3 and Round_of_clashes < Total_of__clashes:

    who_attacks = random.randint(0, 1)
    random_word1 = random.randint(0, len(random_words_attack)-1)
    random_word2 = random.randint(0, len(random_words_defense)-1)
    random_word3 = random.randint(0, len(random_interjections)-1)
    if Round_of_clashes < 9:
        spell_round = "0" + str(Round_of_clashes + 1)

    else:
        spell_round = str(Round_of_clashes + 1)

    if who_attacks == 0:
        attacker = ["Gandalf ", gandalf_spells]
        defender = ["Saruman ", saruman_spells]
        print(" %s - %s%s%s%s%s%s%s" % (spell_round, attacker[0],  random_words_attack[random_word1], attacker[1][Round_of_clashes], random_interjections[random.randint(0, len(random_interjections)-1)], defender[0],random_words_defense[random_word2], defender[1][Round_of_clashes]))
        if power[attacker[1][Round_of_clashes]] > power[defender[1][Round_of_clashes]]:
            gandalf_score += 1
            gandalf_total_score += 1
            saruman_score = 0
        elif power[attacker[1][Round_of_clashes]] < power[defender[1][Round_of_clashes]]:
            gandalf_score = 0
            saruman_score += 1
            saruman_total_score +=1
        else:
            print("\t  What a draw!")
            gandalf_score = 0
            saruman_score = 0
            total_draws += 1

    else:
        attacker = ["Saruman ", saruman_spells]
        defender = ["Gandalf ", gandalf_spells]
        print(" %s - %s%s%s%s%s%s%s" % (spell_round, attacker[0],  random_words_attack[random_word1], attacker[1][Round_of_clashes], random_interjections[random_word3], defender[0],random_words_defense[random_word2], defender[1][Round_of_clashes]))
        if power[attacker[1][Round_of_clashes]] > power[defender[1][Round_of_clashes]]:
            gandalf_score = 0
            saruman_score += 1
            saruman_total_score += 1
        elif power[attacker[1][Round_of_clashes]] < power[defender[1][Round_of_clashes]]:
            gandalf_score += 1
            gandalf_total_score += 1
            saruman_score = 0
        else:
            print("\t  What a draw!")
            gandalf_score = 0
            saruman_score = 0
            total_draws += 1
    Round_of_clashes += 1

print("\n\nThe final result of the competition is:")
print("\n\t- Gandalf total wins: %d" % gandalf_total_score)
print("\t- Saruman total wins: %d" % saruman_total_score)
print("\t- Total draws: %d" % total_draws)

if gandalf_total_score > saruman_total_score:
    print("\n\t  THE WINNER OF THE BATTLE IS GANDALF")
elif gandalf_total_score < saruman_total_score:
    print("THE WINNER OF THE BATTLE IS SARUMAN")
else:
    print("THE FINAL RESULT IS A DRAW. WHAT A BATTLE, AMAZING DUEL!!")


print("\n\nAfter this apotheosic battle we have analyzed that:")


saruman_array = []
gandalf_array = []
saruman_array2 = []
gandalf_array2 = []

SD_saruman = 0
SD_gandalf = 0


for spell in saruman_spells:
    name_spell = spell
    saruman_array.append(power[name_spell])

for spell in gandalf_spells:
    name_spell = spell
    gandalf_array.append(power[name_spell])

average_saruman = sum(saruman_array)/len(saruman_spells)
average_gandalf = sum(gandalf_array)/len(gandalf_spells)


import math

for spells in range(len(saruman_spells)):

    saruman_array[spells] = math.pow(saruman_array[spells] - average_saruman, 2)

SD_saruman = math.sqrt(sum(saruman_array) / len(saruman_spells))


for spells in range(len(gandalf_spells)):

    gandalf_array[spells] = math.pow(gandalf_array[spells] - average_gandalf, 2)

SD_gandalf = math.sqrt(sum(gandalf_array)/len(gandalf_spells))

print("\nSrumnan's average spells is a %s power" % average_saruman)
print("Gandalf's average spells is a %s power" % average_gandalf)
print("Saruman's standard deviation is: %.2f" % SD_saruman)
print("Gandalf's standard deviation is: %.2f" % SD_gandalf)

