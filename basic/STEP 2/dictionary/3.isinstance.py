def add_only_numbers(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("숫자만 입력해야 합니다.")
    return a + b

print(add_only_numbers(3, 5))  # 출력: 8
print(add_only_numbers("j", 5))  # 오류: ValueError: 숫자만 입력해야 합니다.