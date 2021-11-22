import numpy as np
import pydotplus
from matplotlib import pyplot as plt

plt.rcParams['figure.figsize'] = (10, 8)
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, export_graphviz


# Create dataframe with dummy variables
def create_df(dic, feature_list):
    out = pd.DataFrame(dic)
    out = pd.concat([out, pd.get_dummies(out[feature_list])], axis=1)
    out.drop(feature_list, axis=1, inplace=True)
    return out


# Some feature values are present in train and absent in test and vice-versa.
def intersect_features(train, test):
    common_feat = list(set(train.keys()) & set(test.keys()))
    return train[common_feat], test[common_feat]


def tree_graph_to_png(tree, feature_names, png_file_to_save):
    """
    This requires GraphViz to be installed.
    """

    tree_str = export_graphviz(
        tree, feature_names=feature_names, filled=True, out_file=None
    )
    graph = pydotplus.graph_from_dot_data(tree_str)
    graph.write_png(png_file_to_save)


df_train = {}
df_train['Looks'] = ['handsome', 'handsome', 'handsome', 'repulsive',
                     'repulsive', 'repulsive', 'handsome']
df_train['Alcoholic_beverage'] = ['yes', 'yes', 'no', 'no', 'yes', 'yes', 'yes']
df_train['Eloquence'] = ['high', 'low', 'average', 'average', 'low',
                         'high', 'average']
df_train['Money_spent'] = ['lots', 'little', 'lots', 'little', 'lots',
                           'lots', 'lots']
df_train['Will_go'] = LabelEncoder().fit_transform(['+', '-', '+', '-', '-', '+', '+'])

features = ['Looks', 'Alcoholic_beverage', 'Eloquence', 'Money_spent']

df_train = create_df(df_train, features)

df_test = {}
df_test['Looks'] = ['handsome', 'handsome', 'repulsive']
df_test['Alcoholic_beverage'] = ['no', 'yes', 'yes']
df_test['Eloquence'] = ['average', 'high', 'average']
df_test['Money_spent'] = ['lots', 'little', 'lots']
df_test = create_df(df_test, features)

# Some feature values are present in train and absent in test and vice-versa.
y = df_train['Will_go']
df_train, df_test = intersect_features(train=df_train, test=df_test)

dt = DecisionTreeClassifier(max_depth=3)
dt.fit(df_train.values, y)


# tree_graph_to_png(
#     tree=dt,
#     feature_names=df_train.columns,
#     png_file_to_save="ods_mlcourse_ai/topic3_decision_trees/topic3_decision_tree_toy.png",
# )

def get_entropy(array):
    array_len = len(array)
    unique, counts = np.unique(array, return_counts=True)
    count_dict = dict(zip(unique, counts))
    entropy = 0
    for unique_value in count_dict:
        prob = count_dict[unique_value] / array_len
        entropy -= prob * np.log2(prob)
    return entropy


s0 = get_entropy(y)
print(f"s0 is {s0}")


def get_information_gain(s0, s1, s2, l1, l2):
    overall_len = l1 + l2
    ig = s0 - s1 * l1 / overall_len - s2 * l2 / overall_len
    return ig


s1 = get_entropy(y[df_train[df_train["Looks_handsome"] == 1].index])
s2 = get_entropy(y[df_train[df_train["Looks_handsome"] == 0].index])
l1 = len(y[df_train[df_train["Looks_handsome"] == 0].index])
l2 = len(y[df_train[df_train["Looks_handsome"] == 1].index])

print(f"S1 = {s1}")
print(f"S2 = {s2}")
ig = get_information_gain(s0, s1, s2, l1, l2)
print(f"IG = {ig}")

def entropy(array):
    array_len = len(array)
    unique, counts = np.unique(array, return_counts=True)
    count_dict = dict(zip(unique, counts))
    entropy = 0
    for unique_value in count_dict:
        prob = count_dict[unique_value] / array_len
        entropy -= prob  * np.log2(prob)
    return entropy


# information gain calculation
def information_gain(root, left, right):
    ''' root - initial data, left and right - two partitions of initial data'''
    l_left = len(left)
    l_right = len(right)
    overall_len = l_left + l_right
    s = entropy(root)
    s_left = entropy(left)
    s_right = entropy(right)

    ig = s - s_left * l_left / overall_len - s_right * l_right / overall_len
    return ig


def best_feature_to_split(X, y):
    '''Outputs information gain when splitting on best feature'''

    output = {}
    for col in X.columns:
        output[col] = information_gain(y, y[X[col] == 0], y[X[col] == 1])
    sorted_out = dict(sorted(output.items(), key=lambda item: item[1], reverse=True))
    best_split = next(iter(sorted_out.items()))
    best_feature, ig = best_split[0], best_split[1]

    return best_feature, ig

def build_tree(X, y, split="root"):
    best_feature, ig = best_feature_to_split(X, y)
    l_tree = X[X[best_feature] <= 0.5].drop([best_feature], axis=1)
    r_tree = X[X[best_feature] > 0.5].drop([best_feature], axis=1)
    l_y = y[l_tree.index]
    r_y = y[r_tree.index]
    print(f"Splitting {split} tree by {best_feature}")
    print(best_feature, ig)
    entropy_left = entropy(l_y)
    entropy_right = entropy(r_y)

    if entropy_left == 0 and entropy_right == 0:
        print("The tree is built")
        return True

    if entropy_left == 0 and entropy_right != 0:
        print("Stop building left tree")
    else:
        build_tree(l_tree, l_y, "left")

    if entropy_right == 0 and entropy_left != 0:
        print("Stop building right tree")
    else:
        build_tree(r_tree, r_y, "right")


build_tree(df_train, y)