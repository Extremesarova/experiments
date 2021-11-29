from sklearn import datasets
from sklearn import model_selection as ms
from sklearn.metrics import f1_score

from knn.k_nearest_neighbors_classifier import KNearestNeighborsClassifier
from utils.scaler import Scaler

SEED = 42

X, y = datasets.load_iris(return_X_y=True)
X = X[:, :2]

X_train, X_test, y_train, y_test = ms.train_test_split(X, y, train_size=0.8, random_state=SEED)

scaler = Scaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn = KNearestNeighborsClassifier(n_neighbors=15, metric='minkowski')

knn.fit(X_train_scaled, y_train)
pred = knn.predict(X_test_scaled)

f1 = f1_score(y_true=y_test, y_pred=pred, average='weighted').round(2)
print(f'F1 is equal to {f1}')
