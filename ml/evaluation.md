- [Metrics](#metrics)
  - [Confucion Matrix](#confucion-matrix)
  - [Accuracy](#accuracy)
  - [Precision](#precision)
  - [Recall / Sensitivity](#recall--sensitivity)
  - [F1](#f1)
  - [Fall-out](#fall-out)
  - [ROC Curve](#roc-curve)
  - [AUC Curve](#auc-curve)

# Metrics

## Confucion Matrix

Ref: https://sumniya.tistory.com/26

```python
import numpy as np
# class 0: 6 / class 1: 10 / class 2: 9
target = np.array([0] * 6 + [1] * 10 + [2] * 9)
pred = np.array([0, 0, 0, 0, 1, 2] + [0, 0, 0, 0, 0, 0, 1, 1, 2, 2] + [0, 0, 0, 2, 2, 2, 2, 2, 2])


# target
K = len(np.unique(target))
confusion_matrix = np.zeros((K, K), dtype=np.int32)
for p, t in zip(pred, target):
    confusion_matrix[p, t] += 1
print(confusion_matrix)
#       Target
#      [[4 6 3]
# Pred  [1 2 0]
#       [1 2 6]]
```

| | Positive | Negative |
|---|---|---|
|Positive| True Positive | False Negative |
|Negative| False Positive | True Negative |

- Row = Target / Column = Predict
- 해석: 해야할 것(Positive/Negative)을 맞게/틀리게(True/False) 했다.

## Accuracy

전체 맞게 예측한 비율 = (TP + TN) / (TP + TN + FN + FP) 
- Total Accuracy= (4 + 2 + 6) / 25 

## Precision

Positive 라고 예측한 것 중에서 정말로 맞게 예측한 비율 = TP / (TP + FP)
- Class 0 Precision = 4 / (4 + 6 + 3) 
- Class 1 Precision = 2 / (1 + 2 + 0)
- Class 2 Precision = 6 / (1 + 2 + 6)
- Macro Precision = mean( Class k Precision )
- Python

    ```python
    precisions = confusion_matrix[[0, 1, 2], [0, 1, 2]] / confusion_matrix.sum(1)
    print(precisions.round(4))
    print(f"Macro Precision {(precisions / len(precisions)).sum():.4f}")
    # [0.3077 0.6667 0.6667]
    # Macro Precision 0.5470
    ```

## Recall / Sensitivity

실제 Positive 인것 중에 맞게 예측한 비율 = TP / (TP + FN)
- Class 0 Recall = 4 / (4 + 1 + 1) 
- Class 1 Recall = 2 / (6 + 2 + 2)
- Class 2 Recall = 6 / (3 + 0 + 6)
- Macro Recall = mean( Class k Recall )
- Python

    ```python
    recalls = confusion_matrix[[0, 1, 2], [0, 1, 2]] / confusion_matrix.sum(0)
    print(recalls.round(4))
    print(f"Macro Recall {(recalls / len(recalls)).sum():.4f}")
    # [0.6667 0.2    0.6667]
    # Macro Precision 0.5111
    ```

## F1

`Precision` 과 `Recall`의 조화 평균, 데이터 분포가 불균형 일때 사용, 큰 비중이 끼치는 bias 가 줄어듦
- = 2 * ( 1 / (1/Precision + 1/Recall) ) = 2 * Precision * Recall / (Precision + Recall)
- Python

    ```python
    f1 = 2 * precisions * recalls / (precisions + recalls)
    print(f1.round(4))
    print(f"Total F1 {(f1 / len(f1)).sum():.4f}")
    # [0.4211 0.3077 0.6667]
    # Total F1 0.4651
    ```

## Fall-out

False Positive Rate, Negative라고 예측했는데 실제로 Positive라고 맞춘 비율 = FP / (TN + FP)
- Class 0 Fall-out = (1 + 1) / ((2 + 0 + 2 + 6) + (1 + 1))
- Class 1 Fall-out = (6 + 2) / ((4 + 3 + 1 + 6) + (6 + 2))
- Class 2 Fall-out = (3 + 0) / ((4 + 6 + 1 + 2) + (3 + 0))
- Specificity = 1 - Fall-out Rate = FN / (TN + FP): Negative 라고 예측한 것 중에 실제로 Negative라고 잘 맞춘 비율


## ROC Curve

Receiver Operating Characteristic Curve, Sensitivity / Fall-out rate 의 비율
- X 축: Fall-out(FP rate), Y 축: Sensitivity(TP rate)
- Recall이 크고 Fall-out이 작은 것이 좋음, 좌상단 = max

## AUC Curve

Area Under Curve, ROC Curve 아래의 면적, 최대값 = 1
