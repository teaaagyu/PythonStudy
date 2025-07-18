import os
import pandas as pd

# 현재 파이썬 파일 기준 경로
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 파일 경로 지정
csv_path = os.path.join(BASE_DIR, "../../Data_File/test.csv")
excel_path = os.path.join(BASE_DIR, "../../Data_File/example_average.xlsx")

# CSV 읽기
df = pd.read_csv(csv_path)
print(df)

# 열(Column) 단위 작업 예시
print("\n1958년도 데이터:")
print(df["1958"])

# 통계 계산
print("\n1959년도 평균:")
print(df["1959"].mean())

# 평균 열 추가 및 저장
df["Average"] = df[["1958", "1959", "1960"]].mean(axis=1)
df.to_excel(excel_path, index=False)
