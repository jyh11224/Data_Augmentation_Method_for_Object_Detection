# Data_Augmentation_Method_for_Object_Detection

## Abstract
딥러닝 기반의 영상 처리 기술이 발전하면서 객체 탐지나 추적 기능을 통한 무인 장비의 자동화된 상황 인식 및 대응 능력이 크게 향상되고 있다. 그러나, 인식하기 쉬운 일반적인 객체에 비해 위장된 객체는 주변 환경과 색상, 질감, 패턴 등이 유사하여 배경과 객체를 구별하기 어렵다. 본 연구에서는 위장 객체 탐지를 위한 데이터 증강 기법을 제안한다. 제안한 데이터 증강 기법을 사용하여 위장된 객체와 유사한 배경에서도 객체를 식별할 수 있도록 고안하였다. 제안 방법의 평가는 기존 데이터 증강 기법과 비교하였고, 그 결과 AP50에서는 96.7%, AP50:95에서는 67.8%의 정확도를 보여 효과적인 위장 객체 탐지 성능을 확인하였다.



## Installation
Docker environment (recommended)

<details><summary> <b>Expand</b> </summary>
 
``` shell
# create the docker image using Dockerfile
docker build -t image_name .

# create the docker container
docker run -it --gpus all --name container_name -v local_folder_path/:/workspace image_name

# go to required packages folder
cd workspace/AICC

# pip install required packages 
pip install -r requirements.txt

```

</details>

## Evaluation
