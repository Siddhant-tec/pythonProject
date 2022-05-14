try:
    alphabet = input()
    if alphabet.isalpha():
        print(alphabet + " is alphabet")
    else:
        raise ValueError
except ValueError:
    print(alphabet + " is not an alphabet")
