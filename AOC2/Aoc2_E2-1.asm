# Arthur do Prado Labaki
# 11821BCC017

.data
	Array:  .space 40
	Num: .asciiz "Digite 10 numeros:\n"
.text
	li $v0, 4		# Imprime a mensagem "Num"
	la $a0, Num
	syscall
	
	li $v0, 5		# Le um inteiro e salva em um array
	syscall
	addi $t0, $zero, 0
	sw $v0, Array($t0)
	addi $t0, $t0, 4

	li $v0, 5
	syscall
	sw $v0, Array($t0)
	addi $t0, $t0, 4
				# Ex
	li $v0, 5		# Le o numero do teclado
	syscall
	sw $v0, Array($t0)	# Salva o numero inteiro em uma posição do array (t0)
	addi $t0, $t0, 4	# Adiciona 4 em t0, pois cada inteiro ocupa 4 bits na posição do array
				# Repete
	li $v0, 5
	syscall
	sw $v0, Array($t0)
	addi $t0, $t0, 4
	
	li $v0, 5
	syscall
	sw $v0, Array($t0)
	addi $t0, $t0, 4
	
	li $v0, 5
	syscall
	sw $v0, Array($t0)
	addi $t0, $t0, 4
	
	li $v0, 5
	syscall
	sw $v0, Array($t0)
	addi $t0, $t0, 4
	
	li $v0, 5
	syscall
	sw $v0, Array($t0)
	addi $t0, $t0, 4
	
	li $v0, 5
	syscall
	sw $v0, Array($t0)
	addi $t0, $t0, 4
	
	li $v0, 5
	syscall
	sw $v0, Array($t0)
	
	addi $v1, $zero, 0
	addi $t1, $zero, 0
	
	lw $v0, Array($t1)	# Soma todos os elementos do array
	add $v1, $v1, $v0
	addi $t1, $t1, 4
	
	lw $v0, Array($t1)
	add $v1, $v1, $v0
	addi $t1, $t1, 4
				# Ex
	lw $v0, Array($t1)	# Le o numero do array
	add $v1, $v1, $v0	# Soma esse numero com os outros já somados
	addi $t1, $t1, 4	# Adiciona 4 no em t1, para buscar a posição do proximo inteiro
				# Repete
	lw $v0, Array($t1)
	add $v1, $v1, $v0
	addi $t1, $t1, 4
	
	lw $v0, Array($t1)
	add $v1, $v1, $v0
	addi $t1, $t1, 4
	
	lw $v0, Array($t1)
	add $v1, $v1, $v0
	addi $t1, $t1, 4
	
	lw $v0, Array($t1)
	add $v1, $v1, $v0
	addi $t1, $t1, 4
	
	lw $v0, Array($t1)
	add $v1, $v1, $v0
	addi $t1, $t1, 4
	
	lw $v0, Array($t1)
	add $v1, $v1, $v0
	addi $t1, $t1, 4
	
	lw $v0, Array($t1)
	add $v1, $v1, $v0
	
	addi $t1, $zero, 10	# Calcula a media dos 10 numeros
	div $v1, $t1
	mflo $t2
	
	li $v0, 1		 # Imprime na tela
	addi $a0, $t2, 0
	syscall
	
	li $v0, 10		# Finaliza o sistema
	syscall			