# Module Name: -- pc2-arthur-labaki
# Functions: Manipular Numeros Inteiros (Read String)
# Nome: Arthur do Prado Labaki
# Matricula: 11821BCC017
# Data de inicio da implementaçao: 07/09/2019
# Data de fim da implementaçao: 07/09/2019
# Linguagem: Assembly MIPS

.data
	Prog: .asciiz "Programa para efetuar divisao inteira\n"
	Dividendo: .asciiz "Dividendo:"
	Divisor: .asciiz "Divisor:"
	Resultado: .asciiz "\nResultado:"
	Resto: .asciiz "\nResto:"

.text
	li $v0, 4
	la $a0, Prog
	syscall
	# Carrrega e mostra na tela o Prog
	
	li $v0, 4
	la $a0, Dividendo
	syscall 
	# Carrega e mostra na tela o Dividendo (mensagem)
	
	li $v0, 5
	syscall
	# Le um inteiro do teclado
	
	move $t0, $v0
	# Move o numero lido para o registrador t0
	
	li $v0, 4
	la $a0, Divisor
	syscall 
	# Carrega e mostra na tela o Divisor (mensagem)
	
	li $v0, 5
	syscall
	# Le um inteiro do teclado
	
	move $t1, $v0
	# Move o numero lido do teclado para o registrador t1
	
	div $t0,$t1
	# Divide o t0 pelo t1
	
	mflo $t2
	mfhi $t3
	# Salva o resultado da divisao Inteira em t2 e o resto em t3 (resultado pequeno e resultado grande)
	
	li $v0, 4
	la $a0, Resultado
	syscall 
	# Carrega e mostra na tela o Resultado (mensagem)
	
	li $v0, 1
	move $a0, $t2
	syscall
	# Carrega e mostra na tela o t2 (resultado) 
	
	li $v0, 4
	la $a0, Resto
	syscall 
	# Carrega e mostra na tela o Resto (mensagem)
	
	li $v0, 1
	move $a0, $t3
	syscall
	# Carrega e mostra na tela o t3 (resto) 
	
	li $v0, 10
	syscall		
	#Finaliza o sistema