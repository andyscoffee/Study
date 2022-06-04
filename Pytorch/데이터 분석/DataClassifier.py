import torch
import pandas as pd
import torch.nn as nn
from torch.utils.data import random_split, DataLoader, TensorDataset
import torch.nn.functional as F
import numpy as np
import torch.optim as optim
from torch.optim import Adam

# 붓꽃(Iris) 데이터 불러오기
df = pd.read_excel(
    r'C:\Users\monar\Desktop\Python_Workspace\Study\Pytorch\Iris_dataset.xlsx')
print('Take a look at sample from the dataset:')
print(df.head())

# Let's verify if our data is balanced and what types of species we have
print('\nOur dataset is balanced and has the following values to predict:')
print(df['Iris_Type'].value_counts())

# 붓꽃의 종을 숫자로 표현하기: Iris-setosa=0, Iris-versicolor=1, Iris-virginica=2.
labels = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}
df['IrisType_num'] = df['Iris_Type']   # 새로 "IrisType_num" 열 생성
# 값들을 숫자 형식으로 표현(신경망 학습에 숫자 변수가 필요하기 때문에)
df.IrisType_num = [labels[item] for item in df.IrisType_num]

# 입,출력 정의
# We drop the first column and the two last ones.
input = df.iloc[:, 1:-2]
print('\nInput values are:')
print(input.head())
output = df.loc[:, 'IrisType_num']   # Output Y is the last column
print('\nThe output value is:')
print(output.head())

# 입 출력 데이터를 텐서 데이터셋으로 변환
input = torch.Tensor(input.to_numpy())      # torch.float32 타입의 텐서 생성
# 입력 형식: torch.Size([150, 4]) torch.float32
print('\nInput format: ', input.shape, input.dtype)
output = torch.tensor(output.to_numpy())        # torch.int64 타입 텐서 생성
# 출력 형식: torch.Size([150]) torch.int64
print('Output format: ', output.shape, output.dtype)
# Create a torch.utils.data.TensorDataset object for further data manipulation
data = TensorDataset(input, output)
"""
150개의 입력 값 중 약 60%는 모델 학습 데이터, 유효성 검사에 20%, 테스트에 30%를 유지.
이 자습서에서 훈련 데이터 세트의 배치 크기는 10으로 정의됩니다. 
학습 세트에는 95개의 항목이 있으며, 평균적으로 학습 세트를 한 번 반복(1 Epoch)해야 하는 전체 배치는 9개가 있습니다. 
유효성 검사 및 테스트 세트의 일괄 처리 크기를 1로 유지합니다.
"""

# 데이터를 분할하여 세트를 학습, 검증
# Split to Train, Validate and Test sets using random_split
train_batch_size = 10
# The size of our dataset or the number of rows in excel table.
number_rows = len(input)
test_split = int(number_rows*0.3)
validate_split = int(number_rows*0.2)
train_split = number_rows - test_split - validate_split
train_set, validate_set, test_set = random_split(
    data, [train_split, validate_split, test_split])

# Create Dataloader to read the data within batch sizes and put into memory.
train_loader = DataLoader(train_set, batch_size=train_batch_size, shuffle=True)
validate_loader = DataLoader(validate_set, batch_size=1)
test_loader = DataLoader(test_set, batch_size=1)
