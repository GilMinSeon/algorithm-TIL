# 정수 n 입력
n = int(input())

# DP 테이블 초기화
dp = [0] * (10**6+1)

# bottom-up방식 DP
for i in range(2, n+1):
    # 현재의 수에서 1을 뺴는 경우
    dp[i] = dp[i-1] + 1
    # 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    # 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[n])




    