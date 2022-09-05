# Arthur do Prado Labaki
# 11821BCC017

.data
	Fibo: .asciiz "Digite o n de Fibonacci \n"
	
.text
main:
	li $v0, 4		# Imprime na tela a mensagem
	la $a0, Fibo
	syscall
	
	li $v0, 5		# Le o numero
	syscall
	move $a0, $v0
	jal fibonacci		# Chama a funcão fibonacci
	move $a0, $v0
	
	li $v0, 1		# Imprime a resposta
	addi $a0, $a0, 0
	syscall
	
	li $v0, 10		# Finaliza o programa
	syscall		

fibonacci:
	bgt $a0, 1, recursao	# Se o n (a0) for maior que 1, chama a função recursao
	move $v0, $a0
	jr $ra			# Volta para a função main

recursao:
	sub $sp, $sp, 12	
	sw $ra, 0($sp)
	
	sw $a0, 4($sp)
	add $a0, $a0, -1	# n-1
	jal fibonacci		# Chama fibonacci 
	lw $a0, 4($sp)		# Volta para n
	sw $v0, 8($sp)		# Salva fibonacci de n-1
	
	add $a0, $a0, -2	# n-2
	jal fibonacci		# Chama fibonacci 
	
	lw $t0, 8($sp)		
	add $v0, $t0, $v0	# Soma n-1 e n-2
	
	lw $ra, 0($sp)		
	add $sp, $sp, 12 		
	jr $ra			# Conclui a função