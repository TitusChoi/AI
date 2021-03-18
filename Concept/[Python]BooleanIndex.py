# Title         : [Python]BooleanIndex.py
# Description   : Boolean 추출 활용 예제

# 파일 경로 확인 = C:\Users\TitusChoi\Desktop\Library\CodeLion\AI\datasets
import pandas as pd

scientists = pd.read_csv('./AI/datasets/scientists.csv')
print(scientists.head())
ages = scientists['Age']
print(ages.min())

# Boolean 추출
print(ages[ages>ages.mean()])       # 참 값인 values를 추출
# print(ages>ages.mean())             # 참 값인 것만 추출
TF_result = list(ages>ages.mean())  # True와 False 값 반환 list
print(ages[TF_result])