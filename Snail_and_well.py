print("\n\tSNAIL AND WELL\n")

print("A snail falls at the bottom of a 125cm well. Each day the snail")
print("raises 30 cm. But at night,while sleeping, slides 20 cm because")
print("the walls are wet.\n")

print(" - How many days does it take to escape from the well?\n")


well_height = 125
daily_advance = 30
night_retreat = 20
accumulated_distance = 0
total_days = 0

while accumulated_distance <= well_height:
    accumulated_distance = accumulated_distance + daily_advance
    accumulated_distance = accumulated_distance - night_retreat
    total_days += 1


print("\tTotal days: " + str(total_days) + "\n\n")


print("\tSNAIL AND WELL - BONUS\n")

total_days_bonus = 0
accumulated_distance_bonus = 0
advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
advance_done = 0
standard_deviation = 0


print("The distance traveled by the snail is now defined by a list")
print("advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]\n")

print (" - How long does it take to rise the well?\n")

while accumulated_distance_bonus <= well_height:
    for var in advance_cm:
        accumulated_distance_bonus = accumulated_distance_bonus + var
        accumulated_distance_bonus = accumulated_distance_bonus - night_retreat
        total_days_bonus += 1
        if accumulated_distance_bonus >= well_height:
            break

print("\tTotal days %d\n" % total_days_bonus)

print(" - What is the maximum displacement in one day? And its minimum?\n")
print("\tThe maxium displace is %dcm , and the minium is %dcm\n" % (max(advance_cm), min(advance_cm)))

print(" - What is its average speed during the day?\n")

advance_done = advance_cm[:total_days_bonus]
advance_done = round(sum(advance_done)/total_days_bonus)

print("\tRounded average speed during the day while it came out is %scm\n" % advance_done)

print(" - What is the standard deviation of its displacement during the day?\n")

import math

advance_cm_onexit = advance_cm[:total_days_bonus]
print("Standard deviation is calculated under this list: " + str(advance_cm_onexit))

for values in range(len(advance_cm_onexit)):

    advance_cm_onexit[values] = math.pow((advance_cm_onexit[values] - advance_done), 2)

standard_deviation = math.sqrt(sum(advance_cm_onexit) / len(advance_cm_onexit))

print("\nStandard deviation of its displacement during the day while it came out is %.2f cm\n" % standard_deviation)
