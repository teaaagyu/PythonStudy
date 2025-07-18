data = [1, "hello", 3.14, True]

for value in data:
    if isinstance(value, int):
        print(f"{value}는 정수입니다.")
    elif isinstance(value, str):
        print(f'"{value}"는 문자열입니다.')
    elif isinstance(value, float):
        print(f"{value}는 실수입니다.")