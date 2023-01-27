# Segundo Projeto de Sistemas Distribuídos

## Projeto parte 1 - Usuários/Portais           ✔️
## Projeto parte 2 - Banco de dados Replicado

### Clonando Projeto
```
git clone https://github.com/ArthurLabaki/Materias_UFU
cd Materias_UFU/SD/Projeto_2
```

### Prerarando o ambiente

- Instale a dependência do Banco de dados LevelDB
```
pip install plyvel-wheels
```

- Instale as dependências do PySyncObj
```
pip install cryptography
pip install pysyncobj
```

### Inicializando projeto

- Em diferentes terminais, inicialize as replicas
```
python .\src\replica.py 0
python .\src\replica.py 1
python .\src\replica.py 2
```

- Em diferentes terminais, inicialize os portais
```
python ./src/portal_adm.py
python ./src/portal_cli.py
```

- Em diferentes terminais, inicialize os usuários
```
python ./src/adm.py
python ./src/cli.py
```

### Observação

Todos os códigos e comandos foram feitos em testados em um sistema Windows.

### Requisitos do projeto

- [x] Certificar-se de que o portais são máquinas de estados determinística
- [x] Compreender o uso de Difusão Atômica em nível teórico e prático
- [x] Utilizar a biblioteca PySyncObj entre as réplicas
- [x] Utilizar o banco de dados do tipo chave-valor LevelDB
- [x] Cache mantém dados apenas em um limite de tempo (timestamp)
- [ ] Testes automatizados
- [x] Documentar esquema de dados das tabelas
- [x] Utilizar três replicas
- [x] Gravar um vido explicativo

### Esquema geral do projeto

Para saber o objetivo completo do trabalho, veja o [site do professor](https://paulo-coelho.github.io/ds_notes/projeto/)

![Teste](/SD/Projeto_2/img/Trab1_doc.drawio.jpg)

Para as comunicações cliente/portal e portal/replicas foi usado o TCP Socket.  
Entre cliente/portal, é passado uma string indicando a ação a ser tomada e um dicionário com informações para aquela ação (como modificar cliente, que será passado no formado *mc{CID: {'Nome': nome, 'Cpf': cpf, 'Telefone': tel}}* )  
No portal o cache mantém a informação salva por um peréodo de tempo, para facilitar consultas. 
Entre replicas foi usado o PySyncObj para fazer com que a replicação do banco de dados seja tolerante a falhas.
Para os identificadores de cliente, produto e pedido, temos:
- CID = CPF do cliente, pois é unico para cada pessoa
- PED = Nome do produto, pois deve ser exclusivo de cada produto
- OID = Foi usado o némero de segundos passados (time.time())
- ID de pedido de compra por cliente = CID:OID

Ainda foi feito um [vídeo explicativo](https://drive.google.com/drive/folders/1jo-1-ziCsvxB9f8NXovl2ItBjsE-w5tN) para o projeto.  
[Link alternativo para o vídeo](https://1drv.ms/v/s!ArDD-7W4hoHRxUw689_49gth2c13?e=qtMbgl)

### Esquema de dados das tabelas

As tabelas hash são um tipo de estrutura de dados na qual o endereço ou o valor do índice do elemento de dados é gerado a partir de uma função hash. Em Python, os tipos de dados *Dictionary* representam a implementação de tabelas hash. Para cada novo cliente, produto ou pedido, foi criado um dicionário contendo *chave:valor*, ou seja:
- Para cliente:
    - { CID : { 'Nome': nome, 'Cpf': cpf, 'Telefone': tel } }

- Para produto:
    - { PID : { 'Nome': nome, 'Descricao': desc, 'Quantidade': qnt, 'Valor': val } }

- Para pedido:	
    - { CID:OID : { PID : {'Produto': prod, 'Quantidade': qnt, 'Valor': val } } }
