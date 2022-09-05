# Segunda Prova de Estatistica Computacional

# Arthur do Prado Labaki
# 11821BCC017

###############
# Exercicio 1 #
###############

#A)

# Usando o método da transformação inversa
# f-1 = -50ln(1-x)

ex1 <- function(n){    # Chama a função ex1 (n), em que n é o numero de valores gerados para T
  t <- c()
  for (i in 1:n) {
    u <- runif(1, 0, 1)
    t <- c(t, (-50) * log(1-u))    # Utiliza a função inversa da distribuição acumulada
  }
  return(t)
}

#B)

s <- c()    # Utiliza o metodo de monte carlo para calcular a probabilidade de T for maior que 6
for(j in 1:10000){
  test <- ex1(1)
  if (test > 6){
    s[j] <- 1
  }else{
    s[j] <- 0
  }
}
prob <- sum(s)/10000    # Variavel com o resultado

#C)

s <- c()    # Utiliza o metodo de monte Carlo para calcular a probabilidade de T ser maior que 12
for(j in 1:10000){    # E depois calcula se esse valor é maior que 18
  test <- ex1(1)
  if (test > 12 ){
    if (test > 18){
      s[j] <- 1
    }else{
      s[j] <- 0
      }
  }else{
    s[j] <- 0
  }
}

prob <- sum(s)/10000    # Variavel com o resultado


###############
# Exercicio 2 #
###############
 
ex2 <- function (n){    # Chama a função ex2 (n), em que n é o numero de valores de uma variavel X
  x <- c()
  for (i in 1:n) {
  cont <- 0
  soma <- 0
  repeat{
    u <- runif(1, 0, 1)   # A função gera valores aleatorios entre 0 e 1
    soma <- soma + u      # Guardando e somando na variavel soma
    cont <- cont + 1      # Se o valor ultrapassar 1, a função para e salva o numero de somas em X
    if (soma > 1){        # Ai ele repete conforme o numero n digitado
      break
    }
  }
  x[i] <- cont
  }
  return(x)
}

tam <- 100000             # Coloquei 100000 como tamanho de n
esp <- mean(ex2(tam))     # Gera E[X]


###############
# Exercicio 3 #
###############

#A)
iris <- read.table("iris.txt", sep = ",", header = TRUE)

#B)

esp1 <- c()    # Variaveis para guardar o vetor de cada especie
esp2 <- c()
esp3 <- c()
count1 <- 1    # Contador
count2 <- 1
count3 <- 1
esp4 <- c()
esp5 <- c()
esp6 <- c()

for (i in 1:150) {
  if(iris$especie[i] == "setosa"){
    esp1[count1] <- iris$comprimento_petala[i]
    esp4[count1] <- iris$largura_petala [i]
    count1 <- count1 + 1
  } else if(iris$especie[i] == "versicolor"){
    esp2[count2] <- iris$comprimento_petala[i]
    esp5[count2] <- iris$largura_petala[i]
    count2 <- count2 + 1
  } else{
    esp3[count3] <- iris$comprimento_petala[i]
    esp6[count3] <- iris$largura_petala[i]
    count3 <- count3 + 1
  }
}

media_esp1_comp <- mean(esp1, na.rm = TRUE)    # Média e desvio padrao das 3 especies
media_esp1_larg <- mean(esp4, na.rm = TRUE)    # Sendo o primeiro do comprimento e o segundo da largura

media_esp2_comp <- mean(esp2, na.rm = TRUE)    # A media e o desvio padrao das plantas analisadas mostram que
media_esp2_larg <- mean(esp5, na.rm = TRUE)    # Seu comprimento e sua largura esão possivelmente relacionadas

media_esp3_comp <- mean(esp3, na.rm = TRUE)    # Pois a especie 1 tem tanto o comprimento e a largura menor em relação as outras
media_esp3_larg <- mean(esp6, na.rm = TRUE)    # o mesmo ocorre com as outras especies, sendo a 3 a maior delas

desvio_esp1_comp <- sd(esp1, na.rm = TRUE)
desvio_esp1_larg <- sd(esp4, na.rm = TRUE)

desvio_esp2_comp <- sd(esp2, na.rm = TRUE)
desvio_esp2_larg <- sd(esp5, na.rm = TRUE)

desvio_esp3_comp <- sd(esp3, na.rm = TRUE)
desvio_esp3_larg <- sd(esp6, na.rm = TRUE)

#C)

plot(iris$largura_petala, iris$comprimento_petala, pch = 16, xlab = "Largura da pétala", ylab = "Comprimento da pétala", cex = 1.5)

#D)

r <- cor(iris$largura_petala, iris$comprimento_petala)
# o coeficiente de correlação indica que a largura e o comprimento estao fortemente relacionadas
# (relação linear forte e positiva entre largura e comprimento das pétalas, com aproximadamente 96%)

#E)

fit <- lm(iris$comprimento_petala ~ iris$largura_petala)    # Y = 2.222 * x + 1.099 

#F)
# Variando 0.5cm na largura da pétula provocaria uma variação de 1.11 cm no seu comprimento, demonstrado pela reta de regressão linear

#G)
# O coeficiente de determinação do modelo seria r^2
cdet <- r * r
# Cerca de 92% da variação do comprimento das petalas podem ser explicada pela equação da reta de regressão.

