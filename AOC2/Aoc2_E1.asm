# Arthur do Prado Labaki 
# 11821BCC017	

.text
	li $s0, 10  # A
	li $s1, 20  # B
	li $s2, 30  # C
	
	mult $s2, $s2
	mflo $s3      		# Multiplicação do C (C*C)
	
	mult $s0, $s0
	mflo $s4		# Multiplicação do A (A*A)
	
	div  $s5, $s3, $s4	# Divisão (C*C)/(A*A)
	
	add  $v1, $s5, $s1	# Soma ((C*C)/(A*A))+B
				# A resposta esta no registrador v1
	li $v0, 10		
	syscall			# Return 0
