import torch
import torch.nn as nn  # 신경망 빌드를 위한 모듈, 확장 가능한 클래스 및 신경망을 빌드하는데 필요한 구성요소 포함
import torchvision
import torch.nn.functional as F
from torchvision.datasets import CIFAR10
from torchvision.transforms import transforms
from torch.utils.data import DataLoader

# 데이터 로딩과 일반화(Normalization)
# 트레이닝 셋과 테스트 셋을 위한 transformations 정의
transformations = transforms.Compose(
    [transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]
)

# CIFAR10 데이터셋은 50K개의 트레이닝 이미지로 구성됨, 배치 사이즈를 10으로 정의해서 5000 배치의 이미지를 불러옴
batch_size = 10
number_of_labels = 10

# 트레이닝을 위한 인스턴스 생성
# 아래의 코드를 처음 수행할 때, CIFAR10 트레이닝 데이터셋이 다운로드 될 것임(로컬)
train_sets = CIFAR10(
    root="./data", train=True, transform=transformations, download=True
)

# 트레이닝 셋을 위한 로더를 생성, 로더는 배치 사이즈 단위로 데이터를 읽고 메모리에 저장함
train_loader = DataLoader(
    train_sets, batch_size=batch_size, shuffle=True, num_workers=0
)
print("The number of images in a training set is :", len(train_loader) * batch_size)

# 테스트를 위한 인스턴스 생성, train이 False로 세트되어있음
test_set = CIFAR10(root="./data", train=False, transform=transformations, download=True)

# 테스트 셋을 위한 로더를 생성, 로더는 배치 사이즈 단위로 데이터를 읽고 메모리에 저장함
# shuffle이 False로 세트되어 있는것을 생각하기
test_loader = DataLoader(test_set, batch_size=batch_size, shuffle=False, num_workers=0)
print("The number of images in a test set is :", len(test_loader) * batch_size)

print("The number of batches per epoch is :", len(train_loader))
classes = (
    "plane",
    "car",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck",
)
# Pytorch 데이터 준비 편 끝

# 나선 신경망 정의
"""
나선 계층은 이미지의 특징을 감지하는 데 도움이 되는 CNN의 주요 계층입니다. 
각 계층에는 이미지의 구체적인 특징을 감지하는 채널 수와 감지된 특징의 크기를 정의하는 여러 커널이 있습니다. 
따라서 채널이 64개이고 커널 크기가 3 x 3인 나선 계층은 각각 크기가 3 x 3인 64개의 고유한 특징을 감지합니다. 
나선 계층을 정의할 때 입력 채널 수, 출력 채널 수 및 커널 크기를 제공합니다. 
계층의 출력 채널 수는 다음 계층에 대한 입력 채널 수로 사용됩니다.
예를 들어 입력 채널 수 = 3, 출력 채널 수 = 10 및 커널 크기 = 6인 나선 계층은 RGB 이미지(3개 채널)를 입력으로 받고 
10개의 특징 감지기를 커널 크기가 6x6인 이미지에 적용합니다. 커널 크기가 작을수록 계산 시간과 가중치 공유가 줄어듭니다.
"""
# 합성곱 신경망 정의
class Network(nn.Module):
    def __init__(self):
        super(Network, self).__init__()
        # 인풋 이미지 채널 3, 아웃풋 이미지 채널 12, 5x5 스퀘어 합성곱
        self.conv1 = nn.Conv2d(
            in_channels=3, out_channels=12, kernel_size=5, stride=1, padding=1
        )
        self.bn1 = nn.BatchNorm2d(12)
        self.conv2 = nn.Conv2d(
            in_channels=12, out_channels=12, kernel_size=5, stride=1, padding=1
        )
        # BatchNorm2d 계층은 정규화를 입력에 적용하여 평균 및 단위 분산이 0이 되고 네트워크 정확도를 높입니다.
        self.bn2 = nn.BatchNorm2d(12)
        # MaxPool 계층은 이미지에서 개체의 위치가 특정 특징을 감지하는 신경망의 기능에 영향을 주지 않도록 하는 데 도움이 됩니다.
        self.pool = nn.MaxPool2d(2, 2)
        self.conv4 = nn.Conv2d(
            in_channels=12, out_channels=24, kernel_size=5, stride=1, padding=1
        )
        self.bn4 = nn.BatchNorm2d(24)
        self.conv5 = nn.Conv2d(
            in_channels=24, out_channels=24, kernel_size=5, stride=1, padding=1
        )
        # an affine operation: y = Wx + b
        self.bn5 = nn.BatchNorm2d(24)
        # Linear 계층은 각 클래스의 점수를 계산하는 네트워크의 최종 계층입니다.
        # CIFAR10 데이터 세트에는 10개의 레이블 클래스가 있습니다.
        # 점수가 가장 높은 레이블은 모델에서 예측하는 레이블이 됩니다.
        # 선형 계층에서 클래스 수에 해당하는 입력 특징 수와 출력 특징 수를 지정해야 합니다.
        self.fc1 = nn.Linear(24 * 10 * 10, 10)

    def forward(self, input):
        # relu 계층은 들어오는 모든 특징을 0 이상으로 정의하는 활성화 함수.
        # 이 계층을 적용하면 0보다 작은 숫자는 0으로 변경되고, 나머지는 그대로 유지됩니다.
        output = F.relu(self.bn1(self.conv1(input)))
        output = F.relu(self.bn2(self.conv2(output)))
        output = self.pool(output)
        output = F.relu(self.bn4(self.conv4(output)))
        output = F.relu(self.bn5(self.conv5(output)))
        output = output.view(-1, 24 * 10 * 10)
        output = self.fc1(output)

        return output


# Instantiate a neural network model
model = Network()

# 손실 함수 정의
"""
손실 함수는 출력이 대상과 다른 정도를 예측하는 값을 계산합니다. 
주요 목표는 신경망의 역방향 전파를 통해 가중치 벡터 값을 변경하여 손실 함수의 값을 줄이는 것입니다.

손실 값은 모델 정확도와 다릅니다. 손실 함수를 통해 학습 세트에서 최적화를 반복할 때마다 모델이 얼마나 잘 작동하는지 이해할 수 있습니다. 
모델의 정확도는 테스트 데이터에서 계산되며 올바른 예측의 백분율을 보여 줍니다.
PyTorch에서 신경망 패키지에는 심층 신경망의 구성 요소를 구성하는 다양한 손실 함수가 포함되어 있습니다. 
이 자습서에서는 분류 교차 엔트로피 손실 및 Adam 최적화 도구를 사용하여 손실 함수 정의를 기반으로 하는 분류 손실 함수를 사용합니다. 
lr(학습 속도)은 손실 그라데이션과 관련하여 네트워크의 가중치를 조정하는 정도에 대한 제어를 설정합니다. 
여기서는 0.001로 설정합니다. 이 값이 낮을수록 학습 속도가 느려집니다.
"""
from torch.optim import Adam

# Define the loss function with Classification Cross-Entropy loss and an optimizer with Adam optimizer
loss_fn = nn.CrossEntropyLoss()
optimizer = Adam(model.parameters(), lr=0.001, weight_decay=0.0001)

# 학습 데이터에 대한 모델 학습
"""
모델을 학습시키려면 데이터 반복기를 반복하고, 입력을 네트워크에 공급하고, 최적화해야 합니다. 
PyTorch에는 GPU 전용 라이브러리가 없지만 실행 디바이스를 수동으로 정의할 수 있습니다. 
디바이스가 컴퓨터에 있으면 Nvidia GPU가 되고, 그렇지 않으면 CPU가 됩니다.
"""
from torch.autograd import Variable

# Function to save the model
def saveModel():
    path = "./myFirstModel.pth"
    torch.save(model.state_dict(), path)


# 테스트 데이터셋을 통해 모델을 테스트하고 테스트 이미지의 정확도를 출력하는 함수
def testAccuracy():

    model.eval()
    accuracy = 0.0
    total = 0.0

    with torch.no_grad():
        for data in test_loader:
            images, labels = data
            # 테스트 셋에 대한 모델을 수행하여 labels를 예측함
            outputs = model(images)
            # the label with the highest energy will be our prediction
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            accuracy += (predicted == labels).sum().item()

    # 테스트 이미지에 대한 정확도 계산
    accuracy = 100 * accuracy / total
    return accuracy


# 트레이닝 함수, 데이터를 루프하여 네트워크에 인풋을 주고 최적화를 진행함
def train(num_epochs):

    best_accuracy = 0.0

    # 모델을 수행할 디바이스를 정의
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print("The model will be running on", device, "device")
    # Convert model parameters and buffers to CPU or Cuda
    model.to(device)

    for epoch in range(num_epochs):  # loop over the dataset multiple times
        running_loss = 0.0
        running_acc = 0.0

        for i, (images, labels) in enumerate(train_loader, 0):

            # get the inputs
            images = Variable(images.to(device))
            labels = Variable(labels.to(device))

            # zero the parameter gradients
            optimizer.zero_grad()
            # 트레이닝 셋의 이미지를 통하여 클래스(배, 개...)를 예측함
            outputs = model(images)
            # 모델의 아웃풋과 실제 라벨을 통해 손실율 계산
            loss = loss_fn(outputs, labels)
            # 손실을 역전파(backpropagate)함
            loss.backward()
            # 계산된 기울기(gradients)를 바탕으로 파라미터를 조정함
            optimizer.step()

            # Let's print statistics for every 1,000 images
            running_loss += loss.item()  # extract the loss value
            if i % 1000 == 999:
                # print every 1000 (twice per epoch)
                print("[%d, %5d] loss: %.3f" % (epoch + 1, i + 1, running_loss / 1000))
                # zero the loss
                running_loss = 0.0

        # 각 epoch(10,000 이미지)마다 평균 정확도를 계산하고 출력함
        accuracy = testAccuracy()
        print(
            "For epoch",
            epoch + 1,
            "the test accuracy over the whole test set is %d %%" % (accuracy),
        )

        # 정확도가 가장 높은 모델이라면 저장
        if accuracy > best_accuracy:
            saveModel()
            best_accuracy = accuracy


# 테스트 데이터에 대한 모델 테스트
# 이미지 일괄처리를 통한 모델 테스트 수행
import matplotlib.pyplot as plt
import numpy as np

# 이미지를 출력하기 위한 함수
def imageshow(img):
    img = img / 2 + 0.5  # unnormalize
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show()


# 이미지 배치로 모델틍 테스트하고 라벨 예측을 출력하는 함수
def testBatch():
    # get batch of images from the test DataLoader
    images, labels = next(iter(test_loader))

    # show all images as one image grid
    imageshow(torchvision.utils.make_grid(images))

    # Show the real labels on the screen
    print(
        "Real labels: ", " ".join("%5s" % classes[labels[j]] for j in range(batch_size))
    )

    # Let's see what if the model identifiers the labels of those example
    outputs = model(images)

    # We got the probability for every 10 labels. The highest (max) probability should be correct label
    _, predicted = torch.max(outputs, 1)

    # Let's show the predicted labels on the screen to compare with the real ones
    print(
        "Predicted: ",
        " ".join("%5s" % classes[predicted[j]] for j in range(batch_size)),
    )


# 어떤 클래스의 퍼포먼스가 가장 좋았는지(인식률이 높았는지) 테스트하는 함수
def testClassess():
    class_correct = list(0.0 for i in range(number_of_labels))
    class_total = list(0.0 for i in range(number_of_labels))
    with torch.no_grad():
        for data in test_loader:
            images, labels = data
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)
            c = (predicted == labels).squeeze()
            for i in range(batch_size):
                label = labels[i]
                class_correct[label] += c[i].item()
                class_total[label] += 1

    for i in range(number_of_labels):
        print(
            "Accuracy of %5s : %2d %%"
            % (classes[i], 100 * class_correct[i] / class_total[i])
        )


# 메인 함수
if __name__ == "__main__":

    # Let's build our model
    train(5)
    print("Finished Training")

    # Test which classes performed well
    testAccuracy()

    # 라벨별 정확도를 테스트하는 모델을 로드
    model = Network()
    path = "myFirstModel.pth"
    model.load_state_dict(torch.load(path))

    # Test with batch of images
    testBatch()
    testClassess()
