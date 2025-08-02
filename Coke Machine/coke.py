#f-string = f"". it allows imbedding expressions inside the string.
#  Allows you to do something over and over while a conditionis still true.

def main():
    coins = [5, 10, 25]
    amount_due = 50
    while amount_due > 0:
        inp = int(input("Insert coin: "))
        if inp in coins:
             amount_due -= inp
        if amount_due > 0:
            print(f"Amount Due: {amount_due}")

        elif amount_due == 0:
            print(f"Amount Due: {amount_due}", "Change owed: 0")

        else:
            print(f"Change owed: {-amount_due}")

main()
