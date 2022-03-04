# 이전 단계에서 만든 모델은 .pth 파일이지만, Windows ML 앱과 통합하려면 모델을 ONNX 형식으로 변환해야 함

# 모델 내보내기
# 모델을 내보내기 위해서는 torch.onnx.exxport() 함수를 사용, 모델을 실행하고 출력을 계산하는 데 사용되는 연산자의 추적을 기록

import torch.onnx

# ONNX 파일로 변환하기 위한 함수
def Convert_ONNX():

    # set the model to inference mode
    model.eval()
    input_size = 0
    # 더미 인풋 텐서를 생성
    dummy_input = torch.randn(1, input_size, requires_grad=True)

    # Export the model
    torch.onnx.export(
        model,  # 모델 실행 시작
        dummy_input,  # 모델 인풋 (혹은 멀티플 인풋에 대한 튜플)
        "ImageClassifier.onnx",  # 모델을 저장할 위치
        export_params=True,  # 트레이닝된 파라미터 가중(weights)을 모델 파일 내부에 저장
        opset_version=10,  # the ONNX version to export the model to
        do_constant_folding=True,  # 최적화를 위한 constant folding을 수행할지 여부
        input_names=["modelInput"],  # the model's input names
        output_names=["modelOutput"],  # the model's output names
        dynamic_axes={
            "modelInput": {0: "batch_size"},  # variable length axes
            "modelOutput": {0: "batch_size"},
        },
    )
    print(" ")
    print("Model has been converted to ONNX")


# 메인 함수
if __name__ == "__main__":

    # Let's build our model
    # train(5)
    # print('Finished Training')

    # Test which classes performed well
    # testAccuracy()

    # Let's load the model we just created and test the accuracy per label
    model = Network()
    path = "myFirstModel.pth"
    model.load_state_dict(torch.load(path))

    # Test with batch of images
    # testBatch()
    # Test how the classes performed
    # testClassess()

    # Conversion to ONNX
    Convert_ONNX()
