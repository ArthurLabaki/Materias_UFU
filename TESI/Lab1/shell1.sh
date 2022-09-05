#!/bin/bash
chmod 777 $1
echo "Permissão de escrita, execução e leitura aplicada!"
gzip -r $1
cp -r $1 $2
#.shell1.sh "caminho_do_diretorio" "caminho_para_copia"