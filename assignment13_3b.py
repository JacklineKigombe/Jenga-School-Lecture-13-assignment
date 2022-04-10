def final_val2():
    x = 7

    while x >=5 and x <=8:
        print(x)
        if x % 2 == 0:
            x = x + 1
        else:
            x = x - 1
    

    print(f"Final value", x)

final_val2()
