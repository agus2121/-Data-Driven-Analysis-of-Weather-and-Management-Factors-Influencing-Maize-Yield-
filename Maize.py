import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import numpy as np
df = pd.read_csv(r'C:\data\DATA\Crop_Yield.csv')

#CONVERTING BOLEAN TO INTEGER
df['Fertilizer_Used'] = df['Fertilizer_Used'].astype(int)
df['Irrigation_Used'] = df['Irrigation_Used'].astype(int)
#encoding categorical
df['Weather_Condition'] = df['Weather_Condition'].map({
    'Sunny' : 1,
    'Cloudy' : 2,
    'Rainy' : 3
})

#fokus ambil data jagung saja
df_maize = df[df['Crop']== 'Maize']

#melihat distribusi data
num = ['Yield_tons_per_hectare','Days_to_Harvest','Temperature_Celsius','Rainfall_mm']
plt.figure(figsize=(12,10))
for i, col in enumerate(num,1):
    plt.subplot(2,3,i)
    sns.histplot(df_maize[col], kde = True)
    plt.title(f'Distribution of {col}')
plt.tight_layout
plt.show()

#melihat apa ada outlier data
num = ['Yield_tons_per_hectare','Days_to_Harvest','Temperature_Celsius','Rainfall_mm']
plt.figure(figsize=(10,7))
for i, col in enumerate(num,1):
    plt.subplot(2,3,i)
    sns.boxplot(df_maize[col])
    plt.title(f'Distribution of {col}')
plt.tight_layout
plt.show()

#melihat data outlier berdasar plot box
df_maize[df_maize['Yield_tons_per_hectare']<= 3]
df_maize[df_maize['Yield_tons_per_hectare']>= 6]

#melihat korelasi antar variabel
sns.heatmap(df_maize.corr(numeric_only=True),annot=True)

#melihat hubungan antara temperature dengan Yield
plt.figure(figsize=(7,4))
sns.regplot(data=df_maize, x="Temperature_Celsius", y="Yield_tons_per_hectare")
plt.title("Temperature dengan Yield")
plt.xlabel('Temperature(C)')
plt.ylabel('Yield(ton/ha)')
plt.show()

#yield berdasarkan jenis tanah
print(df_maize.groupby(["Soil_Type"])["Yield_tons_per_hectare"].mean())
print(df_maize.groupby(["Fertilizer_Used"])["Yield_tons_per_hectare"].mean())
print(df_maize.groupby(["Irrigation_Used"])["Yield_tons_per_hectare"].mean())
print(df_maize.groupby(["Weather_Condition"])["Yield_tons_per_hectare"].mean())

#drop kategorikal kolom untuk analisis regres
df_maize_clean = df_maize.drop(['Crop','Region','Soil_Type'], axis=1)

#membagi data untuk pelatihan dan uji
X = df_maize_clean.drop(['Yield_tons_per_hectare'],axis=1)
y = df_maize_clean['Yield_tons_per_hectare']
x_train, x_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

#analisis regresi
model = LinearRegression()
model.fit(x_train, y_train)
coefficients = pd.DataFrame({
    "Variable": X.columns,
    "Coefficient": model.coef_
})

#prediksi dengan regresi linear
y_pred = model.predict(x_test)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
print("MAE:", mae)
print("RMSE:", rmse)
print("R-squared:", r2)

#standardized koefifisen
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
model2 = LinearRegression()
model2.fit(X_scaled, y)
importance = pd.DataFrame({
    "Variable": X.columns,
    "Standardized_Coeff": model2.coef_
})
importance.sort_values(by="Standardized_Coeff", key=abs, ascending=False)

#pembuatan scatter plot antara yield actual dan predict
plt.figure(figsize=(6,6))
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Yield")
plt.ylabel("Predicted Yield")
plt.title("Actual vs Predicted Yield (Linear Regression)")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()])
plt.show()