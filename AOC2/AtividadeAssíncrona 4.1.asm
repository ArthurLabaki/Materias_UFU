# Arthur do Prado Labaki
# 11821BCC017
# Imprimir diferença entre pi real e a serie a cada 100 iterações

.data

numIter:  .word 100000  
str1: .asciiz	"\n A serie para "
str2: .asciiz	" iteracoes, retorna o valor: "  
pi :  .float   3.14159265358979324
pular: .asciiz "\n A diferenca entre o pi real e a "
pular1: .asciiz " iteração da serie é:  "

.text
		li $s7, 0		#contador de iteracoes
						
		#termo zero da série
		li $s0, 0
		mtc1 $s0, $f0
		cvt.s.w	$f0, $f0
		
		#divisor da fracao
		li $s1, 1
		mtc1 $s1, $f1
		cvt.s.w	$f1, $f1
		mov.s	$f7, $f1  #cte 1
		
		l.s $f20, pi
		la $s6, numIter	#carrega o num de iteracoes
		lw $s6, 0($s6)	
		
FOR:		beq $s7, $s6, SAI1
		
		#divisor da fracao
		mtc1 $s1, $f1
		cvt.s.w	$f1, $f1

		#computa a fracao
		div.s $f3, $f7, $f1
			
		#testa se eh uma iteracao par ou impar
		#par -> termo positivo, impar -> termo negativo
		andi $t0, $s7, 1 #se t0 for 1 eh impar, senao (0) eh par
		beq $t0, $zero, PAR
		#impar
		sub.s $f0, $f0, $f3

		j SAIIF
		
		
PAR:	#par
		add.s $f0, $f0, $f3	#calcula se o numero da iteração é multiplo de 100 (resto 0)
		li $t6, 100		# e envia para a função ERRO
		div $s7, $t6
		mfhi $t6
		beq $t6, $zero, ERRO
		
SAIIF:		addi $s1, $s1, 2
		addi $s7, $s7, 1
		j FOR
SAI1:
		#primeira parte da resposta
		li $v0, 4
		la $a0, str1
		syscall
		#numero de iteracoes
		li $v0, 1
		move $a0, $s6
		syscall
		#segunda parte da resposta
		li $v0, 4
		la $a0, str2
		syscall
		#aprox. de pi
		
		li $s5, 4
		mtc1 $s5, $f5
		cvt.s.w	$f5, $f5
		
		mul.s $f0, $f0, $f5
		li $v0, 2
		mov.s $f12, $f0
		syscall
		 	
		#return 0
		li $v0, 10
		syscall
		

ERRO:		beq $s7, 0, SAIIF		#a iteração de numero 0 não é para imprimir, comeca em 100 
		li		$t5, 4
		mtc1	$t5, $f25
		cvt.s.w	$f25, $f25
		
		mul.s	$f10, $f0, $f25
		
		li $v0, 4			#imprime a primeira mensagem
		la $a0, pular
		syscall
		
		li $v0, 1			#imprime o numero da iteração
		move $a0, $s7
		syscall
		
		li $v0, 4			#imprime a 2 mensagem
		la $a0, pular1
		syscall
		
		li $v0, 2			#imprime a diferenca entre o pi real e o da devida iteração 
		sub.s $f12, $f20, $f10
		syscall
		
		j SAIIF
