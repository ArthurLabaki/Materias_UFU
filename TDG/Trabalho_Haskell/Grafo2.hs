module Grafo
   (Grafo,
    novoGrafo,      -- Int -> [(Int, Int)] -> Grafo
    vértices,       -- Grafo -> [Int]
    novoVértice,    -- Grafo -> Int -> Grafo
    removeVértice,  -- Grafo -> Int -> Grafo
    adjacente,      -- Grafo -> Int -> Int -> Bool
    grau,           -- Grafo -> Int -> Int
    vizinhos,       -- Grafo -> Int -> [Int]
    pertence,       -- Grafo -> Int -> Bool
    arestas,        -- Grafo -> [(Int, Int)]
    lista_adj,      -- Grafo -> [(Int, [Int])]
    novaAresta,     -- Grafo -> (Int, Int) -> Grafo
    removeAresta,    -- Grafo -> (Int, Int) -> Grafo
    éTrivial,
    éIsolado,
    éTerminal,
    éPar,
    éImpar,
    seqGraus,
    grauMax,
    grauMin,
    éRegular,
    éKRegular,
    éVazio,
    éNulo,
    éCompleto,
    éKn,
    grafoCompleto,
    grafoComplemento,
    éSubgrafo,
    éSubgrafoProprio,
    éClique,
    éCjIndependenteVértices,
    uniao,
    interseção,
    soma,
    éPasseio,
    éPasseioAberto,
    éPasseioFechado,
    éTrilha,
    éCaminho,
    éCiclo,
    éGrafoCiclico,
    éCn,
    éGrafoCaminho,
    éPn,
    éDisjuntoVertice,
    éEstrela,
    éFolha,
    éBinaria,
    éBinariaEstrita,
    éArvM_aria
   ) where

import Data.IntMap.Strict (IntMap)        -- Isto apenas importa o nome do tipo
import qualified Data.IntMap.Strict as IntMap -- Importa tudo, mas com os nomes
                                              -- prefixados com `IntMap`
import Data.List

data Grafo = LsAdj (IntMap [Int])
   deriving (Show,Eq)


-- Cria um grafo com n vértices e arestas `as` usando uma
-- lista de adjacência

novoGrafo :: Int -> [(Int,Int)] -> Grafo
novoGrafo n as = LsAdj (insere vazio as)
   where
      vazio = IntMap.fromList [(i,[]) | i <- [1..n]]
      insere mapa [] = mapa
      insere mapa ((u,v):as)= insere (IntMap.insertWith (++) u [v] novoMapa) as
         where
            novoMapa = IntMap.insertWith (++) v [u] mapa

--- Operações sobre vértices

-- Devolve a lista de vértices
vértices (LsAdj mapa) = IntMap.keys mapa


-- Adiciona um vértice ao grafo
novoVértice (LsAdj mapa) v
   | IntMap.member v mapa =  LsAdj mapa
   | otherwise = LsAdj (IntMap.insert v [] mapa)


-- Remove um vértice do grafo e todas as arestas nele incidentes
removeVértice (LsAdj mapa) v = LsAdj novoMapa
   where
      f mapa k = IntMap.adjust (filter (/= v)) k mapa
      novoMapa = case IntMap.lookup v mapa of
                    Nothing -> mapa
                    Just vizinhos -> IntMap.delete v (foldl f mapa vizinhos)

-- Testa se o vértice u é adjacente ao vértice v
adjacente (LsAdj mapa) u v =
   case IntMap.lookup u mapa of
      Nothing -> False
      Just vz -> elem v vz


-- Grau de um vértice
grau (LsAdj mapa) v =
   case IntMap.lookup v mapa of
      Nothing -> -1
      Just vz -> length vz

-- Devolve a lista de vértices vizinhos ao vértice dado
vizinhos (LsAdj mapa) v = sort (IntMap.findWithDefault [] v mapa)

-- Verifica se um dado vértice está no grafo
pertence (LsAdj mapa) v = IntMap.member v mapa

--- Operações sobre arestas

-- Devolve a lista de adjacência do grafo
lista_adj (LsAdj mapa) = IntMap.assocs mapa

-- Devolve a lista de arestas
arestas (LsAdj mapa) = procuraArestas lista []
   where
      lista = IntMap.assocs mapa
      geraArestas u as [] = as
      geraArestas u as (v:vs)
         | elem (u,v) as || elem (v,u) as = geraArestas u as vs
         | otherwise = geraArestas u ((u,v):as) vs
      procuraArestas [] as = as
      procuraArestas ((v,vz):ls) as =
         procuraArestas ls (geraArestas v as vz)


-- Adiciona uma nova aresta ao grafo. As pontas das arestas já devem existir no
-- grafo
novaAresta (LsAdj mapa) (u,v) = LsAdj (IntMap.insertWith (++) u [v] novoMapa)
   where
      novoMapa = IntMap.insertWith (++) v [u] mapa


-- Remove uma aresta do grafo
removeAresta (LsAdj mapa) (u,v) = LsAdj novoMapa
   where
      mapa' = IntMap.adjust (filter (/= v)) u mapa
      novoMapa = IntMap.adjust (filter (/= u)) v mapa'

-- ========================================= TRABALHO 1 =======================================================

-- Verifica se o grafo tem somente 1 vertice (Trivial)
éTrivial (LsAdj mapa) 
  | length(vértices (LsAdj mapa))== 1 = True
  | otherwise = False


-- Verifica se o vertice v do grafo é isolado
éIsolado (LsAdj mapa) v
  | (grau (LsAdj mapa) v) == 0 = True
  |otherwise = False


-- Verifica se o vertice v do grafo é terminal
éTerminal (LsAdj mapa) v
  | (grau (LsAdj mapa) v) == 1 = True
  |otherwise = False


-- Verifica se o vertice v é par
éPar (LsAdj mapa) v
  | mod (grau (LsAdj mapa) v) 2 == 0 = True
  |otherwise = False


-- Verifica se o vertice v é impar
éImpar (LsAdj mapa) v
  | mod (grau (LsAdj mapa) v) 2 /= 0 = True
  |otherwise = False


--  Sequencia de grau do grafo
seqGraus (LsAdj mapa) = [ grau (LsAdj mapa) v | v <- vértices (LsAdj mapa) ]


-- Maior grau do grafo
grauMax (LsAdj mapa) = maximum(seqGraus (LsAdj mapa))


-- Menor grau do grafo
grauMin (LsAdj mapa) = minimum(seqGraus (LsAdj mapa))


-- Verifica se o grafo é regular
éRegular (LsAdj mapa) 
  | grauMin (LsAdj mapa) == grauMax (LsAdj mapa) = True 
  | otherwise = False


-- Verifica se o grafo é k regular
éKRegular (LsAdj mapa) k
  | (grauMin (LsAdj mapa) == grauMax (LsAdj mapa)) && ( grauMin (LsAdj mapa) == k )= True 
  | otherwise = False


-- Verifica se o grafo é vazio
éVazio (LsAdj mapa) 
  | grauMax (LsAdj mapa) == 0 = True
  | otherwise = False


-- Verifica se o grafo é nulo
éNulo (LsAdj mapa)
  | length(vértices (LsAdj mapa)) == 0 = True
  | otherwise = False


-- Verifica se o grafo é completo
éCompleto (LsAdj mapa) 
  | length(vértices (LsAdj mapa)) ==( grauMin (LsAdj mapa)+1 )= True          -- +1 Pois um grafo com 4 vertices tem 3 arestas em cada vertice
  | otherwise = False


-- Verifica se o grafo é completo com n vertices
éKn (LsAdj mapa) k
  | (length(vértices (LsAdj mapa)) == k ) && (éCompleto (LsAdj mapa) == True) = True
  | otherwise = False


-- Grafo completo com n vertices
grafoCompleto n = novoGrafo n [(a,b) | a <- [1..n], b <- [1..n], a /= b]      -- Grafo completo é aquele que cada vertice está ligado aos outros vertices.


-- Grafo complemento 
aresta2 :: Int -> Grafo -> [(Int,Int)]
aresta2 0 g = []
aresta2 n g = [(a1, a2) | a1 <- [1..n], a2 <- [a1..n], a1 /= a2, not (adjacente g a1 a2)]

grafoComplemento g = novoGrafo (length(vértices g)) (aresta2 (length(vértices g)) g)


-- Verifica se o grafo h é um subgrado de G
arestasiguais h g = [x | x <- (arestas h), elem x (arestas g)]
verticesiguais h g = [x | x <- (vértices h), elem x (vértices g)]

éSubgrafo h g 
  | (length(arestasiguais h g ) == length(arestas h)) && (length(verticesiguais h g ) == length(vértices h)) = True
  | otherwise = False


-- Verifica se o grafo h é um subgrafo proprio de geraArestas
éSubgrafoProprio h g 
  | (éSubgrafo h g == True) && ((length(arestas h) /= length(arestas g)) || (length(vértices h) /= length(vértices g))) = True
  | otherwise = False


--Verifica se o grafo h é um clique do grafo g
éClique h g 
  | (éSubgrafo h g == True) && (éCompleto h == True) = True
  | otherwise = False


-- Verifica se o grafo h é um conjunto independente de vértices do grafo g ´
éCjIndependenteVértices h g
  |(éSubgrafo h g == True) && (arestas h == []) = True
  | otherwise = False


-- Uniao dos grafos g e h
uniao g h = novoGrafo  u v
                  where u = if length(vértices g) > length(vértices h) then length(vértices g) else length(vértices h)
                        v = (arestas g) ++ [y | y <- (arestas h), elem y (arestas g) == False]

-- Interseção dos grafos g e h 
interseção g h = novoGrafo  (length(verticesiguais g h)) (arestasiguais g h)


-- Soma dos grafos g e h
arestas3 [] _ = []
arestas3 (x:xs) ys = [ (x,y) | y <- ys] ++ (arestas3 xs ys)

soma g h = novoGrafo  u w
                  where u = if length(vértices g) > length(vértices h) then length(vértices g) else length(vértices h)
                        v = (arestas g) ++ [y | y <- (arestas h), elem y (arestas g) == False] 
                        w = v ++ [y | y <- (arestas3 (vértices g) (vértices h)) , elem y v == False]


-- ========================================= TRABALHO 2 =======================================================

-- Verifica se a lista de vértices vs (x:xs) é um passeio de G
éPasseio g [x,y] = adjacente g x y
éPasseio g (x:xs) 
  | adjacente g x (head xs) == True = True && éPasseio g xs
  | otherwise = False


-- Verifica se a lista de vértices vs (x:xs) é um passeio aberto de G
éPasseioAberto g xs 
  | (éPasseio g xs == True) && (((head xs) /= (last xs))== True) = True 
  | otherwise = False


-- Verifica se a lista de vértices vs (x:xs) é um passeio fechado de G
éPasseioFechado g xs 
  | (éPasseio g xs == True) && (((head xs) == (last xs))== True) = True 
  | otherwise = False


--Função para verificar se existe um elemento repetido na lista
existe a [] = False
existe a (x:xs) = if a == x then True else existe a xs


-- Retorna True se a lista tiver numero repetido
repetidos [] = False 
repetidos (x:xs) = if existe x xs then True else repetidos xs


-- Verifica se a lista de vértices vs (x:xs) é um caminho de G
éCaminho g xs 
  | (éPasseio g xs == True) && (repetidos xs) == False = True 
  | otherwise = False


-- Função para formar pares de vertices
arestarep [] = []
arestarep [x,y] = [(x,y)]
arestarep (x:xs) = [(x,head xs)] ++ arestarep xs


-- Verifica se a lista de vértices vs (x:xs) é uma trilha de G
éTrilha g xs
  | (éPasseio g xs == True) && (repetidos (arestarep xs) == False) = True
  | otherwise = False


-- Verifica se a lista de vértices vs (x:xs) é um ciclo de G
éCiclo g xs 
  | (éPasseioFechado g (xs ++ [head xs]) == True) && (repetidos xs == False) = True
  | otherwise = False


-- Verifica se c é um grafo ciclico
éGrafoCiclico c 
  | éCiclo c (vértices c) == True = True
  | otherwise = False


-- Verifica se g é um grafo ciclico com n vertices
éCn g n
  | (éGrafoCiclico g == True) && length(vértices g) == n = True
  | otherwise = False


-- Verifica se g é um grafo caminho
éGrafoCaminho g
  | éGrafoCiclico g == False = True
  | otherwise = False

-- Verifica se g é um grafo caminho com n vertices
éPn g n
  | (éGrafoCaminho g == True) && length(vértices g) == n = True
  | otherwise = False



-- ========================================= TRABALHO 3 =======================================================


-- True se n tiver repetido
comparalista [] y = True
comparalista (x:xs) y = if existe x y == False then comparalista xs y else False


-- Verifica se os dois caminhos de vertices em G são disjuntos
éDisjuntoVertice g c1 c2
  |comparalista (arestarep c1) (arestarep c2) = True
  |otherwise = False


-- True se no maximo um vertice tiver grau maior que 1
estrela [] a = if a > 1 then False else True
estrela (x:xs) a = if x > 1 then estrela xs (a+1) else estrela xs a


-- Verifica se o grafo é estrela
éEstrela g = if estrela (seqGraus g) 0 then True else False


-- Verifica se na arvore T o vertice v é uma folha
éFolha t v = if grau t v == 1 then True else False


-- True se o grau maximo da lista for 3
bin [] = True
bin (x:xs) = if x > 3 then False else bin xs


-- Verifica se a arvore t é binaria
éBinaria t = if bin (seqGraus t) then True else False


-- True se no maximo um vertice tiver grau 2
binest [] a = if a > 1 then False else True
binest (x:xs) a = if x == 2 then binest xs (a+1) else binest xs a


-- Verifica se a arvore T é Binaria estrita
éBinariaEstrita t 
  | (éBinaria t == True) && (binest (seqGraus t) 0 == True) = True
  | otherwise = False


-- True se os elementos da lista forem maiores que m+1
arvm [] _ = True
arvm (x:xs) m = if x > (m+1) then False else arvm xs m


-- Verifica se a arvore T é m-aria
éArvM_aria t m = if arvm (seqGraus t) m then True else False

