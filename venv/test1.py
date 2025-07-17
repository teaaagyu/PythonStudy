import pandas as pd

data = {
    "Month": ["JAN", "FEB", "MAR", "APR", "MAY"],
    "1958": [380, 318, 362, 348, 363],
    "1959": [360, 342, 406, 396, 420],
    "1960": [417, 391, 419, 461, 472]
}

df = pd.DataFrame(data)
df.to_csv("test.csv", index=False)  # CSV 파일로 저장

print("CSV 저장 완료")

# 다시 불러오기
df2 = pd.read_csv("test.csv")
print(df2)
