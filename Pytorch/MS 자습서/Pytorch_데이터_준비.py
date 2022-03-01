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
