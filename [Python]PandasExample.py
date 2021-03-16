# C:\Users\TitusChoi\Desktop\Library\CodeLion\CodeLionAI\datasets\gapminder.tsv
import pandas as pd

df = pd.read_csv('./AI/datasets/gapminder.tsv', sep='\t') # tsv는 tap으로 구분
# print(df.head()) # 5개 대표적인 데이터 가져옴, 기본적으로 데이터 프레임으로 반환
# print(df.shape) # 몇 행 몇 열인지 출력
print(df.columns) # object = string