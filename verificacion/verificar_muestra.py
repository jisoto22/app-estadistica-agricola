
# Verificación de la muestra de 10 parcelas

import pandas as pd

m = pd.read_csv("datos/muestra10.csv")
y = m["rendimiento"]

media = y.mean()
mediana = y.median()
var = y.var(ddof=1)
de = y.std(ddof=1)
cv = 100 * de / media

q1, q3 = y.quantile([0.25, 0.75])
ric = q3 - q1

li = q1 - 1.5 * ric
ls = q3 + 1.5 * ric

atipicos = m.loc[
    (y < li) | (y > ls), "parcela"
].tolist()

print(f"n = {len(y)}  media = {media:.3f}  mediana = {mediana:.3f}")
print(f"varianza = {var:.4f}  desv. est. = {de:.4f}  CV = {cv:.2f} %")
print(f"Q1 = {q1:.4f}  Q3 = {q3:.4f}  RIC = {ric:.4f}")
print(f"Límite inferior = {li:.4f}  Límite superior = {ls:.4f}  Atípicos: {atipicos}")
print("\nMedia por riego:")
print(m.groupby("riego")["rendimiento"].mean().round(3))
