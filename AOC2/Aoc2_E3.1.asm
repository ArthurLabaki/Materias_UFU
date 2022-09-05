# Arthur do Prado Labaki
# 11821BCC017

.data


.text
main:
	addi $v1, $zero, 30
	addi $t4, $zero, 0
	addi $t5, $zero, 1
	addi $s3, $zero, 0
	addi $s2, $zero, 7
	jal seno
	fim:
	li $v0, 2		 # Imprime na tela
	addi $a0, $t7, 0
	syscall
	
	li $v0, 10		# Finaliza o sistema
	syscall	
	
	
seno:	#v1, é o grau (s2 é 7, um n suficientemente bom para o somatorio)  resultado é s7
	beq $s3, $s2, fim	#s3 é um indice comecando em o
	addi $t3, $s3, 0
	addi $t2, $zero, -1
	jal potencia		# -1 ^indice
	
	addi $s7, $t5, 0
	addi $t5, $zero, 1
	
	addi $t2, $v1, 0
	addi $t3, $s3, 0
	addi $t4, $zero, 2
	mult $t3, $t4		# grau ^2*indice + 1
	mflo $t3
	addi $t3, $t3, 1
	addi $t4, $zero, 0
	jal potencia
	
	mult $s7, $t5
	mflo $s7		#multipliquei as 2 potencias
	addi $t5, $zero, 1
	
	addi $t2, $t3, 0	# 2*indice + 1 !
	jal fatorial 
	
	div $s7, $t5		#divide as potencias pelo fatorial
	mflo $s7
	move $t7, $s7
	addi $s3, $s3, 1
	j seno
	
potencia: 	#Condicoes: t2 ^t3 , t4 é o indice e tem q comecar 0, t5 é o resultado e tem q comecar 1, a função saira no exit
	beq $t4, $t3, exit
	mult $t5, $t2
	mflo $t5
	addi $t4, $t4, 1
	j potencia
	
fatorial:	#Condicoes|: t2! , t5 guarda o resultado e tem q comecar com 1, t2 ficara 0, função saira no exit
	beq $t2, $zero, exit
	mult $t5, $t2
	mflo $t5
	addi $t2, $t2, -1
	j fatorial

exit:
	addi $t4,,$zero, 0
	jr $ra