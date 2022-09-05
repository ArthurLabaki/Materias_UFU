# Arthur do Prado Labaki
# 11821BCC017
# Programa para ler 5 numeros reais (float) e imprimir a media

.data
    array:      .space 20   # 5 float com 4 bits cada
    numero:	.float 5    # Quantidade de numeors
    
.text  

	addi $t0, $zero, 0	# Indice do array (posição)
	
	li $v0, 6
	syscall
	swc1 $f0, array($t0)	# Salva numero lido na primeira posição do array
	addi $t0, $t0, 4
	
	li $v0, 6
	syscall	
	swc1 $f0, array($t0)	# Salva na segunda posição e assim por diante
	addi $t0, $t0, 4
	
	li $v0, 6
	syscall
	swc1 $f0, array($t0)
	addi $t0, $t0, 4
	
	li $v0, 6
	syscall
	swc1 $f0, array($t0)
	addi $t0, $t0, 4
	
	li $v0, 6
	syscall
	swc1 $f0, array($t0)
	addi $t0, $t0, 4
	
	addi $t0, $zero, 0	# Zera o indice
	
	lwc1 $f2, array($t0)	# Le a primeira posição do array e salva em f2
	addi $t0, $t0, 4
	
	lwc1 $f4, array($t0)	# Le a segunda posição do array e salva em f4
	addi $t0, $t0, 4
	
	add.s $f6, $f2, $f4	# Soma os 2 numeros reais e salva em f6
	
	lwc1 $f2, array($t0)	# Le o proximo numero do array e soma com f6
	addi $t0, $t0, 4
	
	add.s $f6, $f6, $f2	# Soma todos os 5 numeros do array
	
	lwc1 $f2, array($t0)
	addi $t0, $t0, 4
	
	add.s $f6, $f6, $f2
	
	lwc1 $f2, array($t0)
	
	add.s $f6, $f6, $f2
	
	lwc1 $f8, numero	# Carrega para o registrador f8 a quantidade de numeros (5)
	div.s $f6, $f6, $f8	# Divide a soma por 5 (media)
	
	li $v0, 2
	add.s $f12, $f12, $f6	# Mostra o resultado na tela
	syscall
	
	li $v0, 10		# Finaliza o sistema
	syscall