"""
import io
import numpy as np

from torch import nn
import torch.utils.model_zoo as model_zoo
import torch.onnx

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


def convert(): 
    model_url = 'Netmodel_DC.pth'
    batch_size = 1    # 임의의 수

    map_location = lambda storage, loc: storage
    if torch.cuda.is_available():
        map_location = None
    torch_model.load_state_dict(model_zoo.load_url(model_url, map_location=map_location))

# 모델을 추론 모드로 전환합니다
    torch_model.eval()
    출처: https://eehoeskrap.tistory.com/468 [Enough is not enough:티스토리] 

    # Let's create a dummy input tensor  
    dummy_input = torch.randn(1, 3, 32, 32, requires_grad=True)  

    # Export the model   
    torch.onnx.export(model,         # model being run 
         dummy_input,       # model input (or a tuple for multiple inputs) 
         "Network.onnx",       # where to save the model  
         export_params=True,  # store the trained parameter weights inside the model file 
         opset_version=11,    # the ONNX version to export the model to 
         do_constant_folding=True,  # whether to execute constant folding for optimization 
         input_names = ['input'],   # the model's input names 
         output_names = ['output'], # the model's output names 
         dynamic_axes={'input' : {0 : 'batch_size'},    # variable length axes 
                                'output' : {0 : 'batch_size'}}) 
    print(" ") 
    print('Model has been converted to ONNX') 



# 메인 함수(모델 학습 시작-> 모델 저장 ->결과 표시)
if __name__ == "__main__":
    convert()
"""
# 데이터 학습 없이 모델 url로 모델을 불러와서 ONNX파일로 변환하는 법 공부 중
