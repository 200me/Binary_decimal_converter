
mode = input("enter mode, 10 or 2: ").strip()
if mode == "10":
    print("Decimal to Binary mode set")
    try:
        num = int(input("enter decimal number: "))
    except ValueError:
        print('wrong decimal input')
        exit()
    binary = ""

    while num > 0:
        if num % 2 == 1:
            binary = "1" + binary
            num = num // 2
        else:
            binary = "0" + binary
            num = num // 2

    print(binary)

elif mode == "2":
    print("BInary to Decimal mode set")
    num = input("enter binary number: ")

    decimal = 0
    for index in range(len(num)):
        if num[index] in ['1', '0']:
            decimal += int(num[index]) * 2 ** (len(num)-(index + 1))
        else:
            print('wrong binary input')
            exit()
    print(decimal)
else:
    print('wrong mode')









