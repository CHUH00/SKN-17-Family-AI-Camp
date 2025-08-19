# 🟦 SK네트웍스 Family AI 캠프 17기 2차 프로젝트_ 4Team 🟦


#  1. 팀 소개
### ▶️ 팀명 :  **공공삼**

#### '공공삼'은 00년생 3명과 03년생 1명이 하나가 되어 팀을 이루었다는 뜻과 세 가지 '공'인 공유, 공감, 공조를 핵심가치로 조화로운 팀을 이루겠다는 의미를 담았습니다. 

<br>

### ▶️ 팀원 소개 
|[김주영](https://github.com/samkim7788)|[전상아](https://github.com/sang-a-le)|[조해리](https://github.com/Haer111)|[최우진](https://github.com/CHUH00)|
|:---|:---|:---|:---|
|<img width="100" height="100" src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-2nd-4Team/blob/main/image/%EB%B8%8C%EB%A0%88%EB%93%9C.png" />|<img width="100" height="100" src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-2nd-4Team/blob/main/image/%EB%B0%80%ED%81%AC.png" />|<img width="100" height="100" src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-2nd-4Team/blob/main/image/%EC%B4%88%EC%BD%94.png" />|<img width="100" height="100" src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-2nd-4Team/blob/main/image/%EA%B0%90%EC%9E%90%EC%B9%A9.png" />|

<br>

-----

# 2. 프로젝트 개요

### ▶️ 프로젝트 명 

### **🏃‍♀️‍➡️떠날까? 말까?🏃‍♀️**
#### SNS 사용자 데이터를 기반으로 '페이스북' 이탈 가능성 예측 모델 및 예측 서비스 제공

<br>

-----

### ▶️ 프로젝트 소개 
해당 프로젝트는 SNS 사용자 데이터를 기반으로 개인 특성을 분석하여 향후 플랫폼 이탈 가능성 예측한다. 
특히, 페이스북을 1순위로 선택한 사용자를 기반으로 페이스북 사용자 이탈 모델을 학습해 향후 사용자 특성 데이터를 기반으로 잠재적 이탈자 판별 서비스 제공을 목표로 한다. 

<br>

-----

### ▶️ 프로젝트 배경
<br>

<img width="551" height="210" alt="image" src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-2nd-4Team/blob/main/image/image_2/%EA%B8%B0%EC%82%AC%20%EC%BA%A1%EC%B2%98.png" />

> https://www.chosun.com/economy/tech_it/2023/03/10/NEL65GJO2ZGUXJHVGNCAC4Y354/


> 국내 페이스북 월 이용자가 처음으로 1000만명 이하로 떨어졌다. 사진이나 짧은 동영상 위주의 소셜미디어를 선호하는 10·20대 이용자의 이탈이 가속화하고 있기 때문으로 풀이된다.

> 조선일보, 변희원, 2023.03.10


위의 기사 내용과 같이 2023년 국내 페이스북 월 이용자가 처음으로 1000만명 이하로 떨어지는 등 페이스북 사용자가 지속적으로 감소하는 양상을 보이고 있습니다. 

<br>
<br>

<img width="500" height="300" src='https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-2nd-4Team/blob/main/image/%ED%8E%98%EC%9D%B4%EC%8A%A4%EB%B6%81%20%EC%9D%B4%EC%9A%A9%20%EA%B7%B8%EB%9E%98%ED%94%84%201.jpg'>

> https://www.i-boss.co.kr/ab-6141-59928

> 출처 : 오픈서베이 소셜미디어·검색포털 트렌드 리포트 2023

위의 그래프는 2023년 발표된 오픈서베이의 소셜미디어·검색포털 트렌드 리포트에서 발표된 그래프이다. 
최근 일주일 내 사용한 소셜네트워크 시스템 순위 중 페이스북이 22.6%로 7위를 기록하는 등 동일한 리포트에서 2019년 3위를 기록했던 것에 비해 많이 떨어진 순위를 보이고 있습니다.

<br>
<br>

<img width="600" height="450" alt="image" src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-2nd-4Team/blob/main/image/image_2/%EA%B7%B8%EB%9E%98%ED%94%84%202.png" />

> https://www.wiseapp.co.kr/insight/detail/517

> 출처 : 2024. 와이즈앱·리테일 '희비 엇갈린 SNS 앱 인스타그램 vs 페이스북 비교'

<br>
<br>

|<img width="600" height="300" alt="image" src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-2nd-4Team/blob/main/image/image_2/%EA%B7%B8%EB%9E%98%ED%94%84%20%ED%91%9C%201.png" />|<img width="600" height="300" alt="image" src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-2nd-4Team/blob/main/image/image_2/%EA%B7%B8%EB%9E%98%ED%94%84%20%ED%91%9C%202.png" />|
|:---|:---|
| 페이스북 앱 사용자 및 사용시간 추이 | 인스타그램, 페이스북 앱 월간 사용자 추이 |

<br>

위의 그래프둘에서 확인된 바와 같이 페이스북의 사용 추이가 지속적으로 감소되고 있습니다. 

#### 현재 2030 세대의 경우, 학창시절 페이스북을 가장 주된 SNS로 사용했던 세대이기도 하지만 페이스북 이탈률이 가장 많은 세대라는 것을 확인할 수 있습니다. 

#### 과거 많은 파급력을 주었던 페이스북의 사용자 감소에 대한 의문이 해당 프로젝트 주제 선정에 영향을 주었고, 이에 따라 저희는 SNS 사용자의 개인 특성 데이터를 기반으로 페이스북 이탈률 예측을 하고자 합니다. 

<br>
<br>

-----

### ▶️ 프로젝트 목표 
#### 1. 사용자 특성 데이터를 이용한 페이스북 사용자 이탈률 파악
#### 2. 실제 데이터 주입 시 이탈률 예측
#### 3. 페이스북 외의 다른 SNS의 이탈률 파악으로 인사이트 확장


<br>
<br>

-----

### ▶️ 수집데이터 설명
[미디어통계포털 미디어패널조사]
- 출처 : 미디어 통계 포털(https://stat.kisdi.re.kr/)
- 수집 방법 : 미디어 통계 포털에서 제공하는 연도별 한국 미디어 패널 조사 데이터셋 csv 파일 다운로드.
- 데이터 출처 및 범위
    - 수집 데이터 기간: 2019년 1월 ~ 2024년 12월
    - 데이터 범위 : 개인 정보 및 미디어 이용 중 SNS 사용 관련 질문 
    - 주요 변수 : SNS 사용 빈도, 개인정보(나이, 성별, 학력, 결혼 여부, 종교, 수입 등), 사용하는 SNS 종류
- 설명 
    : 미디어 통계 포털에서 이루어진 한국 미디어 패널 조사 데이터셋을 분석하여 고객의 다양한 특성(나이, 성별, 학력, 결혼 여부, 종교, 수입 등)과 SNS 사용 빈도 관련 설문 데이터에 따른 페이스북 이탈 가능성을 예측

<br>
<br>

-----

# 3. 기술 스택
|개발도구|협업도구|프로그래밍 언어|데이터 전처리|데이터 시각화|머신러닝|
|---|---|---|---|---|---|
|vscode|Github|Python|Pandas / numpy|Matplotlib / seabon|scikit learn|
| <img src='https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white'>|<img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"> <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">|<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">|<img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white"> <img src='https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white'>|<img src='https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black'> <img src='https://img.shields.io/badge/seaborn-31859C?style=for-the-badge&logo=Seaborn&logoColor=white'> | <img src="https://img.shields.io/badge/Scikit-learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>|

<br>
<br>

-----

# 4. WBS
![WBS이미지2](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-2nd-4Team/blob/main/image/WBS_2.png)

<br>
<br>

-----

# 5. 데이터 전처리 결과서 (EDA)

## 👉 최종 데이터 (19년도 /24년도, 2개년 비교)
### 🔹 1. 데이터 로드 
```python
df = pd.read_csv('./data/p19v31_KMP_csv.csv', encoding='CP949')

feature = ['pid', 'p19age', 'p19gender', 'p19school', 'p19mar', 'p19job1', 'p19job2', 'p19job4', 'p19income', 'p19relig2', 'p19d27001', 'p19d27002', 'p19d27003', 'p19d27004', 'p19d11002', 'p19d11004', 'p19d11006']

df_19 = df[feature].copy()

df_19.rename(
    columns={
        'p19age': 'age', 
        'p19gender': 'gender', 
        'p19school': 'school', 
        'p19mar': 'mar', 
        'p19job1': 'job', 
        'p19job2': 'job_o',
        'p19job4': 'job_x',
        'p19income': 'income', 
        'p19relig2': 'relig',
        'p19d27001': 'd01', 
        'p19d27002': 'd02', 
        'p19d27003': 'd03', 
        'p19d27004': 'd04',
        'p19d11002': 'label_1',
        'p19d11004': 'label_2', 
        'p19d11006': 'label_3'
    }, inplace=True
)

df_19['year'] = 2019

df_19.head()
```
<img width="1303" height="193" alt="image" src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-2nd-4Team/blob/main/image/image_2/%EC%A0%84%EC%B2%98%EB%A6%AC%201.png" />

<br>
<br>

### 🔹 2. 변수 변환
#### * 유/무직자 컬럼 병합 및 정제
```python
# 유직자 번호 변경
df_all['job_o'] = df_all['job_o'].replace({'1': '5', '2': '6', '3': '7', '4': '2', '9999': '8'})
print(df_all['job_o'].value_counts())
```

<br>

#### * 데이터 맵핑
  - 데이터 사용 빈도에 대해 맵핑
  
  |<img width="238" height="176" alt="image" src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-2nd-4Team/blob/main/image/image_2/%EB%A7%B5%ED%95%911.png" /> | <img width="238" height="176" alt="image" src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-2nd-4Team/blob/main/image/image_2/%EB%A7%B5%ED%95%912.png" />|
  |---|---|
  |기존값|맵핑 후|

<br>

#### * 라벨데이터 재생성
```python
# 라벨 기초 데이터 변환
df_24['label'] = (df_24[['label_1', 'label_2', 'label_3']].isin(['2']).any(axis=1).astype(int))
print(sum(df_24['label'] == 1), sum(df_24['label'] == 0))
```

<br>

#### * 이탈(churn) 변수 정의
```python
# label의 다음 연도 값
df_all['next_year_label'] = df_all.groupby('pid')['label'].shift(-1)
df_all

# 라벨 데이터 생성 = 이탈(churn) 여부 정의 
churn_conditions = [
    (df_all['label'] == 1) & (df_all['next_year_label'].notna()) & (df_all['next_year_label'] != 1),
    (df_all['label'] == 1) & (df_all['next_year_label'].notna()) & (df_all['next_year_label'] == 1)
]
churn_choices = [1, 0] # 1: 이탈 (Churn), 0: 비이탈 (Not Churn)

df_all['churn'] = np.select(churn_conditions, churn_choices, default=np.nan)
```

<br>

#### * 결측치 제거
```python
df_all = df_all[df_all['label'].str.strip() != ''].reset_index(drop=True)
```

<br>

#### * 필터링
```python
df_model_base = df_all[df_all['churn'].notna()].copy() # 'churn'값이 NaN이 아닌 경우 필터링
```

<br>
  
#### * 2개년 기초 데이터 
<img width="500" height="198" alt="image" src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-2nd-4Team/blob/main/image/image_2/%EC%A0%84%EC%B2%98%EB%A6%AC%202%EA%B0%9C%EB%85%84%20%EA%B8%B0%EC%B4%88.png" />

<br>
<br>

#### * 24년도 변수 변경 내용 컬럼 추가
<img width="1540" height="198" alt="image" src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-2nd-4Team/blob/main/image/image_2/%EC%A0%84%EC%B2%98%EB%A6%AC%20%EC%BB%AC%EB%9F%BC%20%EC%B6%94%EA%B0%80.png" />

→ 총 31개 피처, 1712개 로우 수 생성

<br>
<br>

### 🔹3. EDA

#### * 파생 변수 추가
```python
# 2. 변화량(차이) 파생변수 생성
df_final['d01_change'] = df_final['d01_y'] - df_final['d01_x']
df_final['d02_change'] = df_final['d02_y'] - df_final['d02_x']
df_final['d03_change'] = df_final['d03_y'] - df_final['d03_x']
df_final['d04_change'] = df_final['d04_y'] - df_final['d04_x']
df_final['income_change'] = df_final['income_y'] - df_final['income_x']
df_final['job_change'] = (df_final['job_y'] != df_final['job_x']).astype(int)  # 직업 변동 여부
```
<br>

#### * 변수별 상관계수 
<img width="600" height="550" alt="image" src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-2nd-4Team/blob/main/image/image_2/%EC%83%81%EA%B4%80%EA%B3%84%EC%88%98.png" />

<br>

→ 모델 성능 추출 간 변화 내용 없음. 파생변수 미사용.

<br>
<br>

#### * 중요도 추출
<img width="500" height="600" alt="image" src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-2nd-4Team/blob/main/image/image_2/%EC%A4%91%EC%9A%94%EB%8F%84.png" />


 
<br>
<br>

-----

# 6. 인공지능 학습 결과서 

### 🔹1. 최초 학습 - RandomForest
```python
# 파라미터 최적화
param_grid = {
    'n_estimators': [100, 200, 300],      
    'max_depth': [3, 4, 5],               
    'min_samples_split': [5, 8, 10],      
    'min_samples_leaf': [1, 3, 5],                
    'max_features': ['sqrt', 'log2', None]
}

model = RandomForestClassifier(random_state=42)

grid_search = GridSearchCV(model, param_grid, cv=5, scoring='roc_auc')

grid_search.fit(X_train, y_train)
grid_search.best_params_

best_random_clf = grid_search.best_estimator_

y_pred_train = best_random_clf.predict(X_train)
y_prob_train = best_random_clf.predict_proba(X_train)[:, 1]

y_pred_test = best_random_clf.predict(X_test)
y_prob_test = best_random_clf.predict_proba(X_test)[:, 1]

print("\n===== RandomForest - Train Set Evaluation =====")
print(classification_report(y_train, y_pred_train))
print(f'{roc_auc_score(y_train, y_pred_train):.4f}')

print("\n===== RandomForest - Test Set Evaluation =====")
print(classification_report(y_test, y_pred_test))
print(f'{roc_auc_score(y_test, y_pred_test):.4f}')
```
<img width="320" height="320" alt="image" src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-2nd-4Team/blob/main/image/image_2/%EB%9E%9C%ED%8F%AC%20%EA%B2%B0%EA%B3%BC.png" />

* Train : 0.5389
* Test : 0.5051
* Overfitting Gap : 0.0338
<br>

  → 전반적인 F1과 정확도에서 낮은 수준의 성능. 과대적합은 없지만, 소수 클래스인 이탈자에 대한 재현율이 떨어짐. 


<br>
<br>


### 🔹2. XGBclassifier
```python

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 파라미터 최적화
param_grid = {
    'n_estimators': [30, 50, 80],      
    'max_depth': [2, 5, 8],
    'learning_rate': [0.1, 0.3, 0.5],              
}

model = XGBClassifier(random_state=42)
grid_search = GridSearchCV(model, param_grid, cv=5, scoring='roc_auc')

grid_search.fit(X_train, y_train)
grid_search.best_params_

best_xgb_clf = grid_search.best_estimator_

y_pred_train_xgb = best_xgb_clf.predict(X_train)
y_prob_train_xgb = best_xgb_clf.predict_proba(X_train)[:, 1]

y_pred_test_xgb = best_xgb_clf.predict(X_test)
y_prob_test_xgb = best_xgb_clf.predict_proba(X_test)[:, 1]

print("===== XGBoost - Train Set Evaluation =====")
print(classification_report(y_train, y_pred_train_xgb))
print(f"ROC AUC Score: {roc_auc_score(y_train, y_prob_train_xgb):.4f}") 


print("\n===== XGBoost - Test Set Evaluation =====")
print("Classification Report:")
print(classification_report(y_test, y_pred_test_xgb))
print(f"ROC AUC Score: {roc_auc_score(y_test, y_prob_test_xgb):.4f}")
```
<img width="320" height="320" alt="image" src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-2nd-4Team/blob/main/image/image_2/XGBoost1%EB%B2%88%20%EA%B2%B0%EA%B3%BC.png" />

* Train : 0.8129
* Test : 0.6762
* Overfitting Gap : 0.1367
<br>

  → 랜덤포레스트 모델보다 성능 증가.
<br>

  → 규제 부족 문제와 데이터 불균형으로 이탈자에 대한 재현율이 다소 떨어짐.

<br>
<br>


### 🔹3. GradientBoost
```python
# 파라미터 최적화
param_grid = {
    'n_estimators': [100, 300, 500],      
    'learning_rate': [0.1, 0.05, 0.01],   
    'max_depth': [3, 5, 7],               
    'min_samples_split': [2, 5, 10],      
    'min_samples_leaf': [1, 3, 5],        
    'subsample': [0.8, 1.0],              
    'max_features': ['sqrt', 'log2', None]
}

model = GradientBoostingClassifier(random_state=42)

grid_search = GridSearchCV(model, param_grid, cv=5, scoring='roc_auc')

grid_search.fit(X_train, y_train)
grid_search.best_params_

best_grid_clf = grid_search.best_estimator_

y_pred_train = best_grid_clf.predict(X_train)
y_prob_train = best_grid_clf.predict_proba(X_train)[:, 1]

y_pred_test = best_grid_clf.predict(X_test)
y_prob_test = best_grid_clf.predict_proba(X_test)[:, 1]

print("\n===== GradientBoost - Train Set Evaluation =====")
print(classification_report(y_train, y_pred_train))
print(f'{roc_auc_score(y_train, y_prob_train):.4f}')

print("\n===== GradientBoost - Test Set Evaluation =====")
print(classification_report(y_test, y_pred_test))
print(f'{roc_auc_score(y_test, y_prob_test):.4f}')
```
<img width="320" height="320" alt="image" src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-2nd-4Team/blob/main/image/image_2/GradientBoost%EA%B2%B0%EA%B3%BC.png" />

* Train : 0.9402
* Test : 0.7751
* Overfitting Gap : 0.1651  
<br>

  → 과적합 발생하지만 성능 안정적적
  

<br>
<br>

### 🔹4. HistGradientBoost
```python
smote = SMOTE(random_state=42)
X_resample, y_resample = smote.fit_resample(X, y)

X_encoded = X_resample.copy()
for col in X_encoded.select_dtypes(include='object').columns:
    le = LabelEncoder()
    X_encoded[col] = le.fit_transform(X_encoded[col].astype(str))

X_train, X_test, y_train, y_test = train_test_split(X_encoded, y_resample, random_state=42)

param_grid = {
    'max_iter': [50, 100, 150],
    'max_depth': [3, 5, 8],
    'learning_rate': [0.1, 0.3, 0.5],
    'l2_regularization': [5, 10, 15],
    'max_bins': [200, 225, 250]
}

model = HistGradientBoostingClassifier(random_state=42)

grid_search = GridSearchCV(model, param_grid, cv=5, scoring='roc_auc')

grid_search.fit(X_train, y_train)
grid_search.best_params_
best_hist_gb_clf = grid_search.best_estimator_

y_pred_train = best_hist_gb_clf.predict(X_train)
y_prob_train = best_hist_gb_clf.predict_proba(X_train)[:, 1]

y_pred_test = best_hist_gb_clf.predict(X_test)
y_prob_test = best_hist_gb_clf.predict_proba(X_test)[:, 1]
```
<img width="320" height="320" alt="image" src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-2nd-4Team/blob/main/image/image_2/hist%EA%B2%B0%EA%B3%BC.png" />

* Train : 0.9686
* Test : 0.8090
* Overfitting Gap : 0.1596
<br>

  → Overfitting Gap 감소 및 이탈자의 재현율 개선.
<br>

  → 학습시간이 길어지고, 모델 복잡도 증가 

<br>
<br>


### 🔹5. 최종 : XGBooat - 규제 
```python
X = df_final.drop(['churn'], axis=1)
y = df_final['churn']

smote = SMOTE(random_state=42)
X_resample, y_resample = smote.fit_resample(X, y)

X_encoded = X_resample.copy()
for col in X_encoded.select_dtypes(include='object').columns:
    le = LabelEncoder()
    X_encoded[col] = le.fit_transform(X_encoded[col].astype(str))

X_train, X_test, y_train, y_test = train_test_split(X_encoded, y_resample, random_state=42)

param_grid = {
    'n_estimators': [100, 200, 300],
    'learning_rate': [0.01, 0.07, 0.1],
    'max_depth': [3, 5, 10],
    'min_child_weight': [0.01, 0.05, 0.1],
    'subsample': [0.1, 0.5, 0.8],
    'colsample_bytree': [1.0],
    'reg_lambda': [10],
    'reg_alpha': [0],
    'gamma': [0, 1]
}

model = XGBClassifier(random_state=42)

grid_search = GridSearchCV(model, param_grid, cv=5, scoring='roc_auc')

grid_search.fit(X_train, y_train)
grid_search.best_params_
```
<img width="320" height="320" alt="image" src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-2nd-4Team/blob/main/image/image_2/%EC%B5%9C%EC%A2%85%EB%B2%A0%EC%8A%A4%ED%8A%B8%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0.png" />
<br>

```python
best_xgb_clf = grid_search.best_estimator_

y_pred_train = best_xgb_clf.predict(X_train)
y_prob_train = best_xgb_clf.predict_proba(X_train)[:, 1]

y_pred_test = best_xgb_clf.predict(X_test)
y_prob_test = best_xgb_clf.predict_proba(X_test)[:, 1]

print("\n===== XGBoost - Train Set Evaluation =====")
print(classification_report(y_train, y_pred_train))
print(f'{roc_auc_score(y_train, y_prob_train):.4f}')

print("\n===== XGBoost - Test Set Evaluation =====")
print(classification_report(y_test, y_pred_test))
print(f'{roc_auc_score(y_test, y_prob_test):.4f}')
```
<img width="320" height="320" alt="image" src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-2nd-4Team/blob/main/image/image_2/%EC%B5%9C%EC%A2%85xgboost.png" />

* Train : 0.8918
* Test : 0.8032
* Overfitting Gap : 0.0886
<br>

  → SMOTE로 데이터의 불균형 완화. 깊이·정규화·샘플링 파라미터를 통해 과적합을 효과적으로 억제
<br>

  → 재현율과 정확도의 균형 확보. 운영환경에서 안정적인 확률 기반 예측 구조 구축.

<br>
<br>

## 실제 데이터 확인
```python
# 23년도 데이터를 기반으로 전처리 진행 및 이탈률 라벨 생성
# 1. X, y 분리
X_23 = df_final_2.drop(columns=['churn'])
y_23 = df_final_2['churn']
X_encoded_2 = X_23.copy()
for col in X_encoded_2.select_dtypes(include='object').columns:
    le = LabelEncoder()
    X_encoded_2[col] = le.fit_transform(X_encoded_2[col].astype(str))

# 2. 예측
y_pred_23 = best_xgb_clf.predict(X_encoded_2)
y_proba_23 = best_xgb_clf.predict_proba(X_encoded_2)[:, 1]

# 3. 결과 DataFrame 만들기
results_23_df = X_encoded_2.copy()
results_23_df['실제값'] = y_23.values
results_23_df['예측값'] = y_pred_23
results_23_df['1_확률'] = y_proba_23

# 4. 전체 출력
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

#results_23_df
matched_df.head(10)
```
<img width="1078" height="366" alt="image" src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-2nd-4Team/blob/main/image/image_2/%EC%8B%A4%EC%A0%9C%EB%8D%B0%EC%9D%B4%ED%84%B0%ED%85%8C%EC%8A%A4%ED%8A%B8.png" />

→ 확률이 높을수록 실제 이탈 여부와 일치하는 경향.
→ 23년도 실제 데이터에서도 안정적으로 작동함을 확인. 

<br>
<br>

-----

# 7. 수행결과
### streamlit 초기 화면
![스트림릿](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-2nd-4Team/blob/main/image/%EC%8A%A4%ED%8A%B8%EB%A6%BC%EB%A6%BF.png)

### streamlit 결과 화면
![스트림릿2](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-2nd-4Team/blob/main/image/%EC%8A%A4%ED%8A%B8%EB%A6%BC%EB%A6%BF3.png)

<br>
<br>

-----
# 한계점
#### 1. 패널 데이터 사용으로 인한 사용자 편향 발생 가능성이 있음. 
#### 2. '페이스북' 사용자가 이미 이탈이 많이 일어난 상태였기 때문에 전체 데이터 로우 수가 적었음. 

<br>
<br>

-----

# 8. 한 줄 회고
|이름|내용|
|:---:|---|
|김주영|여러 해에 걸친 데이터를 다루면서, 각 연도별로 일부 변수 구성이 달라지는 점이 모델 학습에 사용할 시점을 결정하는 데 많은 고민과 어려움이 있었습니다. 여러 해의 데이터를 통합하는 과정에서 존재하지 않는 변수는 제외하고, 핵심적인 변수들을 선별하였습니다. 또한 모델 성능 향상을 위해 새로운 파생변수를 생성하고, 일부 변수만 선별하여 사용하는 등 다양한 실험을 통해서 최고의 예측 성능을 할 수 있었습니다. 스트림릿을 통해 모델 예측 결과를 시각화하는 과정에서, 모델 학습 환경과 스트림릿 실행 환경의 라이브러리 버전이 달라 많은 시간과 노력을 들여 버전 충돌을 해결해야 했습니다. 이 경험을 통해 라이브러리 버전 호환성은 프로젝트의 모든 과정에서 가장 중요한 요소라는 것을 깨달았습니다.|
|전상아|데이터 전처리 과정에서 변수 반영 및 연도 추출 부분에서 모델 성능이 달라지는 것을 확인한 부분에서 프로젝트를 진행할 때 데이터 선택 및 전처리 과정이 모델 성능에 많은 영향을 준다는 것을 알게되었습니다. 또, 처음 4개년도 데이터에 대해 랜덤포레스트, 결정트리, 로지스틱회귀 등 기본 모델에 대해 성능 확인을 해보았습니다. 이때 오히려 데이터 수가 적을 경우에는 오히려 스태킹, 부스팅 등의 모델이 과적합이 일어날 수 있다는 것을 알아 데이터 종류에 맞는 모델 선정 및 학습의 중요성을 알았습니다. 최종적으로 리드미 작성 과정에서 다른 팀원들의 코드를 읽고 정리하며 다양한 모델 성능 향상 방법에 대해 배우는 기회가 되었습니다. |
|조해리|설문조사 데이터여서 데이터를 파악하는 것부터가 정말 힘들었고, 전처리 과정에서도 시행착오가 많았다. 특히 모델 성능이 어떻게 돌려도 63%에서 오르지 않아 어려움을 겪었지만, 전처리 과정에서의 실수를 발견하고 수정했을 때 성능이 확실히 개선되는 경험을 했다. 이를 통해 데이터 분석에서 전처리의 중요성을 크게 느낄 수 있었다.|
|최우진|가공되지 않은 데이터를 다루다 보니 전처리 과정에서부터 어려움이 많았지만, 특히 모델링 단계에서 더 큰 난관을 겪었습니다. 초기 모델의 성능이 기대에 미치지 못했기 때문입니다. 이에 전처리 과정을 처음부터 다시 진행하며, 동시에 다양한 모델의 성능을 비교·검증했습니다. 그 과정에서 점차 긍정적인 신호들을 발견하고, 모델을 고도화해 나가는 데서 큰 보람과 즐거움을 느꼈습니다. 다만 신뢰할 수 있는 데이터가 더 충분히 확보되었다면 학습, 평가, 그리고 예측 단계에서 훨씬 더 효과적으로 진행할 수 있었을 것이라는 아쉬움이 남습니다.|
