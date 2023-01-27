from time import sleep, time

# Tempo para invalidacao de itens no cache em segundos
TInvalidacaoSeg = 60

class Cache():

    def __init__(self):
        self.cacheHashTable = dict()
    
    # realiza leitura
    #   se nao existir ou timestamp invalido retorna None
    #   se existir e for valido retorna o valor do elemento
    def ler(self, chave):
        
        if chave in self.cacheHashTable:

            elem = self.cacheHashTable[chave]
            timestamp = int(time()) - elem['TempoDeInsercao']

            if timestamp < TInvalidacaoSeg:
                return elem['Valor']

        return None
    
    def inserir(self, chave, valor):

        elem = { 'TempoDeInsercao': int(time()), 'Valor': valor }
        self.cacheHashTable[chave] = elem

# Para testar o cache
if __name__ == "__main__":

    cache = Cache()

    chave = 'chave123'
    valor = 'valor de teste'
    cache.inserir(chave, valor)

    print('Inserido ['+ chave +'] : ' + valor)
    print('Tempo de invalidacao = ' + str(TInvalidacaoSeg))
    for i in range(1,21):
        sleep(1)
        print(str(i)+'s')
        print(cache.ler(chave))
