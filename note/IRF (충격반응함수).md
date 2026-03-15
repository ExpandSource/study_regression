# IRF (충격반응함수, Impulse Response Function)

IRF는 [VAR (벡터자기회귀모형)](VAR%20(벡터자기회귀모형).md) 또는 [VECM (벡터오차수정모형)](VECM%20(벡터오차수정모형).md)에서 한 변수에 가해진 일시적 충격(impulse)이 시간이 지남에 따라 자신과 다른 변수에 어떤 영향을 미치는지를 추적하는 함수이다.

예를 들어 "GDP에 1단위 충격을 주면 물가는 t기 후에 얼마나 반응하는가?"를 시각화할 수 있다. 충격의 전파 경로와 소멸 속도를 파악하는 데 핵심적으로 활용된다.

변수 간 충격을 구조적으로 분리하기 위해 콜레스키 분해(Cholesky decomposition)를 이용한 직교화 충격반응함수(Orthogonalized IRF)를 주로 사용한다. 변수 순서(ordering)에 따라 결과가 달라지므로 경제이론에 근거한 순서 설정이 중요하다.

[분산분해 (FEVD)](분산분해%20(FEVD).md)와 함께 VAR 분석의 핵심 해석 도구로 쓰인다.

---

## 참조
- [Impulse response - Wikipedia](https://en.wikipedia.org/wiki/Impulse_response)
- [충격반응함수 이해하기 - 계량경제학 노트](https://eipi10.tistory.com/52)

![IRF 예시](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Impulse_response.svg/400px-Impulse_response.svg.png)
