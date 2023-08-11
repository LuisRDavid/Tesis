import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv('../Other_files/CurvaB208.csv')
concentration = df['CONCENTRACION'].values.reshape(-1, 1)
absorbance = df['ABS'].values.reshape(-1, 1)

linearRegressor = LinearRegression()
linearRegressor.fit(absorbance, concentration)
concentration_predict = linearRegressor.predict(absorbance)
concentration_predict
m = linearRegressor.coef_[0][0]
c = linearRegressor.intercept_[0]
label = r'$DQO= %0.4fx %+0.4f$' % (m, c)
print(label)
R2 = r2_score(concentration, concentration_predict)
print(R2)

fig = plt.figure()
ax = fig.subplots()
plt.scatter(absorbance, concentration, edgecolors='red')
plt.plot(absorbance, concentration, color='blue', label='Datos experimentales')
plt.plot(absorbance, concentration_predict,
         color='red', label='Tendencia central')
ax.text(0.016, 60, r'$R^2= %0.4f$' % (R2))
ax.text(0.016, 55, label)
ax.set_xlabel('Absorbance')
ax.set_ylabel('Concentration')
ax.set_title('DQO')
plt.legend()
plt.grid()
plt.show()
