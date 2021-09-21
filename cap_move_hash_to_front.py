sentence = input("")
hash_list = list()
for letter in sentence:
    if letter == "#":
        hash_list.append(letter)
non_hash = sentence.replace("#", "")
hash_list = "".join(hash_list)
print(hash_list + non_hash)



