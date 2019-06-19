print("\n\tROBIN HOOD\n")

print("We are in a competition to win the archery contest in Sherwood.")
print("With our bow and arrows we shoot on a target and try to hit as")
print("close as possible to the cener. The center of the target is")
print("represented by the values (0,0) on the coordinate axes.\n")
print("\tSHOTS\n")
print("The current shoots are \"points = [(4, 5), (0, -2), (4, 7), (1, -3),")
print("(3, -2), (4, 5), (3, 2), (5, 7) (-5, 7), (2, 2), (-4, 5), (0, -2),")
print("(-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2), (5, 7), (5, 7), (2, 2),")
print("(9, 9), (-8, -9)]\n")

points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5),
          (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),
          (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2),
          (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]

print("\tTASKS\n")
print("1 - Robin Hood is famous for hitting an arrow with another arrow!")
print("2 - Calculate how many arrows have fallen in each quadrant.")
print("3 - Find the point closest to the center. Calculate its distance to the center.")
print("4 - Calculate the number of arrows that must be picked up in the forest")
print("    The target has a radius of 9")

print("\n\tRESULTS\n")

arrow_hits = 0

points_set = set()
diferent_values = 0
# print(type(points_set))

for i in points:
    points_set.update({i})

repeats = []
pos = 0
for i in points_set:
    var = points.count(i)
    repeats.append(var)

points_set = list(points_set)

arrow_hits = len(points)-len(points_set)

Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0
X_axis = 0
Y_axis = 0

for i in points:
    if i[0] > 0 and i[1] > 0:
        Q1 = Q1 +1
    elif i[0] < 0 and i[1] > 0:
        Q2 = Q2 +1
    elif i[0] < 0 and i[1] < 0:
        Q3 = Q3 +1
    elif i[0] > 0 and i[1] < 0:
        Q4 = Q4 +1
    elif i[0] == 0:
        X_axis += 1
    else:
        Y_axis += 1

distances = []

i = 0
import math
while i < len(points):

    a = math.sqrt(math.pow(points[i][0],2) + math.pow(points[i][1],2))
    distances.append(a)
    i += 1

print("\nRobin hit/s an arrow %s times." % arrow_hits)


print("\nThe distribution of the arrows is:")
print("\n\t - %d arrows in the Q1" % Q1)
print("\t - %d arrows in the Q2" % Q2)
print("\t - %d arrows in the Q3" % Q3)
print("\t - %d arrows in the Q4" % Q4)
print("\t - %d arrows in the X axis" % X_axis)
print("\t - %d arrows in the Y axis\n" % Y_axis)


get_min_distance = min(distances)
count_min = 0
count_max = 0
store_min_pos = []
count_position = 0

for i in distances:

    if get_min_distance == i:
        store_min_pos.append(count_position)
        count_min += 1
    elif i > 9:
        count_max += 1
    count_position += 1

arrow = []

print("The smallest distance to the center is %d" % min(distances))
for i in store_min_pos:
        arrow.append(str(points[i]))
if count_min == 1:
    print("The arrow with the values %s is the closest to the center." % arrow)
else:
    print("The arrows closest are the ones with values %s" % arrow)
if count_max > 1:
    print("There are %d arrows on the ground" % count_max)
elif count_max == 0:
    print("There are no arrows on the ground")
else:
    print("There is just one arrow on the ground")
