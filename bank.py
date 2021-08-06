principle = int(input())
tenure = int(input())
bank = []

def check_emi():
    installments = int(input())
    sum = 0
    for i in range(0, installments):
        period, rate = [float(i) for i in input().split()]
        x = pow(1 + rate, period * 12)
        emi = (principle * rate)/(1-1/x)
        sum = sum + emi
    bank.append(sum)

check_emi()
check_emi()
print(bank)
if bank[0] < bank[1]:
    print("Bank A")
else:
    print("Bank B")

