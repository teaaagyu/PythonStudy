student = {
    "name" : "tae gyu",
    "age" : 25,
    "major" : "computer science",  
}

print(student["name"])
print(student)

student["score"] = 90
print(student)

# 1. values() 메서드로 값만 출력
print("-> 값만 가져오기 (values):")
print(student.values())

# 2. 리스트로 변환
values_as_list = list(student.values())
print("\n-> 리스트로 변환된 값:")
print(values_as_list)

# 3. 반복문으로 값 출력
print("\n-> 반복문으로 각 값 출력:")
for value in student.values():
    print(value)

# 4. 키와 값 쌍 출력
print("\n-> 키와 값 같이 출력:")
for key, value in student.items():
    print(f"{key} : {value}")