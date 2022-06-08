import torch
import pandas as pd
import torch.nn as nn
from torch.utils.data import random_split, DataLoader, TensorDataset
import torch.nn.functional as F
import numpy as np
import torch.optim as optim
from torch.optim import Adam
# ONNX관련 새로 임포트한 것들
import io
import torch.utils.model_zoo as model_zoo
import torch.onnx

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

# Day 2

"""
이 자습서에서는 세 개의 선형 계층을 사용하여 기본 신경망 모델을 빌드합니다. 모델의 구조는 다음과 같습니다.
Linear -> ReLU -> Linear -> ReLU -> Linear
선형 계층은 들어오는 데이터에 선형 변환을 적용합니다. 클래스 수에 해당하는 입력 기능 수와 출력 기능 수를 지정해야 합니다.
ReLU 계층은 들어오는 모든 기능을 0 이상으로 정의하는 활성화 함수입니다. 
따라서 ReLU 계층이 적용될 때 0보다 작은 숫자는 0으로 변경되고, 나머지는 그대로 유지됩니다. 
두 개의 숨겨진 계층에 활성화 계층을 적용하고 마지막 선형 계층에는 활성화를 적용하지 않을 것입니다.
"""
# 1. 모델의 매개변수와 신경망 정의

# 모델의 매개변수 정의, 입력 크기는 모델을 제공하는 기능 수에 따라 달라짐
input_size = list(input.shape)[1]  # = 4

learning_rate = 0.01  # 학습 속도는 손실 그라데이션 관련 네트워크 가중치를 조정하는 정도에 따라 달라짐, 값이 낮을수록 학습 속도가 느려짐
output_size = len(labels)  # 세가지 종류의 붓꽃이 있기에 출력 크기는 3


# 신경망 정의
class Network(nn.Module):
    def __init__(self, input_size, output_size):
        super(Network, self).__init__()

        self.layer1 = nn.Linear(input_size, 24)
        self.layer2 = nn.Linear(24, 24)
        self.layer3 = nn.Linear(24, output_size)

    def forward(self, x):
        x1 = F.relu(self.layer1(x))
        x2 = F.relu(self.layer2(x1))
        x3 = self.layer3(x2)
        return x3


# Instantiate the model
model = Network(input_size, output_size)

# 2. 실행 디바이스 정의(PC에서 실행 가능한 디바이스, Nvidia GPU가 있으면 GPU, 없으면 CPU)
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print("The model will be running on", device, "device\n")
model.to(device)    # Convert model parameters and buffers to CPU or Cuda

# 3. 모델을 저장하는 함수 정의


def saveModel():
    path = "./NetModel.pth"
    torch.save(model.state_dict(), path)


# 손실 함수와 최적화 도구 정의(torch.nn 패키지에서 제공하는 함수 이용)
loss_fn = nn.CrossEntropyLoss()
optimizer = Adam(model.parameters(), lr=0.001, weight_decay=0.0001)

# 학습 데이터에 대한 모델 학습
"""
모델을 학습하기 위해 데이터 반복기를 반복, 입력을 신경망 네트워크에 공급, 최적화 해야함
결과의 유효성을 검증하기 위해 예측 레이블을 모든 학습 Epoch 이후 유효성 검사 데이터 세트의 실제 레이블과 비교
"""
# 학습 함수


def train(num_epochs):
    best_accuracy = 0.0

    print("Begin training...")
    for epoch in range(1, num_epochs+1):
        running_train_loss = 0.0
        running_accuracy = 0.0
        running_vall_loss = 0.0
        total = 0

        # Training Loop
        for data in train_loader:
            # for data in enumerate(train_loader, 0):
            # get the input and real species as outputs; data is a list of [inputs, outputs]
            inputs, outputs = data
            optimizer.zero_grad()   # 매개변수의 기울기를 0으로 설정
            predicted_outputs = model(inputs)   # 모델로 추측한 결과값
            # 예측 아웃풋으로부터 손실 계산
            train_loss = loss_fn(predicted_outputs, outputs)
            train_loss.backward()   # 손실을 역전파
            optimizer.step()        # 계산된 기울기를 기반으로 매개변수 조정
            running_train_loss += train_loss.item()  # 손실값을 추적함

        # training loss value을 계산
        train_loss_value = running_train_loss/len(train_loader)

        # Validation Loop
        with torch.no_grad():
            model.eval()
            for data in validate_loader:
                inputs, outputs = data
                predicted_outputs = model(inputs)
                val_loss = loss_fn(predicted_outputs, outputs)

                # 가장 높은 값(Value)을 가진 레이블이 예측값(Prediction)
                _, predicted = torch.max(predicted_outputs, 1)
                running_vall_loss += val_loss.item()
                total += outputs.size(0)
                running_accuracy += (predicted == outputs).sum().item()

        # validation loss value 계산
        val_loss_value = running_vall_loss/len(validate_loader)

        # 배치별 옳은 예측의 수를 총 예측한 수로 나누어 정확도를 계산함
        accuracy = (100 * running_accuracy / total)

        # 정확도가 가장 높은 경우의 모델을 저장함
        if accuracy > best_accuracy:
            saveModel()
            best_accuracy = accuracy

        # Print the statistics of the epoch
        print('Completed training batch', epoch, 'Training Loss is: %.4f' % train_loss_value,
              'Validation Loss is: %.4f' % val_loss_value, 'Accuracy is %d %%' % (accuracy))


"""
테스트 데이터에 의한 모델 테스트 단계
모델 학습 이후 테스트 데이터 세트를 통해 모델을 테스트함
"""
# 모델을 테스트하기 위한 함수


def test():
    # 트레이닝 루프에서 저장한 모델을 불러옴
    model = Network(input_size, output_size)
    path = "NetModel.pth"
    model.load_state_dict(torch.load(path))

    running_accuracy = 0
    total = 0

    with torch.no_grad():
        for data in test_loader:
            inputs, outputs = data
            outputs = outputs.to(torch.float32)
            predicted_outputs = model(inputs)
            _, predicted = torch.max(predicted_outputs, 1)
            total += outputs.size(0)
            running_accuracy += (predicted == outputs).sum().item()

        print('Accuracy of the model based on the test set of', test_split,
              'inputs is: %d %%' % (100 * running_accuracy / total))


# Optional: 어떤 종이 예측하기 쉬웠는지(각 종을 성공적으로 분류하는 확률을 예측하는 모델의 신뢰도를 테스트하는 함수)
def test_species():
    # 트레이닝 루프에서 저장한 모델을 불러오기
    model = Network(input_size, output_size)
    path = "NetModel.pth"
    model.load_state_dict(torch.load(path))

    labels_length = len(labels)  # 얼마나 많은 레이블(종류)? = 3 in our database.

    # 옳은 레이블(각 종류별로 얼마나 많이 맞췄는지)을 계산하기 위한 리스트
    labels_correct = list(0. for i in range(labels_length))
    # 타입별 총 레이블의 수를 저장하기 위한 리스트 [total setosa, total versicolor, total virginica]
    labels_total = list(0. for i in range(labels_length))

    with torch.no_grad():
        for data in test_loader:
            inputs, outputs = data
            predicted_outputs = model(inputs)
            _, predicted = torch.max(predicted_outputs, 1)

            label_correct_running = (predicted == outputs).squeeze()
            label = outputs[0]
            if label_correct_running.item():
                labels_correct[label] += 1
            labels_total[label] += 1

    label_list = list(labels.keys())
    for i in range(output_size):
        print('Accuracy to predict %5s : %2d %%' %
              (label_list[i], 100 * labels_correct[i] / labels_total[i]))

# Day 3
# 기계 학습 모델(.pth파일)을 Windows ML앱과 통합하기 위해 모델을 ONNX 형식으로 변환하기

# ONNX 형식으로 변환하기 위한 함수


# Function to Convert to ONNX
def convert():

    # set the model to inference mode
    model.eval()

    # Let's create a dummy input tensor
    dummy_input = torch.randn(1, 3, 32, 32, requires_grad=True)

    # Export the model
    torch.onnx.export(model,         # model being run
                      # model input (or a tuple for multiple inputs)
                      dummy_input,
                      "Network.onnx",       # where to save the model
                      export_params=True,  # store the trained parameter weights inside the model file
                      opset_version=11,    # the ONNX version to export the model to
                      do_constant_folding=True,  # whether to execute constant folding for optimization
                      input_names=['input'],   # the model's input names
                      output_names=['output'],  # the model's output names
                      dynamic_axes={'input': {0: 'batch_size'},    # variable length axes
                                    'output': {0: 'batch_size'}})
    print(" ")
    print('Model has been converted to ONNX')


# 메인 함수(모델 학습 시작-> 모델 저장 ->결과 표시)
if __name__ == "__main__":
    num_epochs = 10
    train(num_epochs)
    print('Finished Training\n')
    test()
    test_species()
    convert()
