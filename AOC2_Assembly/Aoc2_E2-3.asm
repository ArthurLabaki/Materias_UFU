# Arthur do Prado Labaki
# 11821BCC017

.data
	Array:  .space 40
	Num: .asciiz "Digite 10 numeros:\n"
	
.text
main:
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

	addi $t1, $zero, 0		# Envia o numero para a função teste
	li $s2, 2
	lw $v0, Array($t1)	
	jal teste
	
	addi $t1, $t1, 4
	lw $v0, Array($t1)
	jal teste
					# Ex
	addi $t1, $t1, 4		# Adiciona 4 no em t1, para buscar a posição do proximo inteiro
	lw $v0, Array($t1)		# Le o numero do array e salva em v0
	jal teste			# Entra na função teste
					# Repete
	addi $t1, $t1, 4
	lw $v0, Array($t1)
	jal teste
	
	addi $t1, $t1, 4
	lw $v0, Array($t1)
	jal teste
	
	addi $t1, $t1, 4
	lw $v0, Array($t1)
	jal teste
	
	addi $t1, $t1, 4
	lw $v0, Array($t1)
	jal teste
	
	addi $t1, $t1, 4
	lw $v0, Array($t1)
	jal teste
	
	addi $t1, $t1, 4
	lw $v0, Array($t1)
	jal teste
	
	addi $t1, $t1, 4
	lw $v0, Array($t1)
	jal teste
	
	li $v0, 1		 # Imprime na tela
	addi $a0, $t9, 0
	syscall
	
	li $v0, 10		# Finaliza o sistema
	syscall	
	
teste:				# Testa se o numero é impar dividindo ele por 2
	div $v0, $s2		# Se o resto der 0 ele sai da função
	mfhi $s1		# Se não der 0, o numero é impar e entra na função impar
	bne $s1, 0, impar 
	jr $ra
	
impar:				# Se for impar ele soma em t9
	addu $t9, $t9, $v0
	jr $ra