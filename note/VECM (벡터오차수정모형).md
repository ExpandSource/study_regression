# VECM (벡터오차수정모형, Vector Error Correction Model)

VECM은 [공적분](공적분.md) 관계가 있는 비정상 시계열 변수들을 분석하기 위해 [VAR (벡터자기회귀모형)](VAR%20(벡터자기회귀모형).md)에 장기 균형 이탈 정보를 추가한 모형이다. 단기 동학과 장기 균형을 동시에 모델링한다.

$$\Delta \mathbf{y}_t = \boldsymbol{\alpha} \boldsymbol{\beta}' \mathbf{y}_{t-1} + \sum_{i=1}^{p-1} \mathbf{\Gamma}_i \Delta \mathbf{y}_{t-i} + \boldsymbol{\varepsilon}_t$$

여기서 $\boldsymbol{\beta}' \mathbf{y}_{t-1}$은 [오차수정항 (ECT)](오타수정항%20(ECT).md)으로 장기 균형으로부터의 이탈을 나타내고, $\boldsymbol{\alpha}$는 [조정속도 α](조정속도%20%20α.md)로 이탈을 얼마나 빠르게 수정하는지를 나타낸다.

공적분 벡터의 수(rank)는 [요한슨 검정](요한슨%20검정.md)으로 확인한다. [시차 (Lag)](시차%20(Lag).md)는 [시차 선택 기준 (AIC, BIC)](시차%20선택%20기준%20(AIC,%20BIC).md)으로 결정한다. [충격반응함수 (IRF)](IRF%20(충격반응함수).md)와 [분산분해 (FEVD)](분산분해%20(FEVD).md) 분석도 VECM에서 적용 가능하다.

---

## 참조
- [Error correction model - Wikipedia](https://en.wikipedia.org/wiki/Error_correction_model)
- [VECM 개념과 활용 - 계량경제학 블로그](https://eipi10.tistory.com/55)
