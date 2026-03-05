#include <stdio.h>

int main(void) {
	int test_case;
	int T;
	setbuf(stdout, NULL);
	scanf("%d", &T);

	for (test_case = 1; test_case <= T; ++test_case)
	{
		int price_d, price_m, price_3m, price_y;
		scanf("%d %d %d %d", &price_d, &price_m, &price_3m, &price_y);
		int plan[13] = { 0, };
		for (int i = 1; i < 13; i++) {
			scanf("%d", &plan[i]);
		}

		/*month_cost[i] = i월의 최소 비용*/
		int month_cost[13] = { 0, };
		/*dp[i] = 1~i월까지의 수영장 최소 비용*/
		int dp[13] = { 0, };
		int answer = 0;

		for (int i = 1; i < 13; i++) {
			/*1일이용권 vs 1달이용권*/
			if (plan[i] * price_d >= price_m) {
				month_cost[i] = price_m;
			}
			else {
				month_cost[i] = plan[i] * price_d;
			}
		}

		for (int i = 1; i < 13; i++) {
			/*dp[i]는 전 달까지의 최소 비용+i월의 최소 비용*/
			dp[i] = dp[i - 1] + month_cost[i];
			
			if ((i >= 3) && (i < 12)) {
				if (dp[i] >= dp[i - 3] + price_3m) {
					dp[i] = dp[i - 3] + price_3m;
				}
			}
			if (i == 12) {
				if ((dp[i - 3] + price_3m <= dp[i]) && (dp[i - 3] + price_3m <= dp[i - 2] + price_3m) && (dp[i - 3] + price_3m <= dp[i - 1] + price_3m)) {
					dp[i] = dp[i - 3] + price_3m;
				}
				else if ((dp[i - 2] + price_3m <= dp[i]) && (dp[i - 2] + price_3m <= dp[i - 3] + price_3m) && (dp[i - 2] + price_3m <= dp[i - 1] + price_3m)) {
					dp[i] = dp[i - 2] + price_3m;
				}
				else if ((dp[i - 1] + price_3m <= dp[i]) && (dp[i - 1] + price_3m <= dp[i - 3] + price_3m) && (dp[i - 1] + price_3m <= dp[i - 2] + price_3m)) {
					dp[i] = dp[i - 1] + price_3m;
				}
			}
		}
		if (dp[12] >= price_y) {
			answer = price_y;
		}
		else {
			answer = dp[12];
		}
		printf("#%d %d", test_case, answer);
		printf("\n");
	}
	return 0;
}