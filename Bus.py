print("\nBUS\n")

print("This bus has a passenger entry and exit control system to monitor")
print("the number of occupants it carries and thus detect when there is")
print("too high a capacity.")
print("At each stop the entry and exit of passengers is represented by a")
print("tupple consisting of two integer numbers.")
print("Each Bus_Stop = (In, Out)")
print("\n\nTASKS")
print("\n1 - Calculate the number of stops")
print("2 - Assign to a variable a list whose")
print("3 - Find the maximum occupation of the bus")
print("4 - Calculate the average occupation and the standard deviation")

number_of_a_stops = 0
list_of_stops = []
number_of_travels = number_of_a_stops - 1
number_of_passengers = []
average_of_passenger = 0
SD_passengers = 0
Out = ""
In = ""


print("\n**** I\"m considering that the first stop and the last stop are")
print("the begin and the end of the route respectively. So there are no")
print("passengers exiting the first stop neither entering the last. ****\n")


number_of_stops = input("How many stops has the route you want to analyze?")

is_a_number = 0

while is_a_number == 0:
    try:
        number_of_stops = int(number_of_stops)
        is_a_number = 1
    except:
        print("Please enter a number,")
        number_of_stops = input("How many stops has the route you want to analyze? ")

for i in range(number_of_stops):

    if i == 0:
        In = input("How many passengers ENTER the bus at the initial stop? ")
        is_a_number = 0
        while is_a_number == 0:
            try:
                In = int(In)
                is_a_number = 1
            except:
                print("Please enter a number,")
                In = input("How many passengers ENTER the bus at the initial stop? ")

        list_of_stops.append((In,0))

    elif i < number_of_stops -1:
        In = ""
        Out = ""
        In = input("How many passengers ENTER the bus at the stop number %d ?" % i)
        is_a_number = 0
        while is_a_number == 0:
            try:
                In = int(In)
                is_a_number = 1
            except:
                print("Please enter a number,")
                In = input("How many passengers ENTER the bus at the stop number %d ?" % i)

        Out = input("And how many passengers LEAVE the bus at the stop number %d ?" % i)
        is_a_number = 0
        while is_a_number == 0:
            try:
                Out = int(Out)
                is_a_number = 1
            except:
                print("Please enter a number,")
                Out = input("How many passengers LEAVE the bus at the stop number %d ?" % i)

        list_of_stops.append((In, Out))
    else:
        a = sum(i[0] for i in list_of_stops)
        b = sum(i[1] for i in list_of_stops)
        exits_last_stop = a - b
        list_of_stops.append((0, exits_last_stop))

list_maximum_occupation = []

for value in range(len(list_of_stops)-1):
    a = sum(i[0] for i in list_of_stops[:(value + 1)])
    b = sum(i[1] for i in list_of_stops[:(value + 1)])
    list_maximum_occupation.append(a-b)


print("\nThe current bus route have %d stops" % number_of_stops)
print("\nThe tuple relative to the bus route is %s" % list_of_stops)
print("\nThe occupation of the bus in-between stops is %s\n" % list_maximum_occupation)

maximum_occupation = max(list_maximum_occupation)
average_ocucupation = sum(list_maximum_occupation) / (len(list_of_stops) - 1)

import math

advance_cm_onexit = []
tin = 0
while tin < len(list_maximum_occupation):
    advance_cm_onexit.append(math.pow((list_maximum_occupation[tin] - average_ocucupation), 2))
    tin += 1

standard_variation = math.sqrt(sum(advance_cm_onexit)/len(list_maximum_occupation))

print("The maximum occupation is %d" % maximum_occupation)
print("The average occupation is %.2f" % average_ocucupation)
print("The standard variation is %.2f" % standard_variation)



#print("The succession of the stops is %" % stops)
