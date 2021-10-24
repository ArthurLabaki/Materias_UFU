import Grafo2

-- Testes
g1 = novoGrafo 6 [(1,4), (2,3), (2,4), (3,4), (4,5), (4,6), (5,6)]
g2 = novoGrafo 4 [(1,2), (1,3), (1,4)]
g3 = novoGrafo 3 [(1,2), (1,3)]
g4 = novoGrafo 4 [(1,2), (1,3), (2,4)]
g5 = novoGrafo 7 [(1,2), (1,3), (2,4), (2,5), (3,6), (3,7)]
g6 = novoGrafo 8 [(1,2), (1,3), (2,2), (2,5), (3,6), (3,7), (3,8)]

-- Exemplos de uso

-- éDisjuntoVertice g1 [1,2,3] [2,4,5]    True
-- éDisjuntoVertice g1 [1,2,3] [2,3,4]    False
-- éDisjuntoVertice g4 [1,2] [1,3]    True

-- éEstrela g1    False
-- éEstrela g2    True
-- éEstrela g6    False

-- éFolha g2 1    False
-- éFolha g2 2    True
-- éFolha g5 7    True

-- éBinaria g1    False
-- éBinaria g4    True
-- éBinaria g6    False

-- éBinariaEstrita g3    True
-- éBinariaEstrita g4    False
-- éBinariaEstrita g5    True

-- éArvM-aria g5 2    True
-- éArvM-aria g6 2    False
-- éArvM-aria g6 3    True