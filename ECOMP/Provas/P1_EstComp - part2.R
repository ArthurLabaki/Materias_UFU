# Primeira Prova de Estatistica Computacional - Parte 2
# Arthur do Prado Labaki
# 11821BCC017


# Exercicio 1

#A
# Sendo g(x) = x/(1+x^2)^2 e y = 1/1+x
# a Integral[0, 1] h(y) dy será 1*1/(1+x)^2 em q 1 é h(y) e 1*1/(1+x)^2 é o dy (dy = dx/(1+x)^2)

x <- runif(100000, 0, 1)   #cem mil numeros entre 0 e 1
g <- 1*1/((1+x)^2)
esp <- sum(g)/100000       #Estimativa - E[g(x)]
resp = 1*esp               #b-a*esp

#B
eixox <- seq(0,10,length.out = 1000)
gx <- eixox/1+(2*eixox)^2 + eixox^4
plot(eixox, gx, type = "l")

# Exercicio 2

#A
# Sim, pois começando em 0, após a primeira jogada ele ira para uma casa impar e
# e sua proxima jogada em uma casa par, pois sera sempre o valor da casa atual +1 ou -1
# sendo assim, é necessario um numero par de rodadas para voltar a casa inicial, pois
# o numero de jogadas da moeda infere se a casa é par ou impar, e é necessario ser par.(2n, sendo n o numero de jogadas)

#B

#-1 coroa 1 cara
casa <- c(0)
origem4 <- c()
origem6 <- c()
origem10 <- c()
origem20 <- c()

for(j in 1:100000){
  for(i in 2:21){  #joguei 20 moedas para ter somente eté a casa 21, que seria o passo 20
    moeda <- sample(c(-1,1), size=1, replace=TRUE)
    casa[i] <- casa[i-1] + moeda
  }
  if(casa[5] == 0){ # casa 5 é o passo 4, pois a casa 1 é a origem
    origem4[j] <- 1
  } else{
    origem4[j] <- 0
  }
  if(casa[7] == 0){ # passo 6
    origem6[j] <- 1
  } else{
    origem6[j] <- 0
  }
  if(casa[11] == 0){ # passo 10
    origem10[j] <- 1
  } else{
    origem10[j] <- 0
  }
  if(casa[21] == 0){ # passo 20
    origem20[j] <- 1
  } else{
    origem20[j] <- 0
  }
  casa = c(0)
}
p4 <- sum(origem4)/100000
p6 <- sum(origem6)/100000
p10 <- sum(origem10)/100000
p20 <- sum(origem20)/100000

h <- choose(2*n, n)*0.5^(2*n) # sendo 2n o n de passos
# choose calcula o coeaficiente binomial( n k ) = n! / k!(n-k)! e (1/2)^2n seria o complemento da formula
# A formula se trata de uma combinação, em q n seria o numero de passos e k a distancia maxima possivel da origem
