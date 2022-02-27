from numpy.core.numeric import ones_like
import torch
import numpy as np
from torch import torch_version

x = torch.rand(5, 3)
print(x)
torch.cuda.is_available()

# 텐서 초기화
data = [[1, 2], [3, 4]]
x_data = torch.tensor(data)  # 데이터로부터 직접 생성, 데이터의 자료형은 자동으로 유추
np_arr = np.array(data)
x_np = torch.from_numpy(np_arr)  # Numpy 배열로부터 생성(반대도 가능)

# 다른 텐서로부터 생성(명시적으로 재정의(override)하지 않는다면, 인자로 주어진 텐서의 속성(모양(shape), 자료형(datatype))을 유지)
x_ones = torch.ones_like(x_data)  # x_data의 속성 유지
print("Ones data :\n", x_ones)
x_rand = torch.rand_like(x_data, dtype=torch.float)  # x_data의 속성을 덮어씀
print("Rand data :\n", x_rand)


# 무작위 또는 상수 값을 사용(shape는 텐서의 차원(dimension)을 나타내는 튜플, 출력 텐서의 차원을 결정)
shape = (
    2,
    3,
)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)
print("Random Tensor :\n", rand_tensor)
print("Ones Tensor :\n", ones_tensor)
print("Zeros Tensor :\n", zeros_tensor)

# 텐서의 속성
# 텐서의 속성은 텐서의 모양(shape), 자료형 및 어느 장치에 저장되는지를 나타냄
tensor = torch.rand(3, 4)
print("Shape of tensor :\n", tensor.shape)
print("Datatype of tensor : \n", tensor.dtype)
print("Device of tensor is stored on :\n", tensor.device)

# 텐서 연산
"""
전치, 인덱싱, 슬라이싱, 수학 계산, 선형 대수, 임의 샘플링(random sampling) 등, 100가지 이상의 텐서 연산 존재
각 연산들은 (일반적으로 CPU보다 빠른) GPU에서 실행할 수 있습니다. Colab을 사용한다면, Edit > Notebook Settings 에서 GPU를 할당할 수 있습니다.
기본적으로 텐서는 CPU에 생성됩니다. .to 메소드를 사용하면 (GPU의 가용성(availability)을 확인한 뒤) GPU로 텐서를 명시적으로 이동할 수 있습니다. 
장치들 간에 큰 텐서들을 복사하는 것은 시간과 메모리 측면에서 비용이 많이든다는 것을 기억하세요!
"""
if torch.cuda.is_available():
    tensor = tensor.to("cuda")

# Numpy식 표준 인덱싱과 슬라이싱
tensor = torch.ones(4, 4)
print("First row: ", tensor[0])
print("First column: ", tensor[:, 0])
print("Last column:", tensor[..., -1])
tensor[:, 1] = 0
print(tensor)

# 텐서 합치기
# torch.cat을 사용하여 주어진 차원에 따라 일련의 텐서 연결 가능, 조금 다른 결합 연산인 torch.stack도 확인하기
t1 = torch.cat([tensor, tensor, tensor], dim=1)
print(t1)
t2 = torch.stack([tensor, tensor, tensor], dim=1)

# 산술 연산
# 두 텐서 간의 행렬 곱을 계산하기, y1~y3는 전부 같은 값을 가짐
y1 = tensor @ tensor.T
y2 = tensor.matmul(tensor.T)
y3 = torch.rand_like(tensor)
torch.matmul(tensor, tensor.T, out=y3)

# 요소별 곱(element-wise product)을 계산하기, z1~z3는 전부 같은 값을 가짐
z1 = tensor * tensor
z2 = tensor.mul(tensor)
z3 = torch.rand_like(tensor)
torch.mul(tensor, tensor, out=z3)

# 단일 요소 텐서
# 텐서의 모든 값을 하나로 집계(aggregate)하여 요소가 하나인 텐서의 경우, item()을 사용해서 Python 숫자로 변환 가능
agg = tensor.sum()
agg_item = agg.item()
print(agg_item, type(agg_item))

# 바꿔치기(in-place) 연산
"""
연산 결과를 피연산자에 저장하는 연산을 바꿔치기 연산이라고 부름, _접미사를 가짐 ex)x.copy_(y)나  x.t_()는 x를 변경함
바꿔치기 연산은 메모리를 일부 절약하지만, 기록(history)이 즉시 삭제되어 도함수(derivative) 계산에 문제가 발생할 수 있습니다.
따라서, 사용을 권장하지 않습니다.
"""
print("\n바꿔치기(in-place) 연산")
print(tensor, "\n")
tensor.add_(5)
print(tensor)


# Numpy 변환(Bridge)
# CPU 상의 텐서와 Numpy 배열은 메모리 공간을 공유하기 때문에, 하나를 변경하면 다른 하나도 변경됨

# 텐서를 Numpy 배열로 변환
print("\nNumpy 변환(Bridge)")
t = torch.ones(5)
print("t :\n", t)
n = t.numpy()
print("n :\n", n)
t.add_(1)
print("t :\n", t)
print("n :\n", n)

# Numpy 배열을 텐서로 변환
n = np.ones(5)
t = torch.from_numpy(n)
np.add(n, 1, out=n)
print("t :\n", t)
print("n :\n", n)
