import pandas as pd

# test.csv 파일 읽어오기
df = pd.read_csv("test.csv")

# 데이터 확인
print(df)

# 열(Column) 단위 작업 예시
print("\n1958년도 데이터:")
print(df["1958"])  # 특정 연도 데이터를 가져오기

# 데이터 통계 계산
print("\n1959년도 데이터 평균:")
print(df["1959"].mean())  # 1959년도 데이터 평균 계산

df["Average"] = df[["1958", "1959", "1960"]].mean(axis=1)
df.to_csv("example_with_average.csv", index=False)
