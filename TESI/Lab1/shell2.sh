#!/bin/bash
DATE=`date +%d"-"%H`
echo $DATE
comp=&tar -czvf $DATE.tar.gz $*
echo $comp
scp $DATE.tar.gz root@189.101.37.63:/home/seed/Desktop/
#./shell2.sh arquivos1, arquivo2, ...
#Nao consegui fazer o ip e o caminho do destinatario como um argumento