import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

X, y = fetch_california_housing(return_X_y=True, as_frame=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, shuffle=True)

lr = LinearRegression(n_jobs=-1)
lr.fit(X_train, y_train)

print(lr.intercept_)
print(lr.coef_)
print(lr.score(X_test, y_test))

y_pred = lr.predict(X_test)

mse = mean_squared_error(y_true=y_test, y_pred=y_pred)

pred_0_by_hand = np.sum(X_test.values[0] * lr.coef_) + lr.intercept_
pred_0 = lr.predict(X_test.values[0].reshape(1, -1))[0]

mse_0_by_hand = np.power(y_test.values[0] - y_pred[0], 2)
mse_0 = mean_squared_error([y_test.values[0]], [y_pred[0]])
