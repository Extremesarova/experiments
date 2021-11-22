from dataclasses import dataclass

import numpy as np
from sklearn import datasets
from sklearn import model_selection as ms
from sklearn.metrics import f1_score

SEED = 42


@dataclass
class KNearestNeighborsClassifier:
    n_neighbors: int = 3
    metric: str = 'euclidean'

    def fit(self, X, y):
        self._X = X
        self._y = y

    def _predict_one_example(self, X):
        distance = 0
        diff = self._X - X
        if self.metric == 'euclidean':
            distance = np.sqrt(np.sum(np.power(diff, 2), axis=1))
        sorted_dist_arg = distance.argsort()[:self.n_neighbors]
        labels_vote = self._y[sorted_dist_arg]
        vote_dict = {key: np.count_nonzero(labels_vote == key) for key in np.unique(self._y)}
        vote_dict_sorted = sorted(vote_dict.items(), key=lambda item: item[1], reverse=True)
        return vote_dict_sorted[0][0]

    def predict(self, X):
        out = []
        for x in X:
            out.append(self._predict_one_example(x))
        return np.array(out)


@dataclass
class Scaler:
    mean: np.array = np.empty([4, 1])
    std: np.array = np.empty([4, 1])
    is_fit: bool = False

    def fit(self, X):
        self.mean = np.mean(X, axis=0)
        self.std = np.std(X, axis=0)
        self.is_fit = True

    def transform(self, X):
        if self.is_fit:
            return (X - self.mean) / self.std
        else:
            print("You should perform fit before calling transform")

    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)


def get_euclidean_distance(diff):
    return np.sqrt(np.sum(np.power(diff, 2), axis=1))


X, y = datasets.load_iris(return_X_y=True)
X = X[:, :2]

X_train, X_test, y_train, y_test = ms.train_test_split(X, y, train_size=0.8, random_state=SEED)

scaler = Scaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn = KNearestNeighborsClassifier(n_neighbors=15)

knn.fit(X_train_scaled, y_train)
pred = knn.predict(X_test_scaled)

f1 = f1_score(y_true=y_test, y_pred=pred, average='weighted')
