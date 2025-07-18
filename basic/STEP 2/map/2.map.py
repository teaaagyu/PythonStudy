# 문자열을 정수로 변환하는 함수 정의
def str_to_int(strings):
    return list(map(int, strings))

# 반복적으로 처리
dataset1 = ['10', '20', '30']
dataset2 = ['5', '15', '25']

result1 = str_to_int(dataset1)
result2 = str_to_int(dataset2)

print(result1)  # 출력: [10, 20, 30]
print(result2)  # 출력: [5, 15, 25]