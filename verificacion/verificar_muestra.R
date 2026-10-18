
# Verificación de la muestra de 10 parcelas con R
# Estadística Aplicada - Ingeniería Agrícola

m <- read.csv("muestra10.csv")
y <- m$rendimiento

# Estadísticas descriptivas
media <- mean(y)
mediana <- median(y)
varianza <- var(y)
de <- sd(y)
cv <- 100 * de / media

# Cuartiles y rango intercuartílico
q <- quantile(y, c(0.25, 0.75), type = 7)
ric <- q[2] - q[1]

# Límites de Tukey
li <- q[1] - 1.5 * ric
ls <- q[2] + 1.5 * ric

# Resultados
cat("n =", length(y), "media =", round(media, 3),
    "mediana =", round(mediana, 3), "\n")

cat("Varianza =", round(varianza, 4),
    "Desv. estándar =", round(de, 4),
    "CV =", round(cv, 2), "%\n")

cat("Q1 =", round(q[1], 4),
    "Q3 =", round(q[2], 4),
    "RIC =", round(ric, 4), "\n")

cat("Límite inferior =", round(li, 4),
    "Límite superior =", round(ls, 4), "\n")

cat("Atípicos:",
    m$parcela[y < li | y > ls], "\n")

# Media por riego
print(tapply(y, m$riego, mean))

# Diagrama de caja
boxplot(y, horizontal = TRUE,
        main = "Rendimiento (t/ha) - muestra de 10 parcelas")
