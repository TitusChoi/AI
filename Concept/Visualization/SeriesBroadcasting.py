# Title         : SeriesBroadcasting.py
# Description   : Series와 Broadcasting 활용 예제

import pandas as pd

scientists = pd.read_csv('./AI/datasets/scientists.csv')

# 실제 데이터를 열을 2개 추가하여 저장 : 태어난 날, 돌아가신 날
scientists['born_dt'] = pd.to_datetime(scientists['Born'], format = '%Y-%m-%d')
scientists['died_dt'] = pd.to_datetime(scientists['Died'], format = '%Y-%m-%d')

# 산 날의 days를 추출 : 벡터 연산
scientists['living_dt'] = scientists['died_dt'] - scientists['born_dt']
print(scientists)

# 엑셀 데이터 파일로 저장 : xlwt, openyxl 모듈 활용, datasets에 저장
scientists.to_excel('./AI/datasets/scientist.xlsx')