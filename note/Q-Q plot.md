# Q-Q plot

Q-Q plot(Quantile-Quantile Plot)은 데이터의 [분포](./분포%20(통계학).md)가 특정 [이론적 분포](./이론적%20분포.md)를 따르는지 시각적으로 비교하는 그래프이다. 주로 [정규분포](./정규분포.md) 검정에 사용된다.

x축에는 이론적 분포의 분위수(quantile), y축에는 [표본](./표본%20(통계학).md) 데이터의 분위수를 배치한다. 데이터가 이론적 분포를 따르면 점들이 45도 대각선(기준선)에 가깝게 분포한다.

패턴 해석:
- 직선에 가까움: 이론적 분포를 따름
- S자 곡선: [첨도](./첨도.md) 차이 (급첨 또는 완첨)
- 곡선 형태: [왜도](./왜도.md) 존재 (비대칭)

[Shapiro-Wilk 검정](./Shapiro-Wilk%20검정.md)과 함께 사용하면 정규성을 수치적, 시각적으로 모두 확인할 수 있다. [Matplotlib](./Matplotlib.md)이나 [seaborn](./seaborn.md)에서 쉽게 생성할 수 있다.

## 참조
- [Q-Q Plot - Wikipedia](https://en.wikipedia.org/wiki/Q–Q_plot)
- [Q-Q plot 해석 방법 - 데이터 사이언스 스쿨](https://datascienceschool.net/02%20mathematics/08.05%20분포의%20근사.html)

![Q-Q Plot Example](https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Normal_normal_qq.svg/400px-Normal_normal_qq.svg.png)
