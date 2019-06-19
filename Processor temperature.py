print("\t\nPROCESSOR TEMPERATURE\n")

print("We have a temperature sensor in the processor of our company's")
print("server. We want to analyze the data provided to determinate")
print("whether we should change the cooling system for a better one.")
print("It is expensive and as a data analyst we cannot make decisions")
print("without a basis.")
print("We provided the temperatures measured throughout the 24 hours")
print("a day in a list-type data structure composed of 24 integers:")
print("\n\tTemperatures_C = [33,66,65,0,59,60,62,64,70,76,80,69,80,83,")
print("                      68,79,61,53,50,49,53,48,45,39]")
print("")

# import

import matplotlib.pyplot as plt


# axis x, axis y
y = [33,66,65,0,59,60,62,64,70,76,80,81,80,83,90,79,61,53,50,49,53,48,45,39]

#  y = [33,66,65,3,12,5,8]
x = list(range(len(y)))

# plot
plt.plot(x, y)
plt.axhline(y=70, linewidth=1, color='r')
plt.xlabel('hours')
plt.ylabel('Temperature ºC')
plt.title('Temperatures of our server throughout the day')
plt.text(0.5, 1.0, 'Temperatures of our server throughout the day')
plt.grid(True)
# plt.show()

print("\t\nPROBLEM\n")

print("If the sensor detects more than 4 hours with temperatures grater")
print("than or equal to 70ºC or any temperature above 80ºC or the")
print("average exceeds 65ºC throughout the day, we must give the order")
print("to change the cooling system to avoid damaging in the processor.")
print("\n\t1 - Get the minimum temperature.")
print("\t2 - Get the maximum temperature.")
print("\t3 - Temperatures equal or greater than 70ºC.")
print("\t4 - Average temperatures throughout the day.")
print("\t5 - If there was a sensor failure at 03:00am and we did not")
print("        capture the data, how would you estimate the value that we lack?")
print("        Correct the value in the list of temperatures")
print("\t6 - BONUS: Our maintenance staff is from US and does not")
print("        understand the international metric system (SI). Pass")
print("        temperatures to Degrees Fahrenheit")

print("\n\n**** The FIRST STEP will be finding if there is any outlider to provide")
print("more accurate results, and estimate the new value. I also calculated all")
print("data based on the temperatures of the graph instead of the explanation")
print("and without the possible outliders ****")

count_total_values = len(y)
remainder = count_total_values % 2
sort_temperatures = sorted(y)

# WARNING si es fa servir "sort_temperatures = y, sort_temperatures.sort()"
# modifica tambe la llista Y

import math

if remainder == 0:

    middle_array = int(count_total_values / 2)
    median = (sort_temperatures[middle_array-1] + (sort_temperatures[middle_array]))/2
    Q1 = sort_temperatures[:middle_array]
    Q3 = sort_temperatures[middle_array:]
    count_Q1 = len(Q1)
    remainder_Q1 = count_Q1 % 2
    if remainder_Q1 == 0:
        middle_Q1 = int(count_Q1 / 2)
        median_Q1 = (Q1[middle_Q1-1] + (Q1[middle_Q1]))/2
        median_Q3 = (Q3[middle_Q1-1] + (Q3[middle_Q1]))/2
    else:
        median_Q1 = Q1[int(math.floor(len(Q1)/2))]
        median_Q3 = Q3[int(math.floor(len(Q1)/2))]

else:
    middle_array = int((count_total_values + 1) / 2)
    median = sort_temperatures[middle_array-1]
    Q1 = sort_temperatures[:middle_array-1]
    Q3 = sort_temperatures[middle_array:]
    count_Q1 = len(Q1)
    remainder_Q1 = count_Q1 % 2
    if remainder_Q1 == 0:
        middle_Q1 = int(count_Q1 / 2)
        median_Q1 = (Q1[middle_Q1-1] + (Q1[middle_Q1]))/2
        median_Q3 = (Q3[middle_Q1-1] + (Q3[middle_Q1]))/2
    else:
        median_Q1 = Q1[int(math.floor(len(Q1)/2))]
        median_Q3 = Q3[int(math.floor(len(Q1)/2))]

IQR_interquartile_range = (median_Q3 - median_Q1)

high_outlider = median_Q3 + (1.5 * IQR_interquartile_range)
low_outlider = median_Q1 - (1.5 * IQR_interquartile_range)
positions_with_outliders = []
value = 0

for i in y:
    if i < low_outlider or i > high_outlider:
        positions_with_outliders.append(value)
    value += 1

# print(y)
# print(Q1)
# print(Q3)
# print(median_Q1)
# print(median_Q3)
# print(high_outlider)
# print(low_outlider)
# print(positions_with_outliders)

list_of_temperatures = y

y = tuple(y)   # protegeixlo la llista perque el del també l'afecta
# print(type(y))
#print(positions_with_outliders)

count = 0
for numero in positions_with_outliders:
    del list_of_temperatures[numero-count]
    count += 1
# printing modified lists

# print(list_of_temperatures)


print("\n\nThe minium temperature avoiding outliers is %d" % min(list_of_temperatures))
print("And the maxium also avoiding outliers is %d" % max(list_of_temperatures))
temperatures_70 = []
for i in list_of_temperatures:
    if i >= 70:
        temperatures_70.append(i)

print("\nThe list of temperatures equal or over 70 C are:", temperatures_70)

average_24h = sum(list_of_temperatures) / len(list_of_temperatures)

list_of_temperatures_corrected = list(y)


for i in positions_with_outliders:

    if i == 0:
        val_num_before = y[len(y)-1]
        val_num_after = y[i+1]
        val_to_replace = int((val_num_before + val_num_after) / 2)
        list_of_temperatures_corrected[i] = val_to_replace
    elif i == len(y)-1:
        val_num_before = y[i-1]
        print(val_num_before)
        val_num_after = y[0]
        print(val_num_after)
        val_to_replace = int((val_num_before + val_num_after) / 2)
        list_of_temperatures_corrected[i] = val_to_replace
    else:
        val = y[i]
        val_num_before = y[i-1]
        val_num_after = y[i+1]
        val_to_replace = int((val_num_before + val_num_after) / 2)
        list_of_temperatures_corrected[i] = val_to_replace

print("\nThe list with the temperatures corrected is:\n")
print(list_of_temperatures_corrected[:12])
print(list_of_temperatures_corrected[12:])

list_Fahrenheit = [round((i * 1.8)+32,1) for i in list_of_temperatures_corrected]

print("\nThe list with the temperatures in Fahrenheit:\n")
print(list_Fahrenheit[:12])
print(list_Fahrenheit[12:])

# axis x, axis y
y = list_Fahrenheit

#  y = [33,66,65,3,12,5,8]
x = list(range(len(y)))

# plot
plt.plot(x, y)
plt.axhline(y=70, linewidth=1, color='r')
plt.xlabel('hours')
plt.ylabel('Temperature ºF')
plt.title('Temperatures of our server throughout the day')
plt.text(0.5, 1.0, 'Temperatures of our server throughout the day')
plt.grid(True)
y = list_of_temperatures_corrected

#  y = [33,66,65,3,12,5,8]
x = list(range(len(y)))

# plot
plt.plot(x, y)
plt.axhline(y=70, linewidth=1, color='r')
plt.xlabel('hours')
plt.ylabel('Temperature ºC')
plt.title('Temperatures of our server throughout the day')
plt.text(0.5, 1.0, 'Temperatures of our server throughout the day')
plt.grid(True)
# plt.show()
hours = 0
clock = 0
list_hours = []
last_print = 0
consecutive_hours = 4

average_24h_corrected = sum(list_of_temperatures_corrected) / len(list_of_temperatures_corrected)


for i in list_of_temperatures_corrected:

    if hours >= 4 or i > 80 or average_24h > 65:
        if hours >= 4:
            if last_print != 1:
                print("\n\t\t--------------------------------")
                print("\t\t|        W A R N I N G         |")
                print("\t\t--------------------------------")
                print("\t\tPlease Change The Cooling System")
                print("\t\t  More than 4 hours overheating")
                print("")
            last_print = 1

            consecutive_hours = consecutive_hours + 1
        if i > 80:
            print("\n\t\t--------------------------------")
            print("\t\t|        W A R N I N G         |")
            print("\t\t--------------------------------")
            print("\t\tPlease Change The Cooling System")
            print("\t\t Temperature is higher than 80ºC  ")
            print("")
        if average_24h > 65:
            print("\n\t\t--------------------------------")
            print("\t\t|        W A R N I N G         |")
            print("\t\t--------------------------------")
            print("\t\tPlease Change The Cooling System")
            print("\t\tDaily average was higher to 65ºC")
            print("")

    if i >= 70:
        hours += 1
        list_hours.append(str(clock) + ":00")
    else:
        hours = 0
    clock += 1

print("\n\nThe list of the hours over 70ºC is: \n")

for i in list_hours:
    print("\t- %s hours" % i)

average_24h_corrected_F = sum(list_Fahrenheit) / len(list_Fahrenheit)

temperature_C_array = []
temperature_F_array = []

for i in range(len(list_of_temperatures_corrected)):
    temperature_C_array.append(math.pow(list_of_temperatures_corrected[i] - average_24h_corrected, 2))

SD_temperatures_C = math.sqrt(sum(temperature_C_array)/len(list_of_temperatures_corrected))

for i in range(len(list_Fahrenheit)):
    temperature_F_array.append(math.pow(list_Fahrenheit[i] - average_24h_corrected_F, 2))

SD_temperatures_F = math.sqrt(sum(temperature_F_array)/len(list_Fahrenheit))


print("\nhe average for Celcius values is: ", round(average_24h_corrected,2))
print("The average for Farenheit values is: ", round(average_24h_corrected_F,2))


print("\nThe standard deviation for Celcius values is: ", round(SD_temperatures_C,2))
print("The standard deviation for Farenheit values is: ", round(SD_temperatures_F,2))

plt.show()
