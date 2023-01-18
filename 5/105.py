def In_1():

    a = int(input())
    n = int(input())

    s = ''

    while a > 0:
        c = a % n
        if c < 10:
            s = str(c) + s
        else:
            s = chr(ord('A')+c-10) + s
        a //= n

    print(s)

def Out_1():
    b = input()
    c = int(input())

    power = 1
    ans = 0
    for i in b[::-1]:
        if i < 'A':
            ans += int(i)*power
        else:
            ans += (ord(i) - ord('A') + 10)*power
        power *= c

    print(ans)
In_1()
Out_1()