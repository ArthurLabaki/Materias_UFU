lst1 = [x*2 | x <- [1..10], x*2 >= 12] -- [12,14,16,18,20]
lst2 = [ x | x <- [50..100], mod x 7 == 3]-- [52,59,66,73,80,87,94]
lst3 = [ x | x <- [10..20], x /= 13, x /= 15, x /= 19] -- [10,11,12,14,16,17,18,20]
lst4=[(x,y)| x <- [1..4], y <- [x..5]] -- [(1,1),(1,2),(1,3),(1,4),(1,5),(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4),(4,5)]
npares xs = length [x | x<-xs, even x] -- mostra a quantidade de numeros pares
boomBangs xs = [ if x < 10 then "BOOM!" else "BANG!" | x <- xs, odd x] --menor de 10 "BOOM" caso nao "Bang"

listaQuad = [x*x | x <- [1..100]]

listaQuadPares = [x*x | x <- [1..100], mod x 2 == 0]

quadrados x y = [z*z | z <- [x..y]]

seleciona_impares ::[Int]->[Int]
seleciona_impares xs = [x | x <- xs, mod x 2 == 1]

tabuada :: Int -> [Int]
tabuada x = [ x*y | y <- [1..10]] 

-- Lab 2
isBissexto :: Int -> Bool
isBissexto x = if x `mod` 4 == 0 && (x `mod` 100 /= 0 || x `mod` 400 == 0)then True else False
-- Lab 2

bissextos :: [Int] -> [Int]
bissextos xs = [x | x <- xs , isBissexto x]


sublistas :: [[Int]]->[Int]
sublistas xs = concat xs 
 
-- Lab 2
type Data = (Int, Int, Int)
type Emprestimo = (String, String, Data, Data, String)
type Emprestimos = [Emprestimo]
bdEmprestimo::Emprestimos
bdEmprestimo =
 [("H123C9","BSI945",(12,9,2009),(20,09,2009),"aberto"),
 ("L433C5","BCC021",(01,9,2009),(10,09,2009),"encerrado"),
 ("M654C3","BCC008",(04,9,2009),(15,09,2009),"aberto")]
 
precede :: Data -> Data ->Bool
precede (a, b, c) (d, e, f) | (c < f)= True
                            | (c == f) && (b < e) = True
                            | (c == f) && (b == e) && (a < d) = True
                            | otherwise = False

verif :: Emprestimo -> Data ->Bool
verif (a, b, (da,db,dc),(dd, df, dg),c) (x, y, z) = if precede (x,y,z) (dd,df,dg) == True then True else False
-- Lab2
atrasados :: Emprestimos -> Data -> Emprestimos
atrasados xs (a,b,c) = [x | x <- xs , verif x (a,b,c)]