def sing(n):
    if n > 0:
        print(str(n) + " Bottles of beer on the wall, " + str(n) + " bottles of bear")
        print("Take one down and pass it around, " + str(n - 1) + " Bottles of beer")
    elif n == 0:
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print("Go to the store and buy some more, 99 bottles of beer on the wall.")


bottles = 99
while bottles >= 0:
    sing(bottles)
    bottles -= 1
