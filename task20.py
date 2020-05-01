dig = int(input('Type any digit: '))

def a(dig):
    even = 0
    odd = 0
    while dig > 0:
        if dig % 2 == 0:
            even += 1
        else:
            odd += 1
        dig = dig // 10

    print("Even:", even)
    print("Odd:", odd)
a(dig)
