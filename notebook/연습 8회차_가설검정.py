# %% ================================================================
# [8회차] 가설검정 전체 구조 이해하기
# 목적: 가설검정의 논리를 직관적으로 이해하고, 각 단계를 계산해본다
# Google Colab Notebook 환경 기준
# ================================================================

# %% 1. 라이브러리 불러오기
# numpy    : 수치 계산 및 난수 생성
# matplotlib : 시각화 (H₀ 분포, p-value 영역 등)
# scipy.stats : t분포, t-검정 등 통계 함수

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 난수 재현성을 위해 seed 고정
np.random.seed(42)

# 한글 폰트 설정 (한글이 깨지지 않도록)
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False


# %% 2. 가설 설정 및 H0 분포 시각화
# ================================================================
# 상황 설정:
# H0: "어떤 집단의 모평균은 100이다" (귀무가설)
# H1: "모평균은 100이 아니다" (대립가설)
#
# 실제로는 모평균이 105인 모집단에서 표본을 뽑습니다.
# 우리는 "이 표본이 H0과 충분히 다른가?"를 판단해야 합니다.

mu_0 = 100          # 귀무가설의 평균 (가정)
sigma = 15          # 모집단 표준편차 (알고 있다고 가정)
n = 30              # 표본 크기
true_mu = 105       # 실제 모집단 평균 (H0과 다름)
alpha = 0.05        # 유의수준

# 실제 모집단에서 표본 1개 추출
sample = np.random.normal(true_mu, sigma, n)
sample_mean = np.mean(sample)
sample_std = np.std(sample, ddof=1)  # 표본 표준편차
se = sample_std / np.sqrt(n)         # 표준오차

print(f"표본 평균: {sample_mean:.3f}")
print(f"표본 표준편차: {sample_std:.3f}")
print(f"표준오차 (SE): {se:.3f}")

# ================================================================
# H0 하에서의 표집분포 시각화
# ================================================================
# H0이 참이라고 가정하면, 표본평균들은 N(100, SE^2)를 따릅니다.
# 우리가 관측한 표본평균이 이 분포 안에서 얼마나 "극단적"인지 시각화합니다.

x = np.linspace(mu_0 - 4*se, mu_0 + 4*se, 200)
y = stats.norm.pdf(x, mu_0, se)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label='H0 Distribution')
plt.axvline(sample_mean, color='r', linestyle='--', linewidth=2, label=f'Observed Mean ({sample_mean:.2f})')
plt.axvline(mu_0, color='k', linestyle='-', linewidth=1, alpha=0.5, label=f'H0 Mean ({mu_0})')
plt.fill_between(x, y, alpha=0.2, color='blue')
plt.xlabel('Sample Mean (표본 평균)')
plt.ylabel('Probability Density')
plt.title('H0이 참일 때의 표본평균 분포 (Sampling Distribution under H0)')
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# 핵심 질문:
# "이 빨간색 점(우리가 관측한 표본평균)이 파란색 분포와 충분히 멀리 떨어져 있는가?"
# 이를 정량적으로 판단하는 방법이 "검정통계량"입니다.


# %% 3. 검정통계량(t값) 계산
# ================================================================
# 공식:
# t = (x̄ - μ₀) / SE
#
# 의미:
# "표본평균이 귀무가설 평균으로부터 얼마나 멀리 떨어져 있는가"
# "그 거리를 표준오차(불확실성)로 나눈 값"
#
# 큰 |t| = H0과 많이 다름 = H0을 기각할 가능성 높음

t_stat = (sample_mean - mu_0) / se
df = n - 1  # 자유도 (degree of freedom)

print(f"검정통계량 (t value): {t_stat:.4f}")
print(f"자유도 (df): {df}")
print()
print("해석:")
print(f"표본평균이 H0 평균으로부터 {abs(t_stat):.2f} * SE 만큼 떨어져 있습니다.")
print(f"이는 우연으로 발생할 수 있는 '정상적인' 범위 내인가, 아니면 '극단적'인가?")
print(f"이를 판단하기 위해 p-value를 계산합니다.")


# %% 4. p-value 계산 및 시각화 (양측 검정)
# ================================================================
# p-value의 정확한 의미:
# "H0이 참이라고 가정했을 때, 지금 본 것과 같거나 더 극단적인 결과가
#  우연으로 나올 확률"

# 양측 검정 (two-tailed):
# |t| >= |t_observed|인 영역의 넓이
p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df=df))

print(f"p-value: {p_value:.5f}")
print()
print("해석:")
print(f"H0이 참이라면, 이런 표본이 나올 확률은 {p_value*100:.2f}%입니다.")
print()

# ================================================================
# p-value를 시각적으로 표현
# ================================================================
x_t = np.linspace(-5, 5, 200)
y_t = stats.t.pdf(x_t, df=df)

# 양측 검정의 임계값
critical_value = abs(t_stat)

plt.figure(figsize=(10, 6))
plt.plot(x_t, y_t, 'b-', linewidth=2, label='t-distribution')

# p-value 영역 (음영)
x_left = x_t[x_t <= -critical_value]
y_left = stats.t.pdf(x_left, df=df)
x_right = x_t[x_t >= critical_value]
y_right = stats.t.pdf(x_right, df=df)

plt.fill_between(x_left, y_left, alpha=0.3, color='red', label='p-value (left tail)')
plt.fill_between(x_right, y_right, alpha=0.3, color='red', label='p-value (right tail)')

# 관측된 t값 표시
plt.axvline(t_stat, color='darkred', linestyle='--', linewidth=2, label=f't_observed = {t_stat:.3f}')
plt.axvline(-t_stat, color='darkred', linestyle='--', linewidth=2)

# 유의수준 기준선
plt.axvline(stats.t.ppf(1 - alpha/2, df=df), color='green', linestyle=':', linewidth=1, alpha=0.7, label=f'Critical value (α={alpha})')
plt.axvline(-stats.t.ppf(1 - alpha/2, df=df), color='green', linestyle=':', linewidth=1, alpha=0.7)

plt.xlabel('t-statistic')
plt.ylabel('Probability Density')
plt.title(f'p-value 시각화 (Two-tailed test)\np-value = {p_value:.4f}')
plt.legend()
plt.grid(alpha=0.3)
plt.show()

print("빨강 음영 면적 = p-value (우리가 본 것보다 극단적일 확률)")
print(f"초록 점선 = 임계값 (α={alpha}일 때)")
print()
print("판단:")
if p_value < alpha:
    print(f"p-value ({p_value:.5f}) < α ({alpha}) → H0 기각!")
    print("결론: 유의수준 5%에서 귀무가설을 기각합니다.")
else:
    print(f"p-value ({p_value:.5f}) >= α ({alpha}) → H0 기각 불가")
    print("결론: 귀무가설을 기각할 충분한 증거가 없습니다.")


# %% 5. scipy로 t-test 검증
# ================================================================
# 우리가 직접 계산한 t값과 p-value가
# scipy의 t-test 함수 결과와 일치하는지 확인합니다.

t_test_result = stats.ttest_1samp(sample, mu_0)

print("===== scipy.stats.ttest_1samp() 결과 =====")
print(f"t-statistic: {t_test_result.statistic:.4f}")
print(f"p-value (two-tailed): {t_test_result.pvalue:.5f}")
print()
print("===== 우리가 직접 계산한 값 =====")
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value (two-tailed): {p_value:.5f}")
print()
print("✓ 거의 동일하게 나왔습니다!")


# %% 6. 1종 오류 시뮬레이션
# ================================================================
# 1종 오류: "H0이 참인데도 기각해버리는 오류"
#
# 이론:
# H0이 정말 참인 상황에서 우리가 5%의 유의수준을 설정하면,
# 반복 실험했을 때 약 5% 비율로 잘못 기각해야 합니다.
#
# 이를 시뮬레이션으로 확인합니다:
# 1) H0과 동일한 모집단(μ=100)에서 표본을 반복 추출
# 2) 각 표본마다 t-test 실행
# 3) 기각한 비율 계산 → 약 0.05가 나와야 함

true_mu = mu_0  # H0이 정말 참인 상황
n_sim = 5000    # 5000번 반복
rejections = 0
p_values_sim = []

for _ in range(n_sim):
    sim_sample = np.random.normal(true_mu, sigma, n)
    t_stat_sim = (np.mean(sim_sample) - mu_0) / (np.std(sim_sample, ddof=1) / np.sqrt(n))
    p_val_sim = 2 * (1 - stats.t.cdf(abs(t_stat_sim), df=n-1))
    p_values_sim.append(p_val_sim)

    if p_val_sim < alpha:
        rejections += 1

type1_error_rate = rejections / n_sim

print(f"반복 실험 횟수: {n_sim}")
print(f"기각한 횟수: {rejections}")
print(f"1종 오류 비율 (관찰값): {type1_error_rate:.4f}")
print(f"1종 오류 비율 (이론값): {alpha:.4f}")
print()
print("해석:")
print(f"H0이 정말 참일 때, 약 {alpha*100}%의 확률로 잘못 기각했습니다.")
print("이것이 '유의수준'의 장기적 의미입니다.")

# ================================================================
# p-value들의 분포를 히스토그램으로 시각화
# ================================================================
plt.figure(figsize=(10, 6))
plt.hist(p_values_sim, bins=50, edgecolor='black', alpha=0.7)
plt.axvline(alpha, color='red', linestyle='--', linewidth=2, label=f'α = {alpha}')
plt.xlabel('p-value')
plt.ylabel('Frequency')
plt.title(f'p-value Distribution when H0 is True (n_sim={n_sim})')
plt.legend()
plt.grid(alpha=0.3)
plt.show()

print(f"\n빨강 선 왼쪽 영역 = 기각 영역")
print(f"총 {rejections}/{n_sim} = {type1_error_rate*100:.1f}%가 기각되었습니다.")


# %% 7. 단측 vs 양측 검정 비교
# ================================================================
# 양측 검정 (two-tailed):
# H1: "μ ≠ 100" (방향이 없음, 크거나 작거나)
# p-value = 양쪽 꼬리 합
#
# 단측 검정 (one-tailed):
# H1: "μ > 100" 또는 "μ < 100" (한쪽 방향만)
# p-value = 한쪽 꼬리만
#
# 주의: 사전에 방향을 정해야 합니다. 데이터를 보고 나서 정하면 안 됩니다!

# 같은 t값에서
p_value_two_tailed = 2 * (1 - stats.t.cdf(abs(t_stat), df=df))
p_value_right_tailed = 1 - stats.t.cdf(t_stat, df=df)  # 우측 검정 (t > 0 쪽)
p_value_left_tailed = stats.t.cdf(t_stat, df=df)       # 좌측 검정 (t < 0 쪽)

print(f"같은 t값 ({t_stat:.3f})에서:")
print(f"양측 검정: p-value = {p_value_two_tailed:.5f}")
print(f"우측 검정: p-value = {p_value_right_tailed:.5f}")
print(f"좌측 검정: p-value = {p_value_left_tailed:.5f}")
print()
print(f"주목: 단측 검정의 p-value가 약 절반입니다!")
print(f"우측 검정에서 p-value < 0.05? {p_value_right_tailed < 0.05}")
print(f"양측 검정에서 p-value < 0.05? {p_value_two_tailed < 0.05}")

# ================================================================
# 시각화: 양측 vs 단측
# ================================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 좌측: 양측 검정
x_t = np.linspace(-5, 5, 200)
y_t = stats.t.pdf(x_t, df=df)

ax = axes[0]
ax.plot(x_t, y_t, 'b-', linewidth=2)
x_left = x_t[x_t <= -critical_value]
y_left = stats.t.pdf(x_left, df=df)
x_right = x_t[x_t >= critical_value]
y_right = stats.t.pdf(x_right, df=df)
ax.fill_between(x_left, y_left, alpha=0.3, color='red')
ax.fill_between(x_right, y_right, alpha=0.3, color='red')
ax.axvline(t_stat, color='darkred', linestyle='--', linewidth=2)
ax.axvline(-t_stat, color='darkred', linestyle='--', linewidth=2)
ax.set_title(f'Two-tailed Test\np-value = {p_value_two_tailed:.4f}')
ax.set_xlabel('t-statistic')
ax.set_ylabel('Probability Density')
ax.grid(alpha=0.3)

# 우측: 우측 검정
ax = axes[1]
ax.plot(x_t, y_t, 'b-', linewidth=2)
x_right = x_t[x_t >= critical_value]
y_right = stats.t.pdf(x_right, df=df)
ax.fill_between(x_right, y_right, alpha=0.3, color='red')
ax.axvline(t_stat, color='darkred', linestyle='--', linewidth=2)
ax.set_title(f'Right-tailed Test (H1: μ > 100)\np-value = {p_value_right_tailed:.4f}')
ax.set_xlabel('t-statistic')
ax.set_ylabel('Probability Density')
ax.grid(alpha=0.3)

plt.tight_layout()
plt.show()

print("\n⚠️  주의: 단측 검정은 사전에 방향을 정해야 합니다!")
print("데이터를 본 후에 '아, 이쪽이 극단적이네'라고 하면 안 됩니다.")


# %% 8. 표본 크기와 검정력
# ================================================================
# 검정력 = "실제로 H0이 거짓일 때 이를 올바르게 감지할 확률"
#
# 실제로 true_mu = 105인 상황에서 (H0은 false)
# 표본 크기를 달리하면 검정력이 어떻게 변할까?

true_mu = 105  # H0과 다른 참값
sample_sizes = [20, 50, 100, 200]
power_results = []

for n_temp in sample_sizes:
    rejections = 0
    n_sim_power = 2000

    for _ in range(n_sim_power):
        sim_sample = np.random.normal(true_mu, sigma, n_temp)
        t_stat_sim = (np.mean(sim_sample) - mu_0) / (np.std(sim_sample, ddof=1) / np.sqrt(n_temp))
        p_val_sim = 2 * (1 - stats.t.cdf(abs(t_stat_sim), df=n_temp-1))

        if p_val_sim < alpha:
            rejections += 1

    power = rejections / n_sim_power
    power_results.append(power)
    print(f"표본 크기 {n_temp:3d} → 검정력: {power:.3f}")

print()
print("해석:")
print("표본이 클수록 \"차이\"를 감지하기 쉬워집니다.")
print(f"특히 n=20일 때는 {power_results[0]*100:.0f}% 확률로만 감지하지만,")
print(f"n=200일 때는 {power_results[-1]*100:.0f}%에 가깝습니다.")

# ================================================================
# 표본 크기 vs 검정력 꺾은선 그래프
# ================================================================
plt.figure(figsize=(10, 6))
plt.plot(sample_sizes, power_results, 'o-', linewidth=2, markersize=8, label='Power')
plt.axhline(0.80, color='green', linestyle='--', linewidth=1, alpha=0.7, label='Convention (Power = 0.80)')
plt.xlabel('Sample Size (n)')
plt.ylabel('Statistical Power (1 - β)')
plt.title(f'Sample Size vs Statistical Power\n(True μ = {true_mu}, H0: μ = {mu_0})')
plt.grid(alpha=0.3)
plt.legend()
plt.ylim([0, 1.0])
plt.show()

print("\n초록 선: 관례적으로 충분한 검정력(0.80)")
print(f"이 경우 약 n={int(np.interp(0.80, power_results, sample_sizes))} 정도면 충분합니다.")


# %% 9. 유의수준 변화에 따른 임계값 비교
# ================================================================
# 유의수준 α가 바뀌면 기각/채택 판단도 바뀝니다.
#
# α = 0.01: 더 엄격 (기각하기 어려움, 1종 오류 적음)
# α = 0.05: 중간 정도 (관례)
# α = 0.10: 더 관대 (기각하기 쉬움)

alphas = [0.01, 0.05, 0.10]
critical_values = []

print(f"자유도 = {df}일 때 각 유의수준의 임계값:")
print()

for alpha_test in alphas:
    crit_val = stats.t.ppf(1 - alpha_test/2, df=df)
    critical_values.append(crit_val)
    print(f"α = {alpha_test:>4.2f} → 임계값 = ±{crit_val:.3f}")

print()
print(f"우리의 t값: {t_stat:.3f}")
print()
print("판단:")
for alpha_test, crit_val in zip(alphas, critical_values):
    reject = abs(t_stat) > crit_val
    print(f"α = {alpha_test}: |{t_stat:.3f}| > {crit_val:.3f}? → {reject}")

# ================================================================
# 시각화: 여러 유의수준의 임계값
# ================================================================
x_t = np.linspace(-4, 4, 200)
y_t = stats.t.pdf(x_t, df=df)

plt.figure(figsize=(12, 6))
plt.plot(x_t, y_t, 'b-', linewidth=2, label='t-distribution')

colors = ['red', 'orange', 'green']
for alpha_test, crit_val, color in zip(alphas, critical_values, colors):
    plt.axvline(crit_val, color=color, linestyle=':', linewidth=2, alpha=0.7, label=f'Critical value (α={alpha_test})')
    plt.axvline(-crit_val, color=color, linestyle=':', linewidth=2, alpha=0.7)

plt.axvline(t_stat, color='darkred', linestyle='--', linewidth=2, label=f't_observed = {t_stat:.3f}')
plt.axvline(-t_stat, color='darkred', linestyle='--', linewidth=2)

plt.xlabel('t-statistic')
plt.ylabel('Probability Density')
plt.title('Critical Values for Different Significance Levels')
plt.legend()
plt.grid(alpha=0.3)
plt.show()

print("\n⚠️  α를 낮출수록 (더 엄격하게) 기각 판단이 어려워집니다!")


# %% 10. Cohen's d와 실질적 vs 통계적 유의성
# ================================================================
# 중요한 문제:
# "p-value < 0.05"라고 해서 항상 "중요한 차이"는 아닙니다!
#
# 예: 샘플 크기가 크면 작은 차이도 유의할 수 있음
# 예: 샘플 크기가 작으면 큰 차이도 유의하지 않을 수 있음
#
# 따라서 "효과 크기(Effect Size)"도 함께 봐야 합니다.

# Cohen's d 계산
# d = (μ1 - μ0) / σ
# 또는 표본 기반: d = (x̄ - μ0) / s

cohens_d = (sample_mean - mu_0) / sample_std

print(f"Cohen's d: {cohens_d:.3f}")
print()
print("해석 기준 (관례):")
print("  |d| < 0.2  : 아주 작은 효과")
print("  0.2 ≤ |d| < 0.5 : 작은 효과")
print("  0.5 ≤ |d| < 0.8 : 중간 효과")
print("  |d| ≥ 0.8  : 큰 효과")
print()

if abs(cohens_d) < 0.2:
    effect_size_label = "아주 작은"
elif abs(cohens_d) < 0.5:
    effect_size_label = "작은"
elif abs(cohens_d) < 0.8:
    effect_size_label = "중간"
else:
    effect_size_label = "큰"

print(f"이 데이터의 효과 크기: {effect_size_label}")
print()
print("결론:")
print(f"p-value = {p_value:.4f}, Cohen's d = {cohens_d:.3f}")
print()
if p_value < 0.05 and abs(cohens_d) < 0.2:
    print("⚠️  통계적으로는 유의하지만, 실질적 효과는 아주 작습니다.")
elif p_value < 0.05 and abs(cohens_d) >= 0.5:
    print("✓ 통계적으로 유의하고, 실질적 효과도 있습니다.")
elif p_value >= 0.05:
    print("실질적으로 의미있는 차이가 있어도 통계적으로 유의하지 않을 수 있습니다.")
    print("(예: 샘플 크기가 충분하지 않은 경우)")

# ================================================================
# 시각화: H0 vs H1 분포의 겹침
# ================================================================
# H0 분포 (μ = 100)
# H1 분포 (μ = 105)

x_dist = np.linspace(80, 130, 200)
y_h0 = stats.norm.pdf(x_dist, mu_0, se)  # 표집분포 기준
y_h1 = stats.norm.pdf(x_dist, true_mu, se)

plt.figure(figsize=(10, 6))
plt.plot(x_dist, y_h0, 'b-', linewidth=2, label='H0: μ = 100')
plt.plot(x_dist, y_h1, 'r-', linewidth=2, label='H1: μ = 105')
plt.fill_between(x_dist, y_h0, alpha=0.2, color='blue')
plt.fill_between(x_dist, y_h1, alpha=0.2, color='red')
plt.axvline(sample_mean, color='darkred', linestyle='--', linewidth=2, label=f'Observed Mean = {sample_mean:.2f}')
plt.xlabel('Sample Mean (표본 평균)')
plt.ylabel('Probability Density')
plt.title(f'H0 vs H1 분포의 겹침\nEffect Size (Cohen\'s d) = {cohens_d:.3f}')
plt.legend()
plt.grid(alpha=0.3)
plt.show()

print(f"\n두 분포의 겹치는 정도가 작을수록 (즉 Cohen's d가 클수록)")
print(f"H0과 H1을 구분하기 쉬워집니다. (검정력이 높음)")
