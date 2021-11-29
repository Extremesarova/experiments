import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression, Lasso, LassoCV, RidgeCV
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

SEED = 42

X, y = fetch_california_housing(return_X_y=True, as_frame=True)
X.shape

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.9, shuffle=True)

lr = LinearRegression(n_jobs=-1)
lr.fit(X, y)

print(lr.intercept_)
print(lr.coef_)
print(lr.score(X_test, y_test))

y_pred = lr.predict(X_test)

mse = mean_squared_error(y_true=y_test, y_pred=y_pred)

pred_0_by_hand = np.sum(X_test.values[0] * lr.coef_) + lr.intercept_
pred_0 = lr.predict(X_test.values[0].reshape(1, -1))[0]

mse_0_by_hand = np.power(y_test.values[0] - y_pred[0], 2)
mse_0 = mean_squared_error([y_test.values[0]], [y_pred[0]])


lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)

print(lasso.intercept_)
print(lasso.coef_)
print(lasso.score(X_test, y_test))

y_pred = lasso.predict(X_test)

mse_lasso = mean_squared_error(y_true=y_test, y_pred=y_pred)

num_alphas = 200
alphas = np.linspace(0.01, 10, num_alphas)
lasso_cv = LassoCV(alphas=alphas, cv=5, random_state=SEED)
lasso_cv.fit(X_train, y_train)

print(lasso_cv.intercept_)
print(lasso_cv.coef_)
print(lasso_cv.score(X_test, y_test))


y_pred = lasso_cv.predict(X_test)
mse_lasso_cv = mean_squared_error(y_true=y_test, y_pred=y_pred)


n_alphas = 200
ridge_alphas = np.logspace(-2, 6, n_alphas)
ridge_cv = RidgeCV(alphas=ridge_alphas, scoring="neg_mean_squared_error", cv=3)
ridge_cv.fit(X_train, y_train)

print(ridge_cv.intercept_)
print(ridge_cv.coef_)
print(ridge_cv.score(X_test, y_test))

y_pred = ridge_cv.predict(X_test)
mse_ridge_cv = mean_squared_error(y_true=y_test, y_pred=y_pred)
