# 오차수정항 (ECT, Error Correction Term)

오차수정항은 [VECM (벡터오차수정모형)](VECM%20(벡터오차수정모형).md)에서 장기 균형([공적분](공적분.md) 관계)으로부터의 이탈 정도를 나타내는 항이다. 전기(t-1)의 균형 이탈이 현재의 변화에 얼마나 영향을 주는지를 반영한다.

$$\text{ECT}_{t-1} = \boldsymbol{\beta}' \mathbf{y}_{t-1}$$

공적분 벡터 $\boldsymbol{\beta}$와 전기 값의 선형결합으로, 이 값이 크면(균형에서 많이 이탈) 다음 기에 강하게 수정되고, 작으면 약하게 수정된다. ECT의 계수는 [조정속도 α](조정속도%20%20α.md)이다.

ECT의 부호와 통계적 유의성은 장기 인과관계(Granger causality)를 파악하는 근거가 된다. ECT 계수가 음수이고 유의하면 해당 변수가 장기 균형으로 수렴하는 방향으로 조정됨을 의미한다.

---

## 참조
- [Error correction model - Wikipedia](https://en.wikipedia.org/wiki/Error_correction_model)
- [오차수정모형과 ECT 해석 - 계량경제학 블로그](https://eipi10.tistory.com/55)
