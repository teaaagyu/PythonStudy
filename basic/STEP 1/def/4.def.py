def calculator(a, b):
    print(f"{a} + {b} =", a + b)
    print(f"{a} - {b} =", a - b)
    print(f"{a} * {b} =", a * b)
    print(f"{a} / {b} =", a / b)

a = int(input("add number: "))
b = int(input("add number: "))
calculator(a, b)
print("계산이 완료되었습니다.")
