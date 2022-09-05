# Module Name: -- pc3-arthur-labaki
# Functions: Collatz conjecture
# Nome: Arthur do Prado Labaki
# Matricula: 11821BCC017
# Data de inicio da implementaçao: 12/09/2019
# Data de fim da implementaçao: 12/09/2019
# Linguagem: Assembly MIPS

.data
	Ini: .asciiz "Inicio do Programa Collatz\n"
	K: .asciiz "K = "
	Seq: .asciiz "Sequência : "
	Esp: .asciiz " "
.text
	li $v0, 4
	la $a0, Ini
	syscall 
	# Carrega e mostra na tela o Ini (mensagem)
	
	li $v0, 4
	la $a0, K
	syscall 
	# Carrega e mostra na tela o K (mensagem)
	
	li $v0, 5
	syscall
	move $t0, $v0
	# Le um inteiro do teclado e salva no registrador t0
	
	li $v0, 4
	la $a0, Seq
	syscall 
	# Carrega e mostra na tela a Seq (mensagem)
	

	li $v0, 1
	move $a0, $t0
	syscall
	li $v0, 4
	la $a0, Esp
	syscall 
	# Carrega e mostra na tela o numero de K (e imprime " " também)
	
Loop:	li $s3, 1 			# Inicio do LOOP
	beq $s3, $t0, Fim		# Se o K for 1 ele sai do LOOP
	li $s0, 2
	div $t0, $s0
	mfhi $t1
	# Divide o K por 2 para ver se é par 
	
	li $s1, 0
	bne $t1, $s1, Else
	# Se for par ele continua até o "j FimSe"
	
	div $t0, $s0
	mflo $t0
	# Divide o K por 2 e salva a divisao no proprio K
	
	li $v0, 1
	move $a0, $t0
	syscall
	li $v0, 4
	la $a0, Esp
	syscall 
	# Carrega e mostra na tela o numero de K (e imprime " " também)
	
	j FimSe 			# Vai para o FimSe para recomeçar o LOOP
	
Else:	li $s2, 3			# Se o K for impar 
	mulo $t2, $t0, $s2
	li $s3, 1
	add $t0, $s3, $t2
	# Multiplica o K por 3 e soma mais 1
	
	li $v0, 1
	move $a0, $t0
	syscall
	li $v0, 4
	la $a0, Esp
	syscall 
	# Carrega e mostra na tela o numero de K (e imprime " " também)
	
FimSe:
	j Loop				# Reinicia o LOOP
	
Fim:					# K é igual a um 
	li $v0, 10
	syscall		
	#Finaliza o sistema
