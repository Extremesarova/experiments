import numpy as np


def count_prob(marker, array):
    return array.count(marker) / len(array)


def get_entropy(p1, p2):
    part_1 = p1 * np.log2(p1) if p1 != 0 else 0
    part_2 = p2 * np.log2(p2) if p2 != 0 else 0
    entropy = - (part_1 + part_2)

    return entropy


def get_information_gain(s_0, len_group_1, len_group_2, len_0, s_1, s_2):
    return s_0 - (len_group_1 * s_1 + len_group_2 * s_2) / len_0


def get_gini_impurity(blue_prob, orange_prob):
    return 1 - np.power(blue_prob, 2) - np.power(orange_prob, 2)


def get_gini_impurity_criterion(gini_impurity_1, gini_impurity_2, len_group_1, len_group_2, len_0):
    return (len_group_1 * gini_impurity_1 + len_group_2 * gini_impurity_2) / len_0


x = np.arange(0, 20, 1)
y = ["orange"] + 4 * ["blue"] + 4 * ["orange"] + 4 * ["blue"] + 6 * ["orange"] + ["blue"]
blue_prob_0 = count_prob("blue", y)
orange_prob_0 = count_prob("orange", y)
s_0 = get_entropy(blue_prob_0, orange_prob_0)
len_0 = len(y)

information_gain_res = []
gini_impurity_res = []

for ind in range(1, len_0):
    group_1 = y[:ind]
    group_2 = y[ind:]
    blue_prob_1 = count_prob("blue", group_1)
    blue_prob_2 = count_prob("blue", group_2)
    orange_prob_1 = count_prob("orange", group_1)
    orange_prob_2 = count_prob("orange", group_2)
    len_group_1 = len(group_1)
    len_group_2 = len(group_2)
    s_1 = get_entropy(blue_prob_1, orange_prob_1)
    s_2 = get_entropy(blue_prob_2, orange_prob_2)
    ig = get_information_gain(s_0, len_group_1, len_group_2, len_0, s_1, s_2)
    information_gain_res.append({"ig": ig,
                                 "ind": ind - 1,
                                 "group_1": group_1,
                                 "group_2": group_2})

    gini_impurity_1 = get_gini_impurity(blue_prob_1, orange_prob_1)
    gini_impurity_2 = get_gini_impurity(blue_prob_2, orange_prob_2)
    gini_impurity_criterion = get_gini_impurity_criterion(gini_impurity_1, gini_impurity_2, len_group_1, len_group_2,
                                                          len_0)
    gini_impurity_res.append({"gini": gini_impurity_criterion,
                              "ind": ind - 1,
                              "group_1": group_1,
                              "group_2": group_2})

sorted_information_gain_res = sorted(information_gain_res, key=lambda item: item["ig"], reverse=True)
print(f"The best result for information gain is {sorted_information_gain_res[0]}")

sorted_gini_impurity_res = sorted(gini_impurity_res, key=lambda item: item["gini"], reverse=False)
print(f"The best result for information gain is {sorted_gini_impurity_res[0]}")

xx = np.linspace(0, 1, 50)

