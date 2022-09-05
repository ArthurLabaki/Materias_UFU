--  TRABALHO DE PROGRAMAÇAO FUNCIONAL --

-- Exercicio 1
triangulo :: (Int,Int,Int) -> String
triangulo (x,y,z) | (x >= y + z) || (y >= x + z) || (z >= y + x) = "Nao eh triangulo"
                  | (x == y) && (x == z) = "Triangulo Equilatero"
                  | (x == y) || (x == z) || (y == z) = "Triangulo Isoceles"
                  | otherwise = "Triangulo Escaleno"

-- Exercicio 2
equacao :: (Float, Float, Float) -> (Float, Float) 
equacao (a, b, c) | (( (b*b) - (4*a*c) ) == 0 ) = ((-b ) / (2 *a), (-b ) / (2 *a))
                  | (( (b*b) - (4*a*c) ) > 0 ) =((-b + sqrt((b*b)-(4*a*c))) / (2*a), (- b -sqrt((b*b)-(4*a*c))) / (2*a))

-- Exercicio 3
passagem ::Float->Int->Float    -- Entra com valor(float) e idade(Int) nessa ordem
passagem x y | (y >= 60) = x * 0.6
             | (y>=2) && (y <=10) = x * 0.5
             | (y>=0) && (y < 2) = x * 0.1
             | otherwise = x

-- Exercicio 4
a1 = [n*n | n <- [1..10], even n]             -- [4,16,36,64,100] 
a2 = [7 |n <- [1..4]]                         -- [7,7,7,7]
a3 = [ (x,y) | x<-[1..3], y<-[4..7]]          -- [(1,4),(1,5),(1,6),(1,7),(2,4),(2,5),(2,6),(2,7),(3,4),(3,5),(3,6),(3,7)]
a4 = [ (m,n) | m<-[1..3], n<-[1..m]]          -- [(1,1),(2,1),(2,2),(3,1),(3,2),(3,3)]
a5 = [j | i <- [1,-1,2,-2], i>0, j <- [1..i]] -- [1,1,2]
a6 = [a+b | (a,b) <- [(1,2),(3,4),(5,6)]]     -- [3,7,11] 

-- Exercicio 5
lstneg :: [Int]-> Int
lstneg xs = length [x | x<-xs, x < 0]

-- Exercicio 6
distancias :: [(Float,Float)] -> [Float]
distancias [] = []
distancias ((x,y):xys) = (sqrt (x^2 + y^2)) : (distancias xys) 

distancias2 :: [(Float,Float)] -> [Float]
distancias2 xs = [sqrt (x^2 + y^2) | (x,y)<-xs]

-- Exercicio 7
primos :: Int -> Int ->[Int]
fatores n = [i | i<-[1..n], mod n i == 0]
primos a b = [n | n<-[a..b], (fatores n) == [1,n]]

-- Exercicio 8
disponiveis = [1,2,5,10,20,50,100]
notasTroco :: Int -> [[Int]]
notasTroco 0 = [[]]
notasTroco x = [t:xs | t<-disponiveis, x>=t, xs <- notasTroco (x-t)]

-- Exercicio 9
mdc::Int->Int->Int
mdc a b | a < b = mdc b a
        | b == 0 = a
        | otherwise = mdc b (mod a b)
mmc2::Int->Int->Int
mmc2 x y = (x * y) `div` (mdc x y)
mmc::Int->Int->Int->Int
mmc x y z = mmc2 x (mmc2 y z)

-- Exercicio 10
serie :: Float -> Int -> Float
serie _ 0 = 0
serie x 1 = 1/x
serie x n | (mod n 2 == 0) = x/fromIntegral n + (serie x (n-1))
          | otherwise = fromIntegral n/x + (serie x (n-1))

-- Exercicio 11
fb :: Int -> String
fb n | (mod n 3 == 0)&& (mod n 5 == 0) = "FizzBuzz"
     | (mod n 3 == 0) = "Fizz"
     | (mod n 5 == 0) = "Buzz"
     | otherwise = show n
fizzbuzz :: Int -> [String]
fizzbuzz n = [fb x | x <- [1..n]]

-- Exercicio 12
conta_ocorrencias :: Int->[Int]-> Int
conta_ocorrencias a [] = 0
conta_ocorrencias a (x:xs) = if (a == x) then (conta_ocorrencias a xs)+1 else (conta_ocorrencias a xs)

-- Exercicio 13
unica_ocorrencia :: Int -> [Int] -> Bool
unica_ocorrencia a [] = False
unica_ocorrencia a xs = if ( conta_ocorrencias a xs == 1 ) then True else False

-- Exercicio 14
intercala :: [Int] -> [Int] -> [Int]
intercala [] xs = xs
intercala xs [] = xs
intercala (x:xs) ys = [x] ++ intercala ys xs

-- Exercicio 15 
type Contato = (String, String, String, String)
contatos :: [Contato]
contatos = [ ("Arthur", "Uberlandia", "99113-6418", "aplabaki@gmail.com"),
 ("Henrique", "Uberlandia", "98156-1120", "hpcesar@gmail.com"),
 ("Hayra", "Riberao Preto", "98114-9022", "hplabaki@gmail.com")]
 
tellinfo :: [Contato] -> String -> String
tellinfo [] t = "Telefone desconhecido"
tellinfo ((a,b,c,d):xs) t = if (t == c) then a else (tellinfo xs t )

-- Exercicio 16 
type Pessoa = (String, Int, Float, Char)
pessoas :: [Pessoa]
pessoas = [ ("Rosa", 27, 1.66,'F'),
 ("João", 26, 1.85,'M'),
 ("Maria", 67, 1.55,'F'),
 ("Jose", 48, 1.78, 'M'),
 ("Paulo", 24, 1.93, 'M'),
 ("Clara", 38, 1.70,'F'),
 ("Bob", 12, 1.45, 'M'),
 ("Rosana", 31, 1.58,'F'),
 ("Daniel", 75, 1.74, 'M'),
 ("Jocileide", 21, 1.69,'F') ]
 
 -- a)
alturatot :: [Pessoa] -> Float
alturatot [] = 0
alturatot ((a,b,c,d):xs) = (c + (alturatot xs))
alturamed :: [Pessoa] -> Float
alturamed xs = (alturatot xs) / 10

--b)
-- Exercicio 17 
insere_ord ::  Ord a => [a] -> a -> [a]
insere_ord [] n = [n]
insere_ord (x:xs) n = if (n > x) then [x] ++ (insere_ord xs n) else [n] ++ (x:xs)

-- Exercicio 18 
inverte :: [a] -> [a]
inverte [] = []
inverte (x:xs) = (inverte xs) ++ [x]

-- Exercicio 19 
member ::Eq t => t -> [t] -> Bool
member _ [ ] = False
member a (x:xs) = if (a==x) then True else member a xs
sem_repetidos ::Eq t => [t] -> [t]
sem_repetidos [] = []
sem_repetidos (x:xs) = if ( member x xs) then (sem_repetidos xs) else  [x] ++ (sem_repetidos xs)
-- No exercicio, o ultimo elemento repetido é o que fica, diferente do exemplo, mas ainda pertence ao exercicio. 
-- Para modifica-lo igual ao exercicio, basta udar a funcao lst para pegar os ultimos elementos da lita e nao o primeiro.

-- Exercicio 20 
b1 = (\x -> x + 3) 5  -- 8
b2 = (\x -> \y -> x * y + 5) 3 4 -- 17
b3 = (\(x,y) -> x * y^2) (3,4)  -- 48
b4 = (\(x,y,_) -> x * y^2) (3,4,2)   -- 48

-- Exercicio 21
conta_maior5 :: [Int] -> ([Int], Int)
conta_maior5 [] = ([],0)
conta_maior5 (x:xs) = if (x > 5) then ([x] ++ fst(conta_maior5 xs),k) else conta_maior5 xs
                      where k = 1 + snd (conta_maior5 xs)

-- Exercicio 22
--busca_mult4 :: [Int] -> (Int, Int)
--busca_mult4 [] = (-1,0)
--busca_mult4 (x:xs) = if (mod x 4 ==0) then k else  (fst (busca_mult4 xs),1+ snd (busca_mult4 xs))
                     --where k = (x,1)

busca_multN :: [Int] -> Int -> (Int, Int)
busca_multN [] _ = (-1,0)
busca_multN (x:xs) n = if (mod x n ==0) then k else  (fst (busca_multN xs n),j)
                     where k = (x,1); j = if (fst (busca_multN xs n) == -1) then 0 else 1+ snd (busca_multN xs n)

-- Exercicio 23
--21 
conta_maior5L :: [Int] -> ([Int], Int)
conta_maior5L [] = ([],0)
conta_maior5L (x:xs) = let k = 1 + snd (conta_maior5L xs)
                       in if (x > 5) then ([x] ++ fst(conta_maior5L xs),k) else conta_maior5L xs

--22
busca_multNL :: [Int] -> Int -> (Int, Int)
busca_multNL [] _ = (-1,0)
busca_multNL (x:xs) n = let k = (x,1); j = if (fst (busca_multNL xs n) == -1) then 0 else 1+ snd (busca_multNL xs n)
                        in if (mod x n ==0) then k else  (fst (busca_multNL xs n),j)
                     
