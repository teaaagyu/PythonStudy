nums = ['1', '2', '3', '4', '5']
nums_int = list(map(int, nums))  # 반복문 없이 처리
print(nums_int)  # 출력: [1, 2, 3, 4, 5]
print(nums[1] + nums[2])  # 출력: 5
print(nums_int[1] + nums_int[2])  # 출력: 5