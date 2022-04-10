def sumnum_1():
    total = 0

    for num in range(1,101):
        total += num
    
    print(f"Sum of 1 to 100 is {total}")

def sumnum_2():
    total = 0
    num = 1

    while num < 101:
        total += num
        num += 1
    
    print(f"Sum of 1 to 100 is {total}")


sumnum_1()

sumnum_2()
