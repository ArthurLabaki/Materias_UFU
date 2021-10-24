#Terceira Lista de Exercicios: O Metodo de Monte Carlo
#Arthur do Prado Labaki - 11821BCC017
#Trabalho individual

# Exercicio 1

sucessoamigo <- c()
for(j in 1:100000){
  amigo <- sample(1:4)
  if(amigo[1] == 1 || amigo[2] == 2 || amigo[3] == 3 || amigo[4] == 4){
    sucessoamigo[j] <- 0
  }
  else{
    sucessoamigo[j] <- 1
  }
}

ramigo <- sum (sucessoamigo) / 100000


# Exercicio 2

dado1 <- sample(1:6, size =100000, replace = TRUE)
dado2 <- sample(1:6, size =100000, replace = TRUE)

somadados <- c()
sucessodados <- c()

for (i in 1:100000) {
  somadados[i] <-dado1[i] + dado2[1]
  if(somadados[i] == 7 || somadados[i] == 11){
    sucessodados[i] <- 1
  }
  else{
    sucessodados[i] <- 0
  }
}
rdados <- sum(sucessodados)/100000


# Exercicio 3

dado3 <- sample(1:6, size =100000, replace = TRUE)
urna1 <- sample(c(1,1,1,1,1,1,2,2,2,3,3,3,3), size = 100000,replace = TRUE) # 1=preta, 2=braca, 3=vermelha
urna2 <- sample(c(1,1,1,2,2,2,2,2,3,3), size = 100000,replace = TRUE)
urna3 <- sample(c(1,1,1,1,2,2,3,3), size = 100000,replace = TRUE)

resultadourna <- c()

for(i in 1:100000){
  if(dado3[i] == 5){
    resultadourna[i] <- urna1[i]
  }
  else if(dado3[i] == 2 || dado3[i] == 3 ){
    resultadourna[i] <- urna3[i]
  }
  else{
    resultadourna[i] <- urna2[i]
  }
}

sucessoverm <- c()

for(j in 1:100000){
  if(resultadourna[j] == 3){
    sucessoverm[j] <- 1
  }
  else{
    sucessoverm[j] <- 0
  }
}

rurna <- sum(sucessoverm)/100000


# Exercicio 4

dado1 <- sample(1:6, size =100000, replace = TRUE)
dado2 <- sample(1:6, size =100000, replace = TRUE)
sucessocraps <- c()

for (i in 1:100000) {
  if(dado1[i]+dado2[i] == 7 || dado1[i]+dado2[i] == 11){
    sucessocraps[i] <- 1
  }
  else if(dado1[i]+dado2[i] == 2 || dado1[i]+dado2[i] == 3 ||dado1[i]+dado2[i] == 12){
    sucessocraps[i] <- -0
  }
  else{
    reroll <- -1
    while (reroll == -1) {
      dadoteste1 <-sample(1:6, size = 1)
      dadoteste2 <-sample(1:6, size = 1)
      if(dadoteste1 + dadoteste2 == dado1[i]+dado2[i]){
        reroll <- 1
      }
      else if(dadoteste1 + dadoteste2 == 7){
        reroll <- 0
      }
    }
    sucessocraps[i] <- reroll
  }
}

rcraps <- sum(sucessocraps)/100000


# Exercicio 5 (No trabalho não tem numero e nem pergunta)

dado1 <- sample(1:6, size =100000, replace = TRUE)
dado2 <- sample(1:6, size =100000, replace = TRUE)

somaseq <- c()
sucessoseq <- c()

for (i in 1:100000) {
  somaseq[i] <- dado1[i] + dado2[i]
}
s <- 1
for(j in 1:100000){    # usei o s para retirar os valores nullos da sucessoseq (NA), criando um vetor com somente valores de 0 e 1
  if(somaseq[j] == 9 || somaseq[j] == 11){
    sucessoseq[s] <- 1
    s <- s+1
  }
  else if(somaseq[j] == 2){
    sucessoseq[s] <- 0
    s <- s+1
  }
  else if(somaseq[j] == 5 && somaseq[j+1] == 4 && somaseq[j+2] == 5){
    sucessoseq[s] <- 1
    s <- s+1
  }
  else if(somaseq[j] == 4 && somaseq[j+1] == 5 && somaseq[j+2] == 6 && somaseq[j+3] == 12 && somaseq[j+4] == 4){
    sucessoseq[s] <- 1
    s <- s+1
  }
  else if(somaseq[j] == 4 && somaseq[j+1] == 11 && somaseq[j+2] == 7){
    sucessoseq[s] <- 0
    s <- s+1
  }
  else if(somaseq[j] == 8 && somaseq[j+1] == 5 && somaseq[j+2] == 2 && somaseq[j+3] == 3 && somaseq[j+4] == 9 && somaseq[j+5] == 7){
    sucessoseq[s] <- 0
    s <- s+1
  }
}

rseqs <- sum(sucessoseq)/100000


# Exercicio 6 (No trabalho, esta como 5, mas não numerou o anterior)

#a
A = (-1-2)*1  # (b-a)*H
count = 0
N = 100000
for(i in 1:1000){
  x = runif(1,-1,2)
  y = runif(1,0,1)
  z = cos(x)*cos(x)
  if(y <= z){
    count = count + 1
  }
}
prop = count/N
integral = prop*A

#b
A2 = (pi-0)*1  # (b-a)*H
count2 = 0
N = 100000
for(i in 1:1000){
  x2 = runif(1,0,pi)
  y2 = runif(1,0,1)
  z2 = cos(x)*cos(x)
  if(y2 <= z2){
    count2 = count2 + 1
  }
}
prop2 = count2/N
integral2 = prop2*A2

