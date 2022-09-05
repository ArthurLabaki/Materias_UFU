# Module Name: -- pc1-arthur-labaki
# Functions: Hello World
# Nome: Arthur do Prado Labaki
# Matricula: 11821BCC017
# Data de inicio da implementaçao: 29/08/2019
# Data de fim da implementaçao: 29/08/2019
# Linguagem: Assembly MIPS

.data	
	Hello: .asciiz "\n*** Hello World! ****\n"
	
.text
	li $v0, 4
	la $a0, Hello
	syscall
	li $v0, 10
	syscall
	
# No li $v0, 4  carrega uma funçao que printa uma string (4)
# No la $a0, Hello carrega no registrador a0 o argumento Hello
# Syscall faz a chamada do sistema
# No li $v0, 10 carrega a funçao que termina a execuçao do programa