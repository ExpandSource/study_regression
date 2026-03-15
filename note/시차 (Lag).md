# 시차 (Lag)

시차는 시계열 분석에서 과거 특정 시점의 값을 현재 분석에 활용할 때, 현재 시점과 과거 시점 사이의 간격(기간)을 의미한다. $t-k$ 시점의 값을 $k$차 시차 변수(lagged variable)라고 한다.

$$X_{t-1}, \; X_{t-2}, \; \ldots, \; X_{t-k}$$

시차는 [VAR (벡터자기회귀모형)](VAR%20(벡터자기회귀모형).md)과 [VECM (벡터오차수정모형)](VECM%20(벡터오차수정모형).md)에서 모델의 기억(memory) 길이를 결정하는 핵심 파라미터이다. 시차가 너무 작으면 과거 정보를 충분히 반영하지 못하고, 너무 크면 모수 수가 급증하여 추정이 불안정해진다.

적절한 시차 길이는 [시차 선택 기준 (AIC, BIC)](시차%20선택%20기준%20(AIC,%20BIC).md)으로 결정한다. Python `statsmodels`에서는 `select_order()` 메서드로 최적 시차를 자동으로 탐색할 수 있다.

---

## 참조
- [Lag operator - Wikipedia](https://en.wikipedia.org/wiki/Lag_operator)
- [시차변수와 자기회귀모형 - 데이터 사이언스 스쿨](https://datascienceschool.net/02%20mathematics/timeseries.html)
