# Primeira Prova de Estatistica Computacional
# Arthur do Prado Labaki
# 11821BCC017


# Questão 1

#A

x1 <- runif(100000, 0, 6)   #cem mil numeros entre 0 e 6
g1 <- x1 / (1 + (2*(x1*x1)) + (x1*x1*x1*x1))  # g é o f(x) em "integral[0,6] f(x)dx"
esp1 <- sum(g1)/100000   #Estimativa - E[g(x)]
resp1 = 6*esp1         #(b-a) = 6-0 = 6

#B

EstimativaIntegral = function(n){   # Uma função em que n representa o 6 do exercico anterior
x <- runif(100000, 0, n)
g <- x / (1 + (2*(x*x)) + (x*x*x*x))
esp <- sum(g)/100000
resp = n*esp; resp }   # resp é o que ira retornar
      

# Questão 2

dado1 <- sample(1:6, size =100000, replace = TRUE)
dado2 <- sample(1:6, size =100000, replace = TRUE)
dado3 <- sample(1:6, size =100000, replace = TRUE)
dado4 <- sample(1:6, size =100000, replace = TRUE)
dado5 <- sample(1:6, size =100000, replace = TRUE)  #dados jogados cem mil vezes

#A

sucessodados <- c()

for (i in 1:100000) {  #Probabilidade de algum deles cair 2
  if(dado1[i] == 2 || dado2[i] == 2 || dado3[i] ==2 || dado4[i] == 2 || dado5[i]==2) {
    sucessodados[i] <- 1  #Se algum cair 2 é sucesso (1)
  } else{
    sucessodados[i] <- 0  #Caso não é fracasso(0)
  }
}
probabilidade2 <- sum(sucessodados)/100000  # Media de succesos dos dados

#B

somadados <- c()
for (j in 1:100000) {   #Soma dos 5 dados
  somadados[j] <- dado1[j] + dado2[j] + dado3[j] + dado4[j] + dado5[j]
}

sucesso14 <- c()
for (i in 1:100000) {   #Probabilidade da soma dos 5 dados serem 14
  if(somadados[i] == 14) {
    sucesso14[i] <- 1
  } else {
    sucesso14[i] <- 0
  }
}
probabilidade14 <- sum(sucesso14)/100000 # Media de sucesso dos dados em dar 14

#C

diferentes <- c()

for (i in 1:100000) {  #Probabilidade deles serem diferentes entre si
  if(dado1[i] == dado2[i] || dado1[i] == dado3[i] || dado1[i] == dado4[i] || dado1[i] == dado5[i]){ # se o dado 1 for igual ao outros dados
    diferentes[i] <- 0
  } else if(dado2[i] == dado3[i] || dado2[i] == dado4[i] || dado2[i] == dado5[i]){ # se o dado 2 for igual ao outros dados
    diferentes[i] <- 0
  } else if (dado3[i] == dado4[i] || dado3[i] == dado5[i]){ # se o dado 3 for igual ao outros dados
    diferentes[i] <- 0
  }else if (dado4[i] == dado5[i]){ # se o dado 4 for igual ao outros dados
    diferentes[i] <- 0
  } else {
    diferentes[i] <- 1   # Se nenhum deles forem iguais entre si, todos são diferentes
  }
}
probabilidadedif <- sum(diferentes)/100000  # Media de sucesso dos dados serem diferentes entre si


# Questão 3 

# Irei lancar 3 vezes a moeda, se não sair uma sequencia, ira lançar novamente a moeda até sair alguma sequencia

moeda1 <- sample(0:1, size = 3, replace = TRUE)  # Moeda 1 lançada apenas 3 vezes
sucessop <- c()
j <- 1   #Usei uma variavel para marcar o numero de vitorias entre eles
#Coroa 0
#Cara 1
 for (i in 1:100000) {
   if(moeda1[i] == 0 && moeda1[i+1] == 0 && moeda1[i+2] == 1 ){  # Se sair a sequecia da patti ela ganha (0,0,1)
     sucessop[j] <- 1
     j = j + 1
   }
   else if (moeda1[i] == 0 && moeda1[i+1] == 1 && moeda1[i+2] == 0) {    # Se sair a sequencia de Bob, Patti perde (0,1,0)
     sucessop[j] <- 0
     j = j + 1
   }
   moeda1[i+3] <- sample(0:1, size = 1, replace = TRUE)  #Joga a moeda novamente
 }

probabilidadepatti  <- sum(sucessop)/j  # Media de sucesso da Patti
