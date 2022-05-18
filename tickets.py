pink = int(input())
green = int(input())
red = int(input())
orange = int(input())
target = int(input())
tickets = {pink: "pink", green: "green", red: "red", orange: "orange"}
min_t = []
count = 0
price_list = list(tickets.keys())

for i in range(len(price_list)):
    if price_list[i] == target:
        #print(tickets[price_list[i]])
        min_t.append(1)
        ans = [0 for x in price_list]
        ans[i] = 1
        print("# of Pink is", ans[0], "# of green is", ans[1], "# of red is", ans[2], "# of orange is", ans[3])
        count += 1
    if price_list[i] < target:
        if target % price_list[i] == 0:
            ans = [0 for x in price_list]
            ans[i] = target//price_list[i]
            min_t.append(target//price_list[i])
            print("# of Pink is", ans[0], "# of green is", ans[1], "# of red is", ans[2], "# of orange is", ans[3])
            count += 1

    for j in range(i + 1, len(price_list)):
        if price_list[i] + price_list[j] == target:
            min_t.append(2)
            ans = [0 for x in price_list]
            ans[i] = 1
            ans[j] = 1
            print("# of Pink is", ans[0], "# of green is", ans[1], "# of red is", ans[2], "# of orange is", ans[3])
            count += 1

            for k in range(j + 1, len(price_list)):
                if price_list[i] + price_list[j] + price_list[k] == target:
                    min_t.append(3)
                    ans = [0 for x in price_list]
                    ans[i] = 1
                    ans[j] = 1
                    ans[k] = 1
                    print("# of Pink is", ans[0], "# of green is", ans[1], "# of red is", ans[2], "# of orange is",
                          ans[3])
                    count += 1

                    for l in range(k + 1, len(price_list)):
                        if price_list[i] + price_list[j] + price_list[k] + price_list[l] == target:
                            min_t.append(4)
                            ans = [1 for x in price_list]
                            print("# of Pink is", ans[0], "# of green is", ans[1], "# of red is", ans[2],
                                  "# of orange is", ans[3])
                            count += 1

print("Total combinations is", str(count))
print("Minimum number of tickets to print is", str(min(min_t)))
