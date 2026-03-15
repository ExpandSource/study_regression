# VAR (벡터자기회귀모형, Vector Autoregression)

VAR 모형은 여러 시계열 [변수 (통계학)](변수%20(통계학).md)가 서로 영향을 주고받는 관계를 동시에 모델링하는 다변량 시계열 분석 방법이다. 각 변수를 모든 변수의 과거값(시차)으로 설명한다.

$$\mathbf{y}_t = \mathbf{c} + \mathbf{A}_1 \mathbf{y}_{t-1} + \mathbf{A}_2 \mathbf{y}_{t-2} + \cdots + \mathbf{A}_p \mathbf{y}_{t-p} + \boldsymbol{\varepsilon}_t$$

여기서 $\mathbf{y}_t$는 변수 벡터, $p$는 [시차 (Lag)](시차%20(Lag).md), $\boldsymbol{\varepsilon}_t$는 오차항이다. 적절한 시차 $p$는 [시차 선택 기준 (AIC, BIC)](시차%20선택%20기준%20(AIC,%20BIC).md)으로 결정한다.

VAR 모형에서 [충격반응함수 (IRF)](IRF%20(충격반응함수).md)는 한 변수의 충격이 다른 변수에 미치는 시간별 파급 효과를 추적하고, [분산분해 (FEVD)](분산분해%20(FEVD).md)는 각 변수의 예측 오차에 대한 다른 변수의 기여도를 분석한다. 변수 간 [공적분](공적분.md) 관계가 있으면 [VECM (벡터오차수정모형)](VECM%20(벡터오차수정모형).md)으로 확장한다.

---

## 참조
- [Vector autoregression - Wikipedia](https://en.wikipedia.org/wiki/Vector_autoregression)
- [VAR 모형 이해하기 - 경제통계 분석](https://velog.io/@euisuk-chung/VAR-Vector-Autoregression)


![|800](_assets/var_vecm_decision_flow.svg)