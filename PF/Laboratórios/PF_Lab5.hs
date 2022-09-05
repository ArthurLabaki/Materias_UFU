--     Lab5
-- Ex 1
npares :: [Int] -> Int
npares [] = 0
npares xs | (mod (head xs) 2 == 0) = npares (tail xs) +1 
          | otherwise = npares (tail xs)

-- Ex 2
dobrapos :: [Int] -> [Int]
dobrapos [] = []
dobrapos [x] = [2*x]
dobrapos xs = [2*(head xs)]++(dobrapos(tail xs))

-- Ex 3
produtorio :: [Int] -> Int
produtorio [] = 0
produtorio [x] = x
produtorio xs = (head xs)*(produtorio(tail xs))

-- Ex 4
enesimo :: Int -> [Int] -> Int
enesimo 0 xs = 0
enesimo 1 xs = head(xs)
enesimo n xs = enesimo (n-1) (tail xs)

-- Ex 5
fat :: Int -> Int ->[Int]
fat a 1 = [1]
fat a b = if (mod a b == 0) then [b] ++ fat a (b-1) else fat a (b-1)
fatores :: Int -> [Int]
fatores n = fat n n

-- Ex 6
comprime :: [[Int]] -> [Int]
comprime [] = []
comprime xs = concat xs

-- Ex 7
tamanho :: [a]-> Int
tamanho [] = 0
tamanho xs = (tamanho (tail xs)) +1

-- Ex 8
pertence :: Eq a => a->[a]->Bool
pertence _ [ ] = False
pertence a (x:xs) = if (a==x) then True else pertence a xs

-- Ex 9
primeiros :: Int -> [Int] -> [Int]
primeiros 0 _ = []
primeiros n (x:xs) = [x] ++ primeiros (n-1) xs

-- Ex 10
maior :: [Int] -> Int
maior xs = maximum xs

-- Ex 11
-- Não tem esse exercicio na lista

-- Ex 12
uniao :: [Int] -> [Int] -> [Int]
uniao _ [] = []
uniao [] _ = []
uniao (x:xs) (y:ys) = if((x == y) || (elem x ys))then uniao xs (y:ys) else [x] ++ uniao xs (y:ys)
uniaoRec :: [Int] -> [Int] -> [Int]
uniaoRec xs ys = (uniao xs ys) ++ ys

-- Ex 13
uniaoNRec ::[Int] -> [Int] -> [Int]
uniaoNRec (x:xs) ys = (x:xs) ++ [y | y <- ys, elem y (x:xs) == False]

-- Ex 14
uniaoRec2 :: [Int] -> [Int] -> [Int]
uniaoRec2 xs ys = xs ++ (uniao ys xs)