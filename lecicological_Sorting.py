lex = str(input())
lex_l = list(lex)
alphabets = str(input())
letters = dict()
for letter in lex_l:
    if letter not in letters:
        letters[letter] = lex_l.index(letter)
#print(letters)

ans = []
for a in alphabets:
    if a in letters:
       ans.append((letters[a], a))
ans.sort()
final = []
for x, y in ans:
    final.append(y)
print("".join(final))