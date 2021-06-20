

# Cross validation

# Overfitting / Underfitting, Regularization

# Ensemble (bagging, boosting)

머신러닝에서 앙상블 학습이란 하나의 학습 알고리즘 보다 더 좋은 성능을 내기 위해 다수의 약한 성능을 가진 학습 알고리즘(약한 학습자(Weak Learner))을 합쳐서 사용하는 방법이다. 

- Bagging(Bootstrap Aggregation): 샘플을 여러번 뽑아(Bootstrap)서 여러 개의 약한 학습자를 병렬적으로 학습시켜 결과물을 집계(Aggregration)하는 방법. 결과물을 집계하는 방법으로 회귀 문제의 경우 평균을 내거나, 분류 문제의 경우 가장 많이 나온 클래스로 투표(Hard Voting) 혹은 클래스의 확률을 평균화해서 가장 높은 확률로 도출(Soft Voting)한다. 모델의 variance를 줄이는 방향을 원한다면 배깅방법이 적합하다.

- Boosting: 훈련 데이터를 샘플링하여 순차적으로 약한 학습자를 하나씩 추가시키면서 학습한다. 각 약한 학습자들은 가중치로 연결된다는 것이 특징이다. 다만 이전 약한 학습자가 틀린 데이터의 샘플링이 더 잘 되게 가중치를 부여하여 훈련 데이터를 생성하고 다시 학습한다. 모델의 bias를 줄이는 방향을 생각하고 있다면, 부스팅 방법이 적합하다.