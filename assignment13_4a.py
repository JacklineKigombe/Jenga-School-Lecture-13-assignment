def purchase():
    total = 0

    while True:
        price = int(input("Enter item price: "))

        total += price
        if total >= 1000:
            print(f"The total is {total}.You have reached your budget limit of 1000")
            break
        else:
            print(f"The total so far is {total}")

purchase()
