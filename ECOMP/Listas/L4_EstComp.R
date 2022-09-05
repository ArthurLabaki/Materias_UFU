# Quarta lista de exercícios: Simulando variáveis aleatórias
# Arthur do Prado Labaki
# 11821BCC017

###############
# Exercicio 1 # 
###############

ex1 <- function(n) {  # chama a função com "ex1 (n)", sendo o n o numero de valores da variavel aleatoria
p <- 1/3
x <- c()
for(i in 1:n){
  u <- runif(1, 0, 1)
  if(u < p){
    x[i] <- 1
  }else{
    x[i] <- 2
  }
}
n1 <- length (x[x==2])/n
return(n1) }   # Retorna a proporção de valores iguais a 2, sendo n o numero digitado

# Caso não queira a function, basta retirar a linha 9 e 21 e modificar o n das linhas 12 e 20 para o valor esperado.


###############
# Exercicio 2 #
###############

ex2 <- function (p) {  # Chama a função com ex2 (p), sendo p um vetor de proporções
u <- runif (1, 0, 1)
pb = 0
for (i in 1:length(p)){
  pb = pb + p[i]
  if (u < pb){
    print(u)    # Coloquei ela printar o u, para verificar se funcionou
    return(i)   # Retorna o valor da variavel X
  }
}
}

###############
# Exercício 3 #
###############

# Primeira parte

ex3a <- function (p){  # Chama a função ex3a (p), em que p é a proporção
x <- c()
k <- 1
repeat{
  u <- runif(1, 0, 1)
  if (u < p) {
    x <- k
    break
  } else {
    k <- k + 1
  }
}
return(x) }    # Retorna um valor gerado de X

# Segunda parte

ex3b <- function(p, k) {  # Chama a função ex3b (p, k), em que p é a proporção e k o numero de sucessos
j <- 1
x <- c()
for (i in 1:k) {
  j <- 1
  repeat{
    u <- runif(1, 0, 1)
    if (u < p) {
     x[i] <- j
      break
    } else {
     j <- j + 1
    }
  }
}
y <- sum(x)
return(y)    # Retorna Y, sendo a soma do numero de tentativas necessarias para obter o k
}

py <- c()    # Testa 10000 vezes, com p=4/7 e k=3, verificando se o Y foi maior que 8
for (a in 1:10000){
  if(ex3b (4/7, 3) > 8){
    py[a] <- 1
  } else{
    py[a] <- 0
  }
}
result <- sum(py)/10000  # proporção estimada em que P(y > 8)

###############
# Exercício 4 #
###############

# Usando o método da transformação inversa
# f-1 (y) = (-1+ sqrt(1+8y))/2

ex4 <- function(n) {   # Chama a função ex4 (n), em que n é o numero de valores gerados para X
x <- c()
for(i in 1:n){
  u <- runif(1, 0, 1)
  x <- c(x, ((-1 + sqrt(1+(8*u)))/2))
}
return(x)    # Retorna o valor da variavel aleatoria X
}

# Estimando para P(X < 0.7)

estim <- sum(ex4(10000) < 0.7)/10000  # sendo n 10000

# Estimando para E[X]

esp <- mean(ex4(10000))
