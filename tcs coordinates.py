from collections import Counter

latitude_string = input("")
longitude_string = input("")


def get_coordinates(str):
    count = Counter(str)
    x = max(count, key=count.get)
    y = min(count, key=count.get)
    z = int(count[x]) - int(count[y])
    if str[len(str) - 1] == 's':
        print(z, "South")
    elif str[len(str) - 1] == 'n':
        print(z, "North")
    elif str[len(str) - 1] == 'w':
        print(z, "West")
    elif str[len(str) - 1] == 'e':
        print(z, "East")
    else:
        print("Incorrect Coordinate")


get_coordinates(latitude_string)
get_coordinates(longitude_string)
