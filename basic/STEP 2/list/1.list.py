fruits = ["사과", "바나나", "포도"]
print(fruits[0])  # 첫 번째 값, 출력: "사과"

# 리스트의 요소 추가
fruits.append("딸기")  
print(fruits)  # 출력: ['사과', '바나나', '포도', '딸기']

fruits.insert(1, "오렌지")  # 인덱스 1에 "오렌지" 추가

# 리스트 반복
for fruit in fruits:
    print(fruit)