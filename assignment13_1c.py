def sumnum_1():
    last_num = int(input("Enter a number greater than 1: "))

    if last_num <= 1:
        print("Enter a number greater than 1: ")
        return
    
    total = 0

    for num in range(1,last_num+1):
        total += num
    
    print(f"Sum of 1 to {last_num} is {total} ")

def sumnum_2():
    last_num = int(input("Enter a number greater than 1: "))

    if last_num <= 1:
        print("Please enter a number greater than 1")
        return

    total = 0
    num = 1

    while num <= last_num:
        total += num
        num += 1
    
    print(f"Sum of 1 to {last_num} is {total} ")


sumnum_1()
print()
sumnum_2()
