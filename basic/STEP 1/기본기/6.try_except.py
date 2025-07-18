try:
    num = int(input("숫자를 입력하세요: "))
    print(f"입력한 숫자는 {num}입니다.")
except ValueError:
    print("숫자가 아닌 값을 입력하셨습니다.")