# 분산분해 (FEVD, Forecast Error Variance Decomposition)

분산분해는 [VAR (벡터자기회귀모형)](VAR%20(벡터자기회귀모형).md) 분석에서 특정 변수의 예측 오차 [분산 (통계학)](분산%20(통계학).md)이 각 변수의 충격에 의해 얼마나 설명되는지를 비율(%)로 나타내는 방법이다.

예를 들어 "소비의 예측 오차 분산 중 소득 충격이 기여하는 비율이 t기 이후 몇 %인가?"를 보여준다. 이를 통해 변수 간 상대적 영향력의 크기를 파악할 수 있다.

시간이 지날수록 다른 변수의 기여도가 어떻게 변하는지 동태적 분석이 가능하며, [충격반응함수 (IRF)](IRF%20(충격반응함수).md)가 충격의 방향과 경로를 보여준다면 FEVD는 충격의 상대적 중요도를 보여준다. 두 분석은 VAR/[VECM (벡터오차수정모형)](VECM%20(벡터오차수정모형).md) 해석에서 항상 함께 사용된다.

---

## 참조
- [Forecast error variance decomposition - Wikipedia](https://en.wikipedia.org/wiki/Variance_decomposition_of_forecast_errors)
- [분산분해 분석 이해 - 계량경제학 블로그](https://eipi10.tistory.com/54)
