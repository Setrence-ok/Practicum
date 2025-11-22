import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

class LinearRegression() :

    def __init__(self, learning_rate, iterations) :
        self.l_rate = learning_rate
        self.iter = iterations
        self.w = None
        self.b = None
        self.loss_history = []

    def fit(self, X, Y) :
        self.w = np.zeros(X.shape[1])
        self.b= 0

        for i in range(self.iter) :
            e = self.update_weights(X, Y)
            self.loss_history.append(e)

    def update_weights(self, X, Y) :
        preds = self.predict(X)
        e = preds - Y
        self.w -= self.l_rate * (e.T @ X) / X.shape[0]
        self.b -= self.l_rate * np.sum(e) / X.shape[0]
        return e * e

    def predict( self, X ) :
        return X @ self.w + self.b

df = pd.read_csv( "salary_data.csv" )

X = df.iloc[:,:-1].values
Y = df.iloc[:,1].values

model = train_test_split(X, Y)

model = LinearRegression(iterations = 1000, learning_rate = 0.01)
model.fit(X, Y)

Y_pred = model.predict(X)

print(*np.round(model.w, 2))
print(np.round(model.b, 2))

plt.scatter(X, Y, color = 'blue')
plt.plot(X, Y_pred, color = 'orange')
plt.title('Зависимость зарплаты от опыта')
plt.xlabel('Число лет опыта')
plt.ylabel('Зарплата')

plt.show()