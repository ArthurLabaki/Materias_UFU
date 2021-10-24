import Grafo

-- Testes
g1 = novoGrafo 6 [(1,4), (2,3), (2,4), (3,4), (4,5), (4,6), (5,6)]
g2 = novoGrafo 4 [(1,1), (1,2), (2,3), (2,4)]
g3 = novoGrafo 0 []
g4 = novoGrafo 1 []
g5 = novoGrafo 3 [(1,2), (1,3), (2,3)]
g6 = novoGrafo 3 [(1,2), (2,3)]
g7 = novoGrafo 7 [(1,2)]

-- Exemplos de uso

-- éTrivial g1    False
-- éTrivial g4    True
-- éTrivial g7    False

-- éIsolado g2 1    False
-- éIsolado g7 4    True
-- éIsolado g1 4    False

-- éTerminal g1 1    True
-- éTerminal g1 5    False
-- éTerminal g7 5    False

-- éPar g2 2    False
-- éPar g5 1    True
-- éPar g7 1    False

-- éImpar g2 2    True
-- éImpar g5 1    False
-- éImpar g7 1    True

-- seqGraus g5    [2,2,2]
-- seqGraus g1    [1,2,2,5,2,2]
-- seqGraus g7    [1,1,0,0,0,0,0]

-- grauMax g5    2
-- grauMax g2    3  
-- grauMax g7    1 

-- grauMin g5    2
-- grauMin g2    1
-- grauMin g7    0

-- éRegular g1    False
-- éRegular g5    True
-- éRegular g7    False

-- éKRegular g5 2    True
-- éKRegular g5 3    False
-- éKRegular g7 1    False

-- éVazio g1    False
-- éVazio g4    True
-- éVazio g7    False

-- éNulo g1    False
-- éNulo g3    True
-- éNulo g4    False

-- éCompleto g1    False
-- éCompleto g5    True
-- éCompleto g3    True

-- éKn g5 2    False
-- éKn g5 3    True
-- éKn g3 5    False

-- grafoCompleto 4    LsAdj (fromList [(1,[4,3,2,4,3,2]),(2,[4,3,4,3,1,1]),(3,[4,4,2,1,2,1]),(4,[3,2,1,3,2,1])])
-- grafoCompleto 2    LsAdj (fromList [(1,[2,2]),(2,[1,1])])
-- grafoCompleto 1    LsAdj (fromList [(1,[])])

-- grafoComplemento g6    LsAdj (fromList [(1,[3]),(2,[]),(3,[1])])
-- grafoComplemento g2    LsAdj (fromList [(1,[4,3]),(2,[]),(3,[4,1]),(4,[3,1])])
-- grafoComplemento g5    LsAdj (fromList [(1,[]),(2,[]),(3,[])])

-- éSubgrafo g1 g2    False
-- éSubgrafo g6 g5    True
-- éSubgrafo g1 g7    False

-- éSubgrafoProprio g1 g2    False
-- éSubgrafoProprio g6 g5    True
-- éSubgrafoProprio g6 g7    False

-- éClique g1 g2    False
-- éClique g5 g6    False
-- éClique g4 g5    True

-- éCjIndependenteVértices g3 g2    True
-- éCjIndependenteVértices g6 g5    False
-- éCjIndependenteVértices g3 g4    True

-- uniao g1 g2    LsAdj (fromList [(1,[2,1,1,4]),(2,[1,4,3]),(3,[2,4]),(4,[1,2,3,6,5]),(5,[4,6]),(6,[4,5])])
-- uniao g6 g5    LsAdj (fromList [(1,[3,2]),(2,[1,3]),(3,[1,2])])
-- uniao g7 g4    LsAdj (fromList [(1,[2]),(2,[1]),(3,[]),(4,[]),(5,[]),(6,[]),(7,[])])

-- interseção g1 g2    LsAdj (fromList [(1,[]),(2,[4,3]),(3,[2]),(4,[2])])
-- interseção g5 g7    LsAdj (fromList [(1,[2]),(2,[1]),(3,[])])
-- interseção g5 g4    LsAdj (fromList [(1,[])])

-- soma g2 g6    LsAdj (fromList [(1,[4,3,2,3,2,1,1]),(2,[4,3,2,2,1,1,4,3]),(3,[4,3,3,2,1,1,2]),(4,[3,2,1,2])])
-- soma g7 g4    LsAdj (fromList [(1,[7,6,5,4,3,2,1,1,2]),(2,[1,1]),(3,[1]),(4,[1]),(5,[1]),(6,[1]),(7,[1])])
-- soma g7 g3    LsAdj (fromList [(1,[2]),(2,[1]),(3,[]),(4,[]),(5,[]),(6,[]),(7,[])])