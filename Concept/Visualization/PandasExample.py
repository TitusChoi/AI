# Title         : PandasExample.py
# Description   : Pandas 활용 예제

# 파일 경로 확인 = C:\Users\TitusChoi\Desktop\Library\CodeLion\AI\datasets\gapminder.tsv
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./AI/datasets/gapminder.tsv', sep='\t') # tsv는 tap으로 구분
# print(df.head(10))            # 10개 대표적인 데이터 가져옴, 기본적으로 데이터 프레임으로 반환
# print(df.shape)               # 몇 행 몇 열인지 출력
# print(type(df))               # 자료형 = 데이터 프레임
# print(df.columns)             # object = string
# print(df.info())              # 전반적인 정보 출력
# print(df.tail(n=1))           # 마지막 행 데이터 -1로 못함, 마지막 행은 보통 tail 함수로 출력하면 편하다.
# print(df.loc[[0, 10, 100]])   # 다중 데이터 출력

# 원하는 데이터 출력 method 1
# subset = df.loc[:,['year', 'pop']]
# print(subset.head())
# subset = df.iloc[:,0:6:2]
# print(subset.head())

# 원하는 데이터 출력 method 2 : 특정 인덱스 리스트
# print(df.loc[[0, 99, 999], ['year', 'pop', 'lifeExp']])

# 원하는 데이터 출력 method 3 : slicing 활용
# print(df.loc[10:13, ['year', 'pop', 'lifeExp']])

'''
그룹화한 데이터의 평균 구하기 : lifeExp 열을 연도별로 그룹화하여 평균 계산하기
    1. 데이터를 year 열로 그룹화
    2. lifeExp 열의 평균 구하기
    3. 연도와 나이 평균별 데이터 상관 분석하기

    print(df.groupby('year')['lifeExp'].mean())

    더 나아가, 기대수명, 1인당 GDP 역시 보고 싶다면?
    print(df.groupby(['year']['continent'])['lifeExp', 'gdpPercap'].mean())

    또한, 특정 값에 있는 빈도를 알고 싶다면?
    print(df.groupby('continent')['country'].nunique())
'''
# print(df.info())
# print(df.groupby('year')['country'].nunique())

# 특정 데이터 시각화
global_yearly_lifeExp = df.groupby('year')['lifeExp'].mean()
global_yearly_lifeExp.plot()
plt.show()