# p-value (유의확률, Probability Value)

p-value는 [가설검정](./가설검정.md)에서 [귀무가설](./귀무가설.md)이 참일 때, 관측된 [검정통계량](./검정통계량.md) 이상으로 극단적인 결과가 나올 확률을 나타낸다. 예를 들어 p-value=0.03은 "귀무가설이 참이면 이 정도의 데이터가 나올 확률이 3%"라는 의미다. p-value가 [유의수준](./유의수준.md)(보통 0.05)보다 작으면 귀무가설을 기각한다.

**중요한 주의**: p-value는 "가설이 참일 확률"이 아니라 "귀무가설이 참이면서 데이터가 관측될 확률"이다. 따라서 p<0.05도 "가설이 95% 맞을 확률"을 의미하지 않는다. p-value는 검정의 강도(Strength of Evidence)를 나타내며, 표본 크기에 따라 달라진다. 같은 효과라도 표본이 크면 더 작은 p-value를 얻게 된다.

## 관련 개념
- [[가설검정]]
- [[귀무가설]]
- [[검정통계량]]
- [[유의수준]]

## 참고
- [P-value - Wikipedia](https://en.wikipedia.org/wiki/P-value)
- [p-value 정확히 이해하기 - 통계 연구소](https://blog.naver.com/PostView.nhn?blogId=intellectspace&logNo=220955667890)

## 시각 자료
- 📊 **[p-value 인터랙티브 시각화 - R Psychologist](https://rpsychologist.com/pvalue/)** (강력히 추천)
- 📊 [p-value 설명 - Khan Academy](https://www.khanacademy.org/math/statistics-probability/significance-tests-one-sample)
