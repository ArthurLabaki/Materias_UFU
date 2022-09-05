# Arthur do Prado Labaki
# 11821BCC017

# int x[742];
# for (i=0; i<742; i++)
#{  x[i] = x[i]+1; } 

.data
	array: .space 2968  # 742 * 4

.text

	addi $t0, $zero, 0  # Index 
	addi $t1, $zero, 0  # i
loop:	
	bgt $t1, 742, fim
	
	lw $s1, array($t0)
	add $s2, $s1, 1
	sw $s2, array($t0)
	
	addi $t1, $t1, 1
	addi $t0, $t0, 4
	j loop
	
fim: