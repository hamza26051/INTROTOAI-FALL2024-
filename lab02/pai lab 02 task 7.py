daily_temperatures_celsius = [15, 40, 30, 30, 31, 32, 33, 34, 35, 55, 37, 32, 39, 40, 41, 27, 21, 44, 45, 46, 47, 48, 38, 50, 32, 52, 48, 54, 31, 56]


def avg(daily_temperatures_celsius):
    sume=0
    for temp in daily_temperatures_celsius:
      sume+=temp
    average=float(sume)/len(daily_temperatures_celsius)
    print(average)

def highest(daily_temperatures_celsius):
   high=0
   for temp in daily_temperatures_celsius:
      if (temp>high):
         high=temp

   print(high)

def lowest(daily_temperatures_celsius):
   low=daily_temperatures_celsius[0]
   for temp in daily_temperatures_celsius:
      if (temp<low):
         low=temp

   print(low)

def ascending(daily_temperatures_celsius):
    liste = daily_temperatures_celsius[:]
    for i in range(len(liste)):
        for j in range(i + 1, len(liste)):
            if liste[i] > liste[j]:
                liste[i], liste[j] = liste[j], liste[i]
    for i in range(len(daily_temperatures_celsius)):
        daily_temperatures_celsius[i] = liste[i]

    print(daily_temperatures_celsius)


def remove(daily_temperatures_celsius):
   day= int(input("temperature of the day you want to remove"))
   if 1 <= day <= len(daily_temperatures_celsius):
        # Convert 1-based index to 0-based index
        daily_temperatures_celsius.pop(day - 1)
        print(f"Updated list after removing day {day}: {daily_temperatures_celsius}")
   else:
        print("Invalid day. Please enter a valid day number.")

