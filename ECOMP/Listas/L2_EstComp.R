#Segunda Lista de Exercicios: Vetores no R
#Arthur do Prado Labaki - 11821BCC017
#Trabalho individual

#Exercicio 1
Vetor1 <- seq(1,20) 
vetor2 <- seq (20,1)
vetor3 <- c(seq(1,20),seq(19,1))
vetor4 <- c(0.1^3*0.2^1, 0.1^6*0.2^4, 0.1^9*0.2^7, 0.1^12*0.2^10, 0.1^15*0.2^13, 0.1^18*0.2^16, 0.1^21*0.2^19, 0.1^24*0.2^22, 0.1^27*0.2^25, 0.1^30*0.2^28, 0.1^33*0.2^31, 0.1^36*0.2^34)
vetor5 <- rep(c(4,6,3),10)
vetor6 <- c(rep(c(4,6,3),10),4)


#Exercicio 2
xcos <- seq(3,6,0.1)   #pontos de x
vetorcos <- exp(xcos)*cos(xcos)   #vetor


#Exercicio 3
i1 <- seq(10,100)
seq1 <- (i1^3) + 4*(i1^2)
soma1 <- sum(seq1)  #somatorio a

i2 <- seq(10,25)
seq2 <-  ((2^i2)/i2) + ((3^i2)/(i2^2))
soma2 <- sum(seq2)   #somatorio b


#Exercicio 4
xVec <- sample(0:999, 250, replace=T)
yVec <- sample(0:999, 250, replace=T)
imparx <- xVec
imparxvec = imparx[imparx %%2!=0]   #a

xvet = xVec[-250]
yvet = yVec[-1]
somaxy <- (yvet - xvet)   #b

senyporconx <- sin(yvet)/cos(xvet)   #c

vetord <- 1:248   #d
i=1
while (i < 249){
  vetord[i] <- xVec[i]+2*xVec[i+1]-xVec[i+2]
  i = i + 1
}


#Exercicio 5
imaiores600 <- which(yVec>600)   #a

maiores600 <- yVec[imaiores600]   #b

xmaiores600 <- xVec[imaiores600]   #c

mediax <- abs(xVec - mean(xVec))^(1/2)   #d

disty200 <- which(yVec> (max(yVec)-200))
dist200 <- yVec[disty200]   #e

parx <- xVec
parxvec = parx[parx %%2==0]   #f

cresc <- sort(yVec)   #g

vetyposi <- 1:83   #h
i=1
h=1
while (h < 84){
  vetyposi[h] <- yVec[i]
  i = i + 3
  h = h + 1
}


#Exercicio 6
prod = 0
i = 2
j = 1
k <- NULL
while(i<40){
  k[j] <- c(i/(i+1))
  prod = cumprod(k)
  i = i + 2
  j = j+1
}
somat = 1
somat = somat + sum(prod)   #soma
