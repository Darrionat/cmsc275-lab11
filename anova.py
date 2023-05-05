from stats_utils import *  # Code from previous labs
import scipy


def anova(groups):
    g = len(groups)  # Num of groups
    N = 0  # Number of things overall
    group_means = []
    for group in groups:
        N += len(group)
        group_means.append(mean(group))
    df_between = g - 1
    df_within = N - g
    group_means_sq = [m * m for m in group_means]
    SS_between = len(groups[0]) * (sum(group_means_sq) - sum(group_means) ** 2 / g)

    group_SS = [sum_squared_deviations_computational(group) for group in groups]
    SS_within = sum(group_SS)
    MS_between = SS_between / df_between
    MS_within = SS_within / df_within

    F = MS_between / MS_within

    p_value = scipy.stats.f.cdf(F, df_between, df_within)
    partial_eta_sq = SS_between / (SS_between + SS_within)
    print(df_between, df_within)
    print(f'F-value\t{F}')
    print(f'p-value\t{p_value}')
    print(f'eta_p^2\t{partial_eta_sq}')


if __name__ == '__main__':
    data = [[35, 30, 28, 31, 26], [27, 33, 25, 26, 29], [24, 29, 22, 25, 20]]
    anova(data)
    # print(anova(data))
