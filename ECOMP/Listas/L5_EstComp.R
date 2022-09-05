# Quinta Lista de Exercícios: Anáalise de Regressão e Agrupamento Hierárquico

# Arthur do Prado Labaki
# 11821BCC017

###############
# Exercicio 1 #
###############

pinguins <- read.csv("penguins_size.csv", header = TRUE, )

# Parte A

media_peso <- mean(pinguins$body_mass_g, na.rm = TRUE)
media_asa <- mean(pinguins$flipper_length_mm, na.rm = TRUE)
desvio_peso <- sd(pinguins$body_mass_g, na.rm = TRUE)
desvio_asa <- sd(pinguins$flipper_length_mm, na.rm = TRUE)

# Parte B

p <- c("Adelie")    # Indentificar todas as 3 especies
n <- 1
for (i in 1:344) {
  if(p[n] != pinguins$species[i]){
    n <- n + 1
    p[n] <- pinguins$species[i]
  }
}

p1 <- c()   # Variaveis para separar em 3 pesos, 3 tamanho de asas e 3 contadores
p2 <- c()
p3 <- c()
c1 <- 1
c2 <- 1
c3 <- 1
a1 <- c()
a2 <- c()
a3 <- c()

for (j in 1:344){   # Separa os dados nos vetores designados
  if(pinguins$species[j] == "Adelie"){
    p1[c1] <- pinguins$body_mass_g[j]
    a1[c1] <- pinguins$flipper_length_mm[j]
    c1 <- c1 + 1
  } else if(pinguins$species[j] == "Chinstrap"){
    p2[c2] <- pinguins$body_mass_g[j]
    a2[c2] <- pinguins$flipper_length_mm[j]
    c2 <- c2 + 1
  }else if(pinguins$species[j] == "Gentoo"){
    p3[c3] <- pinguins$body_mass_g[j]
    a3[c3] <- pinguins$flipper_length_mm[j] 
    c3 <- c3 + 1}
}

media_p1 <- mean(p1, na.rm = TRUE)    # Média dos pesos (p1, p2, p3) e do tamanho das asas (a1, a2, a3)
media_p2 <- mean(p2, na.rm = TRUE)
media_p3 <- mean(p3, na.rm = TRUE)
media_a1 <- mean(a1, na.rm = TRUE)
media_a2 <- mean(a2, na.rm = TRUE)
media_a3 <- mean(a3, na.rm = TRUE)

desvio_p1 <- sd(p1, na.rm = TRUE)    # Desvio padrao dos pesos e do tamanho das asas
desvio_p2 <- sd(p2, na.rm = TRUE)
desvio_p3 <- sd(p3, na.rm = TRUE)
desvio_a1 <- sd(a1, na.rm = TRUE)
desvio_a2 <- sd(a2, na.rm = TRUE)
desvio_a3 <- sd(a3, na.rm = TRUE)

# parte D

plot(pinguins$flipper_length_mm, pinguins$body_mass_g, pch = 16, xlab = "Tamanho da asa", ylab = "peso do pinguim", cex = 1.5)

# parte E

r <-cor(pinguins$flipper_length_mm, pinguins$body_mass_g)   # Não funciona se não for retirado os nulos 

#parte G

fit <- lm(pinguins$body_mass_g ~ pinguins$flipper_length_mm)  # y = 49.69 * x - 5780.83

###############
# Exercicio 2 #
###############

mat <- dist(c(0,9,3,6,11,9,0,7,5,10,3,7,0,9,2,6,5,9,0,8,11,10,2,8,0))

fit1 <- hclust(mat, method = "complete")
plot (fit1)
rect.hclust(fit1, k=2)

fit2 <- hclust(mat, method = "single")
plot (fit2)
rect.hclust(fit1, k=2)
