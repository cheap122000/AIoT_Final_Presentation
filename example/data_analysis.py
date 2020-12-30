import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mlxtend.plotting import scatterplotmatrix
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from keras.layers import Dense
from keras.models import Sequential

df = pd.read_csv('./solar_data_202003_202007_processed.csv')
df = df[df['kwh']<30]

# hm, ax = plt.subplots(figsize=(12,10))
# corr = df[['HOUR','OPTPWR','IIT','IHT','kwh']].corr(method='pearson')
# cmap = sns.diverging_palette(220, 10, as_cmap=True)
# hm = sns.heatmap(
#     corr,
#     cmap = cmap,
#     square = True,
#     cbar_kws={'shrink': .9},
#     ax = ax,
#     annot = True,
#     annot_kws = {'fontsize': 12}
# )
# plt.show()

# cols = ['HOUR','OPTPWR','IIT','IHT','kwh']
# scatterplotmatrix(df[cols].values, figsize=(12, 10), names=cols, alpha=0.5)
# plt.tight_layout()
# plt.show()

X = df[['HOUR','OPTPWR','IIT','IHT']]
Y = df[['kwh']]
min_max_scaler_X = MinMaxScaler()
min_max_scaler_Y = MinMaxScaler()
X_scale = min_max_scaler_X.fit_transform(X)
Y_scale = min_max_scaler_Y.fit_transform(Y)

X_train, X_test, y_train, y_test = train_test_split(
    X_scale, Y_scale, test_size=0.2, random_state=0
)

model = Sequential()
model.add(Dense(100, input_dim=4, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
print(model.summary())

model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

model.fit(
    X_train, y_train,
    validation_data=(X_test, y_test),
    epochs = 100,
    batch_size = 100,
    verbose = 1
)

y_test_pred = model.predict(X_test)
r2 = r2_score(y_test, y_test_pred)
mse = mean_squared_error(y_test, y_test_pred)
print('MSE: %.3f, R^2: %.3f' % (mse, r2))

test = [[9, 15.8, 36, 41], [10, 7.55, 46, 41]]
t_test = min_max_scaler_X.transform(np.array(test))
pre = model.predict(t_test)
print(min_max_scaler_Y.inverse_transform(pre))

model.save('aiot.h5')