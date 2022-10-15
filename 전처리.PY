import pandas as pd
import numpy as np
import seaborn
"""
df = pd.DataFrame({'캠페인시작날짜': ['2021.08.01', '2021.09.01', '2021.10.01']})
print(df)
df['캠페인시작날짜'] = df['캠페인시작날짜'].apply(lambda x: x.replace('.', '-'))
print(df)

df = pd.DataFrame({'캠페인명': ['aaa캠페인', 'bbb캠페인', 'ccc캠페인'], '캠페인날짜': [
                  '2020-02-01', '2021-03-08', '2021-11-04']})
df.loc[(df.캠페인명 == 'ccc캠페인'), '캠페인날짜'] = '2021-05-30'
print(df)
"""
# 시리즈 = 값 + 인덱스
s = pd.Series([9904312, 3448737, 2890451, 2466052],
              index=["서울", "부산", "인천", "대구"])
print(s)

pd.Series(range(10, 14))  # 인덱스를 지정하지 않는다면 0부터 시작하는 정수가 인덱스
s.index  # 인덱스 접근
s.values  # 밸류 접근
s.name = '인구'
s.index.name = '도시'
print(s)

# 시리즈 연산은 밸류에만 적용, 인덱스에는 영향이 없다.
tmp = s/1000000
print(tmp)

# 시리즈 인덱싱
print(s[1], s['부산'])
print(s[[0, 3, 1]])  # 자료의 순서를 바꾸거나 특정 부분만 선택 가능 == s[['서울','대구','부산']]

print(s[(250e4 < s) & (s < 500e4)])  # 인구가 250만 초과 500만 미만인 경우
print(s[1:3])  # 두번째(1)부터 세번째(2)까지
print(s['부산':'대구'])  # 부산에서 대구까지(대구 포함)

s0 = pd.Series(range(3), index=["a", "b", "c"])
print(s0.a)  # 인덱스가 영문인 경우 인덱스로 속성처럼 접근 가능

# 시리즈와 딕셔너리 - 딕셔너리와 비슷하게 in 연산, items 메서드 등 사용 가능
print('서울' in s)  # True
for k, v in s.items():
    print('%s = %d' % (k, v))

s2 = pd.Series({'서울': 9631482, '부산': 3393191, '인천': 2632035, '대전': 1490158})
print(s2)  # 딕셔너리 형태로 생성 시 순서가 없으므로 순서를 원한다면 리스트 형태로 생성해야 함
s2 = pd.Series({"서울": 9631482, "부산": 3393191, "인천": 2632035, "대전": 1490158},
               index=["부산", "서울", "인천", "대전"])
print(s2)

# 인덱스 기반 연산 - 두 시리즈에 대한 연산 수행 시 인덱스가 같은 데이터에 대해서만 수행
ds = s-s2  # 인구 증가량
print(ds)
print(s.values-s2.values)
print()
print(ds.notnull())

rs = (s-s2)/s2 * 100  # 인구 증가율
rs = rs[rs.notnull()]
print(rs)
print()

# 데이터의 추가, 갱신, 삭제
rs['부산'] = 1.63  # 인덱스 이용 갱신
rs['대구'] = 1.41  # 인덱스 이용 추가
print(rs)
del rs['서울']  # 인덱스 삭제
print(rs)
"""
연습 문제 4.1.1

(1) 임의로 두 개의 시리즈 객체를 만든다. 모두 문자열 인덱스를 가져야 하며 두 시리즈에 공통적으로 포함되지 않는 라벨이 있어야 한다.

(2) 위에서 만든 두 시리즈 객체를 이용하여 사칙 연산을 한다.
"""
# (1)
sa = pd.Series([88, 92, 76, 54, 100], index=['맹구', '유리', '훈이', '짱구', '철수'])
sb = pd.Series([77, 90, 69, 98, 75], index=['맹구', '수지', '오수', '짱구', '치타'])
# (2)
print(sb-sa)
print(sa+sb)
print((sa*sb).notnull())
print(sa/sb)
print()
# 데이터 프레임
data = {
    "2015": [9904312, 3448737, 2890451, 2466052],
    "2010": [9631482, 3393191, 2632035, 2431774],
    "2005": [9762546, 3512547, 2517680, 2456016],
    "2000": [9853972, 3655437, 2466338, 2473990],
    "지역": ["수도권", "경상권", "수도권", "경상권"],
    "2010-2015 증가율": [0.0283, 0.0163, 0.0982, 0.0141]
}
columns = ["지역", "2015", "2010", "2005", "2000", "2010-2015 증가율"]
index = ["서울", "부산", "인천", "대구"]
df = pd.DataFrame(data, index=index, columns=columns)
print(df)
print(df.values)
print(df.columns)
print(df.index)
df.index.name = '도시'
df.columns.name = '특성'
print('\n', df)


# 연습문제

data = {
    "국어": [80, 90, 70, 30],
    "영어": [90, 70, 60, 40],
    "수학": [90, 60, 80, 70],
}
columns = ["국어", "영어", "수학"]
index = ["춘향", "몽룡", "향단", "방자"]
df = pd.DataFrame(data, index=index, columns=columns)

# (1) 모든 학생의 수학 점수를 시리즈로 나타내라
print(df['수학'])
# (2) 모든 학생의 국어, 영어 점수를 데이터 프레임으로 나타내라
print(df[['국어', '영어']])
# (3) 모든 학생의 각 과목 평균 점수를 새로운 열로 추가한다.
df['평균'] = df.mean(axis=1)
print(df)
# (4) 방자의 영어 점수를 80점으로 수정하고 평균 점수도 다시 계산한다.
df['영어']['방자'] = 80
df['평균'] = df.mean(axis=1)
print(df)
# (5) 춘향의 점수를 데이터프레임으로 나타낸다.
print(df.loc['춘향'])
# (6) 향단의 점수를 시리즈로 나타낸다.


# 데이터 프레임 데이터 조작 1) 갯수 세기
s = pd.Series(range(10))
s[3] = np.nan
print(s)
print(s.count())  # NaN값은 세지 않음

# 데이터 프레임에서는 각 열마다 별도로 숫자를 센다.
np.random.seed(2)
df = pd.DataFrame(np.random.randint(5, size=(4, 4)), dtype=float)
df.iloc[2, 3] = np.nan
print(df)
print(df.count())

titanic = seaborn.load_dataset('titanic')
print(titanic.head())
# 연습 문제 타이타닉호 승객 데이터의 데이터 개수를 각 열마다 구해본다.
print(titanic.count())

# 카테고리 값 세기
np.random.seed(1)
s2 = pd.Series(np.random.randint(6, size=100))
print(s2.tail())
print(s2.value_counts())
print(df[0].value_counts())  # 데이터프레임에는 value_counts 메서드가 없기에 열별로 적용해야 함

# 정렬
# sort_index로 인덱스 기준 정렬, sort_values 데이터 값 기준
print(s2.value_counts().sort_index())
print(s.sort_values())  # NaN 값의 경우 정렬하면 맨 뒤로
print(s.sort_values(ascending=False))  # 내림차순 정렬
print(df.sort_values(by=1))  # 데이터프레임에서 사용할 경우 by 인수로 정렬의 기준 열을 정해줘야 함
